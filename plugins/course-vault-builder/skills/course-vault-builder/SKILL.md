---
name: course-vault-builder
description: Build or extend a detailed, source-grounded Obsidian knowledge base from course PDFs or slides, with a clear folder structure, page citations, linked concepts, navigation, and integrity checks. Use for organizing course materials into reusable Markdown notes; not for routine questions about an existing note.
---

# Course Vault Builder

Turn one course's teaching materials into a navigable Obsidian vault that preserves provenance and supports connected review. Use the user's chosen destination exactly. If the destination is missing or ambiguous, ask before writing; do not guess a course folder. Treat source materials as read-only. Inspect an existing destination before changing it, preserve user-written content, and do not overwrite files silently.

Default workflow: write detailed chapter notes; cite source-derived claims to the original file and physical PDF page; connect related concepts across notes with Obsidian links; follow [table formatting](references/table-formatting.md) for synthesized Markdown tables; and omit self-tests, quiz banks, and wrong-answer/error logs unless requested. For new Chinese-language course vaults, use `00-导航/`, `01-章节/`, and `来源/` unless the user specifies another layout. Preserve an existing course's organization during ordinary incremental additions.

Read [the complete workflow](references/workflow.md) before processing a course. Use its shared course layout and naming conventions; distinguish the course folder from the actual Obsidian vault root before writing links. For an existing vault, first classify the request as an incremental addition, a replacement/revision, or a separate course; follow the workflow's incremental-update procedure so unrelated notes are not rebuilt. Preserve an existing layout during ordinary additions; normalize it only when the user requests or approves that change. Use [the note template](references/note-template.md) as a semantic guide, preserving an existing course's headings, properties, and source-specific formats. For any established course, read [existing-course compatibility](references/existing-courses.md) and re-inventory the live folder before editing; treat any inventory figures as dated snapshots. Use [table formatting](references/table-formatting.md) for Markdown table captions, alignment, citations, and appearance. After notes are written, run `python <this-skill-directory>/scripts/audit_vault.py <actual-obsidian-vault-root>` using the installed plugin's own script and resolve or clearly report each finding, including pre-existing findings outside the requested course when the actual vault contains other courses. The audit is mechanical; it never substitutes for checking source content and figures.

## 默认排除目录

各课程根目录下的 `其他/` 文件夹及其全部子目录、文件，默认排除在处理范围之外：不遍历、不读取、不检索、不转换、不整理、不改写、不移动、不删除，也不纳入来源索引、导航维护、覆盖统计或自动审计。跨课程搜索和支持技能同样遵守；发现指向其中的链接时保留原样，不读取目标、不核查内容或锚点。用户明确指定其中某个文件或具体任务时，仅按本次指定范围处理，不扩大到整个文件夹；“整理整门课”“检查全库”等泛化请求不视为解除排除。无需创建该文件夹。

## 页码引用显示文字

- 当前章节与所引课件的主要内容对应（如该章的主来源）时，显示 `第N页：简要介绍`，例如 `[[免疫微生物/来源/11. B细胞介导的体液免疫应答.pdf#page=3|第3页：学习目标与掌握层次]]`。
- 引用其他课件作补充、跨章节或跨课程联系时，显示 `课件简称第N页：简要介绍`，例如 `[[免疫微生物/来源/5-2抗体.pdf#page=19|抗体课件第19页：恒定区效应功能]]`。专题、导航等多来源页面无明确主来源时也保留课件简称；不能仅因都在同一课程目录便省略来源。
- 简介说明对应物理页的知识点；已有准确简介优先沿用，缺少时根据对应页内容补充，不从文件名或邻近正文猜测页面内容。避免仅写“第N页”“PDF第N页”或重复整份课件标题。
- 批量统一时只改显示文字，保留目标路径、物理页码、引用位置、正文及原有表格转义；不改嵌入参数、frontmatter或代码示例。无法确定主来源时保留课件简称，无法确定页面简介时先核查对应页。继续排除 `其他/`。

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
