# 课程知识库整理 (Course Vault Builder)

A Codex plugin for creating and incrementally updating source-grounded Obsidian course knowledge bases.

## What it does

- Organizes course notes, navigation, and original courseware while preserving an existing vault's structure.
- Keeps source citations tied to exact physical PDF pages and encourages useful links between related notes.
- Formats synthesized Markdown tables with captions, centered columns, and optional full-width automatic layout.
- Bundles supporting skills for Obsidian Markdown, Bases, JSON Canvas, the Obsidian CLI, and Defuddle.

## Install in Codex

Add this GitHub repository as a marketplace, then install the plugin:

```sh
codex plugin marketplace add Eric0610-2026/course-vault-builder
codex plugin add course-vault-builder@course-vault-builder
```

Restart the Codex desktop app if the plugin does not appear immediately. To update later, refresh the marketplace and reinstall the plugin from the same marketplace.

## Table styling

The packaged table-formatting reference explains Markdown captions, alignment markers, citation placement, and the optional CSS snippet. Install that snippet only in the vault where the user requests the full-width visual style.

## Third-party material

The bundled Obsidian supporting skills are adapted from [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) and are covered by its MIT license. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). No additional license is granted for the original plugin materials in this repository.
