# Course-to-Obsidian workflow

Use this procedure for a new course or when extending an existing course vault. Keep a lightweight work log while processing a large set. Coverage claims must be tied to inspected files and pages.

## 1. Confirm scope and destination

Read the user’s request and project instructions first. Determine:

- the exact destination course folder (use the literal path supplied by the user), and the actual Obsidian vault root used to open it; these may differ when several courses share a parent vault;
- which files are inputs, and whether any synced/reference directory is read-only;
- requested depth, course language, whether the vault should include copies of PDFs, and any exclusions;
- whether this is a new vault or an update to an existing one.

Ask only if a missing choice materially changes the result and cannot be inferred. The user's direct request authorizes the requested files and structure; do not expand to unrelated courses or applications. Before writing to a non-empty destination, inventory it, map existing notes to the planned structure, and preserve existing user edits. Never replace a same-named file without inspecting it and preserving its content; merge deliberately or use a clearly named new file.

### Updating an existing course vault when new courseware arrives

Treat this as a targeted update, not a request to rebuild the vault. First confirm the exact existing vault and identify the newly supplied files. If the destination or relationship to an existing course cannot be determined from the user's message and workspace, ask only for that missing information.

Classify each new file before editing:

- **Additional lecture/material:** add it to the source inventory and map it to the chapter/topic notes it supports. Keep all earlier sources and notes.
- **Revised or replacement edition:** preserve both files under distinct, descriptive filenames; never overwrite or delete the earlier source. Mark their version/status in the source index. Treat the new edition as authoritative only when the user or course context makes that clear; otherwise keep conflicting claims attributed to their respective versions and ask which edition should govern when the conflict affects the notes.
- **Different course:** use a separate course folder within a shared parent vault, or a separate vault if that is the user's chosen layout; do not merge its content into another course's notes.

For an incremental update, use this sequence:

1. Inventory the existing vault before changing it: read its home page, source index, folder guide, relevant notes, and current note/template conventions. Record the new files' exact names and actual page/slide counts; keep source files read-only.
2. Map each new file to affected concepts and existing notes. Search for existing passages, citations, and links that cover those concepts. Update only the affected sections and navigation/source-index entries; add a chapter or topic note only when the material is genuinely new and does not fit an existing note. Preserve unrelated notes and user-written material.
3. Compare the new source against the relevant existing notes. Add source-grounded detail and missing process/pathway stages, with physical PDF page citations beside each claim. If the new material changes or contradicts an earlier version, retain provenance for both and state the courseware conflict instead of silently replacing the old account.
4. Add or repair Obsidian links at meaningful concept transitions, including links from new notes to existing prerequisite, mechanism, or outcome notes and back where useful. Update the home page and source index so the new courseware and affected notes are discoverable.
5. Run the vault audit, resolve broken note/heading links and invalid PDF page references, and manually verify the edited claims against the source pages and any relevant diagrams. Confirm original source files and unrelated notes remain intact.
6. Report which source files were added, which notes were created or updated, which existing links/navigation changed, the audit result, and any unresolved version conflicts or unreadable pages. Do not claim that the entire vault was re-reviewed if only affected material was checked.

Reusable request wording (replace the bracketed fields):

> 请把新增课件 `[文件名]` 增量整理到现有 Obsidian 知识库 `[知识库绝对路径]`。先盘点现有目录和相关笔记，只更新受影响的章节/专题及首页、来源索引；保留原课件和无关笔记，不覆盖旧版本。依据课件逐页核实内容，补上 PDF 物理页码来源、过程/途径的完整因果链和有意义的跨笔记链接。不要添加自测题或错题。完成后运行知识库审计，并报告新增/修改了什么及尚未核实之处。若这是旧课件的新版本，请同时标明版本关系；只有无法判断应以哪个版本为准且会影响内容时再询问我。

## 2. Inventory and establish provenance

List source files and their sizes/types. For each PDF, obtain its actual physical page count and note whether it is text-based, scanned, mixed, or contains complex tables/diagrams. For PPT/PPTX, identify slide count and export/reading constraints. Use file names as source identifiers; do not infer content from file names alone.

Create an internal coverage table with source filename, page/slide count, extraction status, visual-review needs, and planned note(s). Keep source materials read-only. If the user requests sources copied into the vault, copy them without editing and verify copied files against originals (hashes when feasible). Otherwise cite them in place using valid relative links when supported; never leave citations pointing at an inaccessible path without saying so.

## 3. Choose the vault layout

