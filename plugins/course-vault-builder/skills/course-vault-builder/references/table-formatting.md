# Markdown table formatting

Use these defaults when creating or revising synthesized Markdown tables. Preserve the user's requested style and leave faithful source-format conversions unchanged unless conversion of their tables is explicitly in scope.

## Table caption and alignment

- Put a concise bold caption such as `**表：基础代谢率的年龄与性别差异**` on its own line immediately before each Markdown table, with a blank line between caption and table.
- Center every column by writing `:---:` in each table separator cell, with at least three hyphens. Keep the logical column count aligned across the header, separator, and data rows. In Markdown tables, escape wikilink display separators as `\|` so they remain within one cell.
- Center table captions and cells, fill the available note width, and use automatic column layout when the user requests this appearance or the selected vault's conventions call for it. The CSS snippet is [表格居中自适应.css](../assets/表格居中自适应.css).

## Source citations and columns

- When the whole table is supported by one precise source location, cite it once in the caption. When rows rely on different pages or sources, put each citation beside the supported row or cell.
- Remove a `来源` column when it only repeats citations consolidated in the caption. Keep a `来源` column when it contains subject data, such as the type or category being compared.
- Never infer that every row has one source merely because the rows appear together; check the actual citations before moving or removing them.

## Vault appearance

When the user requests full-width table styling, place the CSS asset in `<vault-root>/.obsidian/snippets/表格居中自适应.css` and enable it for that vault. If Obsidian CLI is available, use `snippet:enable name=表格居中自适应`; otherwise enable it in **Settings → Appearance → CSS snippets** and report whether that was verified. Only add or activate CSS in the explicitly selected vault; do not change an unrelated vault's appearance.
