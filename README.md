<div align="center">

<h1>Course Vault Builder</h1>

A ChatGPT and Codex plugin for building source-grounded Obsidian course knowledge bases.

[简体中文](README_ZH_CN.md) | English

[![Latest release](https://img.shields.io/github/v/release/Eric0610-2026/course-vault-builder)](https://github.com/Eric0610-2026/course-vault-builder/releases/latest)

</div>

## ✨ Features

- Organizes chapter notes, navigation, and original courseware while preserving an existing vault’s structure.
- Ties course claims to source files and physical PDF pages, with meaningful links between related notes.
- Formats Markdown tables with centered captions and cells, plus optional full-width layout and automatic column sizing.
- Includes workflows for Obsidian Markdown, Bases, Canvas, the Obsidian CLI, and Defuddle.

## 📦 Import

| Add a plugin marketplace | Upload a plugin ZIP |
| --- | --- |
| **In ChatGPT desktop:** open **Plugins → + Add → Add plugin marketplace**, then enter:<br><br>`https://github.com/Eric0610-2026/course-vault-builder`<br><br>After adding the marketplace, choose and install **Course Vault Builder**. | **Download:** [course-vault-builder-1.1.1.zip](https://github.com/Eric0610-2026/course-vault-builder/releases/download/v1.1.1/course-vault-builder-1.1.1.zip)<br><br>Then open **Plugins → + Add → Upload plugin ZIP**, select the downloaded file, and follow the prompts. |

> ZIP upload availability depends on your ChatGPT account and workspace permissions. If the option is missing, ask your workspace administrator. Marketplace import requires a ChatGPT desktop client that supports GitHub plugin marketplaces.

### Codex CLI

```sh
codex plugin marketplace add Eric0610-2026/course-vault-builder
codex plugin add course-vault-builder@course-vault-builder
```

## 📊 Table formatting

The table guidance uses concise captions, a single caption citation when the whole table shares one source, and row- or cell-level citations when sources differ. It removes a citation-only `Source` column when the citation is already consolidated in the caption. The bundled CSS snippet optionally centers captions and cells, fills the note width, and lets columns size automatically.

## 📄 Third-party material and license

The bundled Obsidian support skills are adapted from [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills). Their MIT license and copyright notice are included in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). No general reuse license is granted for the original plugin materials.
