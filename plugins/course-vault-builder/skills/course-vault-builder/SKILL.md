---
name: course-vault-builder
description: Build or extend a detailed, source-grounded Obsidian knowledge base from course PDFs or slides, with a clear folder structure, page citations, linked concepts, navigation, and integrity checks. Use for organizing course materials into reusable Markdown notes; not for routine questions about an existing note.
---

# Course Vault Builder

Turn one course's teaching materials into a navigable Obsidian vault that preserves provenance and supports connected review. Use the user's chosen destination exactly. If the destination is missing or ambiguous, ask before writing; do not guess a course folder. Treat source materials as read-only. Inspect an existing destination before changing it, preserve user-written content, and do not overwrite files silently.

Default workflow: write detailed chapter notes; cite source-derived claims to the original file and physical PDF page; connect related concepts across notes with Obsidian links; follow [table formatting](references/table-formatting.md) for synthesized Markdown tables; and omit self-tests, quiz banks, and wrong-answer/error logs unless requested. For new Chinese-language course vaults, use `00-导航/`, `01-章节/`, and `来源/` unless the user specifies another layout. Preserve an existing course's organization during ordinary incremental additions.

Read [the complete workflow](references/workflow.md) before processing a course. Use its shared course layout and naming conventions; distinguish the course folder from the actual Obsidian vault root before writing links. For an existing vault, first classify the request as an incremental addition, a replacement/revision, or a separate course; follow the workflow's incremental-update procedure so unrelated notes are not rebuilt. Preserve an existing layout during ordinary additions; normalize it only when the user requests or approves that change. Use [the note template](references/note-template.md) as a semantic guide, preserving an existing course's headings, properties, and source-specific formats. For any established course, read [existing-course compatibility](references/existing-courses.md) and re-inventory the live folder before editing; treat any inventory figures as dated snapshots. Use [table formatting](references/table-formatting.md) for Markdown table captions, alignment, citations, and appearance. After notes are written, run `python <this-skill-directory>/scripts/audit_vault.py <actual-obsidian-vault-root>` using the installed plugin's own script and resolve or clearly report each finding, including pre-existing findings outside the requested course when the actual vault contains other courses. The audit is mechanical; it never substitutes for checking source content and figures.

## Core requirements

- Inventory every supplied source before claiming coverage. Record actual filenames and page counts; distinguish text, scan/OCR, mixed, and visual-heavy files.
- Separate source files from notes. Never modify, rename, move, or delete user-provided/synced source files. Copy them only when the user wants a self-contained vault and the destination layout calls for copies.
- Organize notes by the actual course/chapter structure within the shared layout. Keep `首页.md` as a short entry pointing to `00-导航/课程首页.md`; put the source index, folder guide, and factual coverage/check report in `00-导航`. Name chapter notes `NN-章节标题.md`. Cross-cutting topic notes, per-page records, and reusable templates are conditional, not mandatory empty folders.
- Write explanations at the requested depth. Preserve course terminology and distinctions; do not fill gaps with invented claims. Label explanatory outside knowledge as supplementary and keep it distinct from what the slides explicitly state.
- Preserve the role of each file: synthesized chapter notes, cross-chapter topics, per-page extraction records, and original-format reference conversions are different outputs. Do not impose the chapter template on original-format conversions or replace source-specific notes with a uniform scaffold.
- For every physiological process or pathway in scope, explain the chain rather than only naming it: trigger/source → recognition or entry → ordered steps/branches → convergence point → effect/result → regulation or limitation when taught. Cite the source page(s) beside the relevant steps and link connected processes across notes. If the courseware only gives a summary or stops before a mechanism, state that boundary instead of fabricating missing steps.
- Cite claims locally with a stable file-and-physical-page reference. In tables, put each distinct source in its corresponding row or cell; when the whole table uses one source location, cite it once in the caption and omit a redundant citation-only `来源` column. Keep `来源` when it describes subject data. Use Obsidian links that point to the exact source PDF and `#page=N`; do not confuse printed slide labels with the physical PDF page.
- Add links between notes where they express a real prerequisite, mechanism, comparison, or shared concept. Check both target notes and heading fragments.
- Do not create quizzes, self-tests, flashcards, or wrong-answer logs by default. Existing questions and answers in user-supplied reference materials may be preserved when their conversion is requested; this is not permission to generate new questions or certify their answers.
- Finish with a factual coverage report: files and pages inspected, notes created/updated, audit results, and any pages/figures/tables that remain uncertain.

## Bundled supporting skills

Read [the integration contract](references/supporting-skills.md) when a task needs a supporting capability, then read only the matching bundled skill. These skills are packaged with this plugin; do not assume separate global installations are required.

- [obsidian-markdown](../obsidian-markdown/SKILL.md): Wikilinks, embeds, callouts, properties, and Markdown formatting for chapter/navigation edits.
- [obsidian-bases](../obsidian-bases/SKILL.md): `.base` views of existing notes when the user requests a course index, table, cards, or progress view.
- [json-canvas](../json-canvas/SKILL.md): `.canvas` maps when the user requests a knowledge map or visual course relationships.
- [obsidian-cli](../obsidian-cli/SKILL.md): Read, search, manage, or verify a running Obsidian vault; explicitly target its name and exact vault-relative path including the course folder prefix.
- [defuddle](../defuddle/SKILL.md): Extract user-requested HTML/web sources as supplementary material with URL/date provenance; it does not replace PDF reading or OCR.

An ordinary course update does not automatically create Bases, Canvas files, daily notes, tasks, or web-source downloads. Use those outputs only within the requested task. Continue to preserve the actual course structure, sources, and existing note conventions.
