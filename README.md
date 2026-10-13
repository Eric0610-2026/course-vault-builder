# 课程知识库整理 · Course Vault Builder

[简体中文](#简体中文) · [English](#english) · [GitHub Releases](https://github.com/Eric0610-2026/course-vault-builder/releases)

[![Latest release](https://img.shields.io/github/v/release/Eric0610-2026/course-vault-builder)](https://github.com/Eric0610-2026/course-vault-builder/releases/latest)

面向 ChatGPT 和 Codex 的课程知识库插件：将课件整理为有来源页码、知识互链和清晰导航的 Obsidian 笔记。

## 简体中文

### ✨ 功能

- 按课程结构整理章节笔记、导航与原始课件，保留已有知识库的组织方式。
- 将课件中的知识点关联到原文件和 PDF 物理页码，并在相关笔记间建立有意义的链接。
- 整理 Markdown 表格：表名居中、单元格居中；按需撑满正文宽度并自动调整列宽。
- 支持 Obsidian Markdown、Bases、Canvas、CLI 和 Defuddle 工作流。

### 📦 导入插件

| 添加插件市场 | 上传插件压缩包 |
| --- | --- |
| **ChatGPT 桌面端：**打开 **Plugins → + 添加 → 添加插件市场**，粘贴仓库地址：<br><br>`https://github.com/Eric0610-2026/course-vault-builder`<br><br>添加后，在该市场中选择并安装 **课程知识库整理**。 | **先下载：**[course-vault-builder-1.1.1.zip](https://github.com/Eric0610-2026/course-vault-builder/releases/download/v1.1.1/course-vault-builder-1.1.1.zip)<br><br>然后打开 **Plugins → + 添加 → 上传插件压缩包**，选择刚下载的 ZIP，按界面提示完成导入。 |

> 上传入口是否可用取决于 ChatGPT 账户和工作区权限；若看不到入口，请联系工作区管理员。插件市场方式适用于支持添加 GitHub 插件市场的 ChatGPT 桌面端。

**Codex CLI 用户**也可以添加 GitHub 插件市场：

```sh
codex plugin marketplace add Eric0610-2026/course-vault-builder
codex plugin add course-vault-builder@course-vault-builder
```

### 📊 表格样式

表格规则包括：使用简洁表名；整张表共用一个来源时在表名处引用一次；不同来源按行或单元格标注；删除只重复集中引用的“来源”列。居中、全宽和自动列宽样式由随插件提供的 CSS 片段实现，需在目标 Obsidian 知识库中按需启用。

### 📄 第三方材料与许可

插件随附的 Obsidian 支持技能基于 [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)，其 MIT 许可与版权声明见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。原插件内容未额外授予通用使用或修改许可。

## English

Course Vault Builder is a ChatGPT and Codex plugin that turns course materials into navigable Obsidian notes with page-level citations and useful links between concepts.

### ✨ Features

- Organizes chapter notes, navigation, and original courseware while preserving an existing vault’s structure.
- Ties course claims to source files and physical PDF pages, with meaningful links between related notes.
- Formats Markdown tables with centered captions and cells, plus optional full-width layout and automatic column sizing.
- Includes workflows for Obsidian Markdown, Bases, Canvas, the Obsidian CLI, and Defuddle.

### 📦 Import the plugin

| Add a plugin marketplace | Upload the plugin ZIP |
| --- | --- |
| **In ChatGPT desktop:** open **Plugins → + Add → Add plugin marketplace**, then enter:<br><br>`https://github.com/Eric0610-2026/course-vault-builder`<br><br>After adding it, choose and install **Course Vault Builder** from that marketplace. | **Download:** [course-vault-builder-1.1.1.zip](https://github.com/Eric0610-2026/course-vault-builder/releases/download/v1.1.1/course-vault-builder-1.1.1.zip)<br><br>Then open **Plugins → + Add → Upload plugin ZIP**, select the downloaded file, and follow the prompts. |

> ZIP upload availability depends on your ChatGPT account and workspace permissions. If the option is missing, ask your workspace administrator. Marketplace import requires a ChatGPT desktop client that supports GitHub plugin marketplaces.

**Codex CLI** users can add the GitHub marketplace with:

```sh
codex plugin marketplace add Eric0610-2026/course-vault-builder
codex plugin add course-vault-builder@course-vault-builder
```

### 📊 Table formatting

The table guidance uses concise captions, a single caption citation when the whole table shares one source, and row- or cell-level citations when sources differ. It removes a citation-only `Source` column when the citation is already consolidated in the caption. The bundled CSS snippet optionally centers captions and cells, fills the note width, and lets columns size automatically.

### 📄 Third-party material and license

The bundled Obsidian support skills are adapted from [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills). Their MIT license and copyright notice are included in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). No general reuse license is granted for the original plugin materials.