Use the following layout for new Chinese-language course vaults managed with this plugin and for explicitly authorized structure normalization. During ordinary incremental additions, preserve the existing organization rather than silently migrating it. A user-specified layout takes precedence.

```text
课程名/
├── 首页.md                  # short entry link, not a second copy of navigation
├── 00-导航/
│   ├── 课程首页.md
│   ├── 文件夹说明.md
│   ├── 来源索引.md
│   └── 整理覆盖与检查报告.md
├── 01-章节/                  # NN-章节标题.md
├── 02-专题/                  # optional cross-chapter concepts
├── 03-逐页资料/              # optional; only if per-page records are produced
├── 来源/                    # original PDFs/slides for this course layout
└── 99-模板/                  # optional reusable note template
```

Keep the four navigation filenames and the `NN-章节标题.md` chapter convention consistent across courses. For a new course, put `00-导航/` and `01-章节/` under the course project root and original courseware under `来源/`, unless the user specifies another layout. During ordinary additions, preserve an existing course's actual structure; do not move sources unless the user requested that migration. Keep optional categories only when they contain useful material; their absence is a deliberate course difference, not a missing requirement. Preserve original filenames, including awkward names. Do not add self-test, quiz, or wrong-answer folders/files by default.

Before normalizing an existing course, map old note paths to new paths, preserve a recoverable copy of affected files, and check incoming references. Update links together with renamed notes. Never rename original sources to match the chapter convention. When several courses share a vault, qualify common names such as 首页, 课程首页, 文件夹说明, and 来源索引 with their course paths to prevent ambiguous links.

Determine link paths from the actual vault root, not merely the current working directory. In a shared parent vault, use targets such as `[[课程名/00-导航/课程首页|课程首页]]` and `[[课程名/来源/Lecture.pdf#page=12|Lecture PDF 第12页]]`; for a standalone course vault, omit the course prefix. Verify the exact path exists before accepting a link; a basename fallback in a mechanical audit does not prove a written path is correct. Do not describe a course subfolder as a standalone vault when its links depend on the parent vault.

## 4. Extract and verify courseware

Use text extraction for searchable text, then compare the extracted material against source pages. Extraction is a draft, not proof of completeness. Check every page/slide for coverage. Visually inspect pages with diagrams, microscopy, anatomy/structure labels, flowcharts, tables, image-only text, multi-column layouts, OCR uncertainty, or garbled reading order. Use visual inspection proportionally: render only pages needing it where possible.

For each inspected page, distinguish:

- explicit statements and terminology in the courseware;
- carefully labeled explanation added to bridge a teaching gap;
- unresolved/illegible material.

Do not silently correct a meaningful conflict or fill unreadable labels by guessing. Record uncertainty with the exact physical page and what needs checking. If multiple decks conflict, state the conflict and retain each provenance.

## 5. Draft the notes

Create one chapter note per logical chapter/lecture unless the user asks for another granularity. Follow the note template. Build a logical hierarchy (overview, concepts, categories, mechanisms, examples, links, sources); explain every listed subtype at the promised level of detail. For example, when a course lists several immune-cell classes, explain each class's defining features and functions as stated in the relevant source pages, instead of leaving a one-line umbrella list.

The template specifies semantic coverage, not mandatory heading names or a required metadata language. In an existing course, retain its heading style and either Chinese or English properties; preserve anatomical structure/location/relations notes as well as immune mechanism/pathway notes. Explain a process chain only where an actual process is taught; do not invent mechanisms for a static anatomical classification. Keep source-only chapter entries clearly marked when teacher courseware is absent. For tables created or revised in synthesized notes, follow [table formatting](table-formatting.md); leave faithful source-format conversions unchanged unless the user asks to reformat them.

Distinguish synthesized chapter notes from per-page text records and original-format conversions. If the user requests a conversion that preserves original wording and formatting, retain headings, emphasis, colors, tables, existing questions, and author attribution as supported by the original; do not inject the chapter template, generated page headings, quizzes, or explanatory sections. Keep page citations and conversion limitations in the relevant chapter/navigation entries when that is the established format. A per-page text layer is a search/traceability aid, not proof that all diagrams or labels were reviewed.

Keep source order and distinctions where they aid fidelity, but synthesize repeated slides into readable prose when the user wants study notes rather than verbatim conversion. Tables are useful for genuine comparisons; do not force unrelated concepts into a table. Add a concise bold caption such as `**表：...**` above each newly authored Markdown table, center columns with `:---:` in each separator cell, escape wikilink display separators as `\|`, and keep logical header/body column counts aligned. Leave source-format HTML tables intact unless their conversion is in scope. Preserve symbols, units, terminology, and qualifiers accurately.

