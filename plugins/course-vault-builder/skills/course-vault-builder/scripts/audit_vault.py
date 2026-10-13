#!/usr/bin/env python3
"""Audit local Obsidian wikilinks in a vault without third-party dependencies.

Optionally validates PDF #page=N links when pypdf or PyMuPDF is installed.
Usage: python audit_vault.py VAULT_ROOT
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

WIKILINK = re.compile(r"!?\[\[([^\]]+)\]\]")
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)
BLOCK = re.compile(r"\^([A-Za-z0-9_-]+)\s*$", re.MULTILINE)
FENCE = re.compile(r"^[ \t]{0,3}(`{3,}|~{3,})([^\r\n]*)")
HTML_CODE = re.compile(r"<(code|pre)\b[^>]*>.*?</\1\s*>", re.I | re.S)


def blank_code(value: str) -> str:
    """Keep offsets/newlines while masking literal code examples."""
    return re.sub(r"[^\r\n]", " ", value)


def without_code_blocks(text: str) -> str:
    """Mask backtick/tilde fences and HTML code/pre, without excluding files."""
    lines: list[str] = []
    fence: str | None = None
    for line in text.splitlines(keepends=True):
        match = FENCE.match(line)
        if fence is not None:
            lines.append(blank_code(line))
            if (match and match[1][0] == fence[0]
                    and len(match[1]) >= len(fence) and not match[2].strip()):
                fence = None
            continue
        if match and not (match[1][0] == "`" and "`" in match[2]):
            fence = match[1]
            lines.append(blank_code(line))
        else:
            lines.append(line)
    return HTML_CODE.sub(lambda m: blank_code(m[0]), "".join(lines))


def without_inline_code(text: str) -> str:
    """Code spans close with a matching backtick-run length; unmatched runs stay."""
    result = list(text)
    position = 0
    while match := re.search(r"`+", text[position:]):
        start = position + match.start()
        end = position + match.end()
        # A backslash-escaped opener is literal punctuation, not a code span.
        backslashes = len(text[:start]) - len(text[:start].rstrip("\\"))
        if backslashes % 2:
            position = end
            continue
        delimiter = match[0]
        close = re.search(r"(?<!`)" + re.escape(delimiter) + r"(?!`)", text[end:])
        if close is None:
            position = end
            continue
        stop = end + close.end()
        result[start:stop] = blank_code(text[start:stop])
        position = stop
    return "".join(result)


def link_text(text: str) -> str:
    return without_inline_code(without_code_blocks(text))


def heading_slug(value: str) -> str:
    value = value.strip().lower().replace(" ", "-")
    return re.sub(r"[^\w\-]", "", value, flags=re.UNICODE)


def pdf_page_count(path: Path) -> int | None:
    try:
        from pypdf import PdfReader  # type: ignore
        return len(PdfReader(str(path)).pages)
    except ImportError:
        pass
    try:
        import fitz  # type: ignore
        with fitz.open(path) as doc:
            return doc.page_count
    except ImportError:
        return None
    except Exception:
        return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vault_root", type=Path)
    args = parser.parse_args()
    root = args.vault_root.expanduser().resolve()
    if not root.is_dir():
        print(f"ERROR: vault folder not found: {root}")
        return 2

    notes = sorted(p for p in root.rglob("*.md") if p.is_file())
    if not notes:
        print("ERROR: no Markdown notes found")
        return 2

    by_rel: dict[str, Path] = {}
    by_name: dict[str, list[Path]] = {}
    by_file_name: dict[str, list[Path]] = {}
    for path in root.rglob("*"):
        if path.is_file():
            by_file_name.setdefault(path.name.casefold(), []).append(path)
    contents: dict[Path, str] = {}
    for note in notes:
        rel = note.relative_to(root).with_suffix("").as_posix().casefold()
        by_rel[rel] = note
        by_name.setdefault(note.stem.casefold(), []).append(note)
        try:
            contents[note] = note.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError) as exc:
            contents[note] = ""
            print(f"ERROR: cannot read {note.relative_to(root)}: {exc}")

    errors = warnings = checked = ignored_code_links = 0
    pdf_counts: dict[Path, int | None] = {}
    pdf_count_warnings: set[Path] = set()

    def resolve_target(source: Path, target: str) -> tuple[Path | None, list[Path]]:
        target = target.replace("\\", "/")
        candidate_text = target.lstrip("/")
        candidates: list[Path] = []
        if candidate_text:
            raw = Path(candidate_text)
            for base in (source.parent, root):
                candidate = (base / raw).resolve()
                try:
                    candidate.relative_to(root)
                except ValueError:
                    continue
                if candidate.is_file():
                    candidates.append(candidate)
                elif not candidate.suffix:
                    md = candidate.with_suffix(".md")
                    if md.is_file():
                        candidates.append(md)
        if candidates:
            uniq = list(dict.fromkeys(candidates))
            return (uniq[0] if len(uniq) == 1 else None, uniq)

        if Path(candidate_text).suffix:
            files = by_file_name.get(Path(candidate_text).name.casefold(), [])
            return (files[0] if len(files) == 1 else None, files)

        stem = Path(candidate_text).stem.casefold()
        matches = by_name.get(stem, []) if stem else []
        return (matches[0] if len(matches) == 1 else None, matches)

    for note in notes:
        text = contents[note]
        active_text = link_text(text)
        for match in WIKILINK.finditer(text):
            # Keep the original target: a real heading fragment may itself
            # contain backticks. Only the link opener decides if it is in code.
            if active_text[match.start()] != text[match.start()]:
                ignored_code_links += 1
                continue
            checked += 1
            raw = match.group(1).replace(r"\|", "|").split("|", 1)[0].strip()
            if not raw:
                continue
            # Templates may intentionally contain unresolved example links.
            if "{{" in raw or "}}" in raw:
                continue
            target_part, sep, fragment = raw.partition("#")
            # Obsidian permits [[#Heading]] to mean a heading in the current note.
            if not target_part and sep:
                target, matches = note, [note]
            else:
                target, matches = resolve_target(note, target_part)

            where = f"{note.relative_to(root).as_posix()}"
            if target is None:
                errors += 1
                if len(matches) > 1:
                    found = ", ".join(p.relative_to(root).as_posix() for p in matches)
                    print(f"ERROR: ambiguous link in {where}: [[{raw}]] -> {found}")
                else:
                    print(f"ERROR: broken link in {where}: [[{raw}]]")
                continue

            if target.suffix.casefold() == ".pdf":
                # File-level source links are valid; page citations need #page=N.
                if not sep:
                    continue
                if not re.fullmatch(r"page=\d+", fragment, flags=re.I):
                    warnings += 1
                    print(f"WARNING: PDF link has no physical #page=N in {where}: [[{raw}]]")
                    continue
                page = int(fragment.split("=", 1)[1])
                if target not in pdf_counts:
                    pdf_counts[target] = pdf_page_count(target)
                count = pdf_counts[target]
                if page < 1:
                    errors += 1
                    print(f"ERROR: invalid PDF page in {where}: [[{raw}]]")
                elif count is None:
                    if target not in pdf_count_warnings:
                        warnings += 1
                        pdf_count_warnings.add(target)
                        print(f"WARNING: cannot validate page ranges in {target.relative_to(root).as_posix()} (install pypdf or PyMuPDF)")
                elif page > count:
                    errors += 1
                    print(f"ERROR: PDF page {page} exceeds {count} pages in {where}: [[{raw}]]")
                continue

            if sep and fragment and not fragment.startswith("^"):
                headings = {heading_slug(h) for h in HEADING.findall(without_code_blocks(contents.get(target, "")))}
                if heading_slug(fragment) not in headings:
                    errors += 1
                    print(f"ERROR: missing heading anchor in {where}: [[{raw}]]")
            elif sep and fragment.startswith("^"):
                block_ids = set(BLOCK.findall(link_text(contents.get(target, ""))))
                if fragment[1:] not in block_ids:
                    errors += 1
                    print(f"ERROR: missing block anchor in {where}: [[{raw}]]")

    print(f"Checked {checked} Obsidian links across {len(notes)} Markdown notes.")
    print(f"Ignored {ignored_code_links} wikilink examples inside code blocks/spans (files remain in audit).")
    print(f"Errors: {errors}; warnings: {warnings}.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
