<div align="center">

<h1>课程知识库整理</h1>

面向 ChatGPT 和 Codex 的课程知识库插件：将课件整理为有来源页码、知识互链和清晰导航的 Obsidian 笔记。

简体中文 | [English](README.md)

[![最新版本](https://img.shields.io/github/v/release/Eric0610-2026/course-vault-builder)](https://github.com/Eric0610-2026/course-vault-builder/releases/latest)

</div>

## ✨ 功能

- 按课程结构整理章节笔记、导航与原始课件，保留已有知识库的组织方式。
- 将课件知识点关联到原文件和 PDF 物理页码，并在相关笔记间建立有意义的链接。
- 整理 Markdown 表格：表名和单元格居中；按需撑满正文宽度并自动调整列宽。
- 支持 Obsidian Markdown、Bases、Canvas、CLI 和 Defuddle 工作流。

## 📦 导入插件

| 添加插件市场 | 上传插件压缩包 |
| --- | --- |
| **在 ChatGPT 桌面端：**打开 **Plugins → + 添加 → 添加插件市场**，粘贴仓库地址：<br><br>`https://github.com/Eric0610-2026/course-vault-builder`<br><br>添加后，在该市场中选择并安装 **课程知识库整理**。 | **先下载：**[course-vault-builder-1.1.2.zip](https://github.com/Eric0610-2026/course-vault-builder/releases/download/v1.1.2/course-vault-builder-1.1.2.zip)<br><br>然后打开 **Plugins → + 添加 → 上传插件压缩包**，选择下载的 ZIP，按界面提示完成导入。 |

> ZIP 上传入口是否可用取决于 ChatGPT 账户和工作区权限；若看不到入口，请联系工作区管理员。插件市场导入需要支持 GitHub 插件市场的 ChatGPT 桌面端。

### Codex CLI

```sh
codex plugin marketplace add Eric0610-2026/course-vault-builder
codex plugin add course-vault-builder@course-vault-builder
```

## 📊 表格样式

表格规则包括：使用简洁表名；整张表共用一个来源时在表名处引用一次；不同来源按行或单元格标注；删除只重复集中引用的“来源”列。随插件提供的 CSS 片段可按需居中表名和单元格、撑满正文宽度并自动调整列宽。

## 📄 第三方材料与许可

插件随附的 Obsidian 支持技能基于 [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)，其 MIT 许可与版权声明见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。原插件内容未额外授予通用使用或修改许可。