### Physiological processes and pathways

For each process the course covers, write a connected sequence rather than a list of names. Include the trigger or starting substrate, recognition/entry point, ordered intermediates and compartments, branches or convergence, resulting biological effect, and any regulation/limitation the course teaches. For a pathway table, make clear which stages are shared and which are route-specific. Put page citations beside the steps they support, and link to other chapter notes at transitions (for example, antibody recognition → complement activation → phagocyte effector function). Check process diagrams visually because arrows and layout may carry information omitted by extracted text.

Do not expand a course slide's one-line outcome into unsupported molecular steps. If a process is only named or summarized in the source, state what is and is not shown. Any useful professional explanation beyond the courseware must be clearly labeled “补充理解” and have an appropriate source when the user asks for sources; never present it as the teacher's wording.

Use source citations adjacent to the supported paragraph, bullet, or table. If one precise source location supports the whole table, cite once in its caption; if rows use different locations, cite each corresponding row or cell. Remove a citation-only `来源` column when its references are centralized in the caption, but retain `来源` when it describes subject data. Prefer a link with the exact source path and physical page, such as `[[课程名/来源/Lecture.pdf#page=12|Lecture PDF 第12页]]` in a parent vault. Follow the vault-root convention established in section 3. Use physical PDF page numbering starting at page 1, not a printed slide number. For a slide deck without PDF pages, use an exact slide number and filename. Verify source paths against the actual location, including nested subdirectories.

## 6. Connect related notes

Add `[[Note title]]` links at the point where a relationship helps the reader continue. Use `[[Note title#Heading]]` for a specific section only when the heading exists. Prefer a small set of meaningful connections: prerequisite concepts, cause-to-effect steps, shared mechanisms, contrasts, and applications. Make reciprocal links when both pages benefit; do not manufacture links merely to make the graph look dense.

At minimum, the course home page should link to every chapter/topic note; chapter notes should link to directly related chapters and relevant topic notes. The source index should map each original file to the notes it supports. Every citation should allow a reader to return to the specific source page.

## 7. Build navigation and provenance

The course home page should state the course scope, link all chapter/topic notes, group chapters in course order, and give a short map of major concept paths. The source index should list every supplied file, exact filenames and page/slide counts when known, with links to notes and files where accessible; mark administrative files or materials not yet turned into notes rather than silently omitting them. The folder guide should explain each non-empty directory, the actual vault root and entry point, and the rules for adding notes/sources. A template is optional if it will actually be reused.

Persist the factual coverage/check report as `00-导航/整理覆盖与检查报告.md`. Separate current checks from earlier recorded checks. For a structure-only migration, report page-count inventory, renamed/added notes, link checks, and source preservation; explicitly state that course content and diagrams were not re-reviewed. Do not turn an automatic text-layer inventory into a claim of manual page coverage. Update existing reports by preserving useful historical material and appending the current scope and results.

Do not include unsupported completeness claims. A note's source section should be concise and specific, not just a bibliography of every course file.

## 8. Audit and repair

Run the included audit tool on the actual Obsidian vault root. It checks local Obsidian note links and heading fragments; when a PDF reader library is available, it also checks `#page=N` against actual physical page counts. Review every warning. Fix broken links, ambiguous duplicate basenames, invalid heading fragments, and out-of-range PDF pages within the authorized course scope. When the vault contains unrelated notes or hidden skill documentation, preserve them and report their pre-existing findings separately; do not claim the whole vault passed if it did not. Do not suppress a real issue by changing the audit scope; if a link is intentionally external/unverifiable, explain it in the report. Independently verify that explicit directory-qualified targets exist, because basename fallback can hide a mistyped path.

Then manually review representative chapter notes against source pages and all visually uncertain pages. Confirm:

- every expected input is accounted for and every physical page/slide has a coverage status;
- each requested concept/type is actually explained;
- each in-scope physiological process has a readable step chain, accurate branching/convergence, and page references; missing source detail is explicitly bounded;
- no source attribution was inferred from memory or file title alone;
- no self-test or wrong-answer material slipped in against the default;
- chapter links and navigation open the intended targets;
- source files remain intact and the destination contains no accidental temporary/render outputs.

## 9. Deliver clearly

State the exact vault path, structure, number of source files/pages and notes, how source page references work, audit outcome, and any remaining limitations. Offer one sensible next step only after completion (for example, import the folder as an Obsidian vault or add tags/properties if the user wants them). Never claim successful validation unless it was run and passed.
