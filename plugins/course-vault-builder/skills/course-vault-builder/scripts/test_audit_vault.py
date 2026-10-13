"""Regression checks: literal examples are ignored, real broken links still fail."""
import contextlib
import io
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

import audit_vault as audit


class CodeExampleTests(unittest.TestCase):
    def links(self, text):
        return audit.WIKILINK.findall(audit.link_text(text))

    def test_backtick_and_tilde_fences(self):
        self.assertEqual(self.links("```md\n[[Fake]]\n```\n[[Real]]\n~~~md\n[[Fake2]]\n~~~\n"), ["Real"])

    def test_longer_fence_and_unclosed_block(self):
        self.assertEqual(self.links("````md\n```\n[[Fake]]\n````\n[[Real]]\n~~~\n[[Unclosed]]"), ["Real"])

    def test_inline_code_matching_run_length(self):
        self.assertEqual(self.links("`[[Fake]]` ``a ` [[Fake2]]`` [[Real]]"), ["Real"])

    def test_html_code_and_pre(self):
        self.assertEqual(self.links('<code class="example">![[Fake.base]]</code>\n<PRE>[[Fake2]]</PRE> [[Real]]'), ["Real"])

    def test_unmatched_and_escaped_backticks(self):
        self.assertEqual(self.links("` unmatched [[Real]]"), ["Real"])
        self.assertEqual(self.links(r"\` [[Real]] \`"), ["Real"])

    def test_frontmatter_and_real_embeds_remain(self):
        self.assertEqual(self.links('---\nsource: "[[Source]]"\n---\n![[Real]]'), ["Source", "Real"])

    def test_mask_preserves_offsets_and_line_breaks(self):
        text = "``code [[Fake]]\nnext``\n[[Real]]"
        masked = audit.link_text(text)
        self.assertEqual(len(text), len(masked))
        self.assertEqual([i for i,c in enumerate(text) if c=="\n"], [i for i,c in enumerate(masked) if c=="\n"])

    def run_audit(self, files):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for name, text in files.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8")
            output = io.StringIO()
            with patch.object(sys, "argv", ["audit_vault.py", str(root)]), contextlib.redirect_stdout(output):
                status = audit.main()
            return status, output.getvalue()

    def test_skill_file_real_link_still_fails(self):
        status, output = self.run_audit({".agents/skills/example/SKILL.md": "`[[Fake]]`\n~~~\n[[Fake2]]\n~~~\n[[Actually missing]]"})
        self.assertEqual(status, 1)
        self.assertIn("[[Actually missing]]", output)
        self.assertNotIn("ERROR: broken link in .agents/skills/example/SKILL.md: [[Fake", output)
        self.assertIn("Ignored 2", output)

    def test_valid_heading_with_inline_code_and_block(self):
        status, output = self.run_audit({"a.md": "[[b#An `API` heading]] [[b#^ok]]", "b.md": "## An `API` heading\nText ^ok\n"})
        self.assertEqual(status, 0, output)

    def test_fenced_heading_does_not_validate_real_anchor(self):
        status, output = self.run_audit({"a.md": "[[b#Fake]]", "b.md": "```md\n## Fake\n```\n"})
        self.assertEqual(status, 1)
        self.assertIn("missing heading anchor", output)


if __name__ == "__main__":
    unittest.main()
