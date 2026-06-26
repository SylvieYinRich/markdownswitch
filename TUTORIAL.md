# MarkItDown Desktop 使用教程 / User Guide

## 目录 / Table of Contents

- [快速开始 / Quick Start](#快速开始--quick-start)
- [界面介绍 / Interface](#界面介绍--interface)
- [基础操作 / Basic Operations](#基础操作--basic-operations)
- [高级功能 / Advanced Features](#高级功能--advanced-features)
- [常见场景 / Common Scenarios](#常见场景--common-scenarios)
- [故障排除 / Troubleshooting](#故障排除--troubleshooting)

---

## 快速开始 / Quick Start

### 第一步：启动程序 / Launch

双击 `MarkItDown.exe`（Windows）或 `MarkItDown`（macOS）

Double-click `MarkItDown.exe` (Windows) or `MarkItDown` (macOS)

### 第二步：添加文件 / Add Files

有三种方式添加文件 / Three ways to add files：

1. **拖拽文件** - 直接把文件拖到窗口 / Drag files to window
2. **拖拽文件夹** - 把整个文件夹拖到窗口（推荐）/ Drag entire folder (recommended)
3. **点击按钮** - 点击「打开文件」选择文件 / Click "Open File" button

### 第三步：开始转换 / Convert

点击「开始批量转换」按钮 / Click "Start Batch Convert"

### 第四步：保存结果 / Save

点击「保存 Markdown 文件」，选择输出目录 / Click "Save Markdown" and choose output directory

---

## 界面介绍 / Interface

```
┌─────────────────────────────────────────────────────┐
│  文件(F)  视图(V)    File   View                      │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌───────────────────────────────────────────────┐  │
│  │    拖拽文件或文件夹到此处                        │  │
│  │    Drag files or folder here                   │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  [输入 URL / Input URL]           [打开文件 / Open]  │
│                                                     │
│  文件队列 (15)  File Queue          [清空 / Clear]   │
│  ┌─────────────────────────────────────────────┐    │
│  │ ✓ 报表.pdf  Report.pdf                      │    │
│  │ ✓ 总结.docx Summary.docx                    │    │
│  │ ⏳ 数据.xlsx Data.xlsx                       │    │
│  │ ○ 计划.pptx Plan.pptx                        │    │
│  └─────────────────────────────────────────────┘    │
│                                                     │
│  [开始转换 / Start] [取消 / Cancel]  并发: [4]       │
│  [保存 Markdown / Save]                             │
│  ████████████████░░░░  75%                          │
│  已完成/Done: 12/16  成功/OK: 11  失败/Fail: 1       │
│                                                     │
├─────────────────────────────────────────────────────┤
│  Markdown 渲览 / Preview  │  Markdown 源码 / Source  │
│                           │                         │
│  # 标题 / Heading         │  # 标题 / Heading        │
│  这是内容... / Content... │  这是内容... / Content...│
│                           │                         │
└─────────────────────────────────────────────────────┘
```

### 区域说明 / Areas

| 区域 Area | 功能 Function |
|------|------|
| **菜单栏 Menu** | 文件操作、主题切换 / File ops, theme toggle |
| **拖拽区 Drop Zone** | 拖入文件或文件夹 / Drop files or folder |
| **URL 输入框 URL Input** | 输入网页链接转换 / Convert web pages |
| **文件队列 File Queue** | 显示待转换的文件 / Show pending files |
| **按钮区 Buttons** | 批量转换、取消、保存 / Batch convert, cancel, save |
| **进度条 Progress** | 显示转换进度 / Show conversion progress |
| **状态标签 Status** | 显示成功/失败统计 / Show success/fail stats |
| **预览区 Preview** | 左侧渲染预览，右侧源码 / Left: render, Right: source |

---

## 基础操作 / Basic Operations

### 操作 1：转换单个文件 / Convert Single File

```
步骤 Steps：
1. 拖入文件 → 文件出现在队列    Drag file → appears in queue
2. 点击「开始批量转换」          Click "Start Batch Convert"
3. 等待转换完成                  Wait for conversion
4. 点击「保存 Markdown 文件」    Click "Save Markdown"
5. 选择保存位置                  Choose save location
```

### 操作 2：批量转换 / Batch Convert

```
步骤 Steps：
1. 拖入多个文件（或整个文件夹）  Drag multiple files (or folder)
2. 调整并发数（可选）            Adjust concurrency (optional)
3. 点击「开始批量转换」          Click "Start Batch Convert"
4. 等待所有文件转换完成          Wait for all files
5. 点击「保存 Markdown 文件」    Click "Save Markdown"
6. 选择保存目录                  Choose output directory
```

### 操作 3：转换网页 / Convert Web Page

```
步骤 Steps：
1. 复制网页链接                  Copy web URL
2. 粘贴到 URL 输入框             Paste into URL input
3. 点击「转换 URL」              Click "Convert URL"
4. 等待转换完成                  Wait for conversion
5. 预览结果                      Preview result
6. 点击「保存 Markdown 文件」    Click "Save Markdown"
```

---

## 高级功能 / Advanced Features

### 功能 1：调整并发数 / Adjust Concurrency

并发数决定同时处理几个文件 / Concurrency determines how many files to process simultaneously：

| 并发数 | 适用场景 |
|--------|----------|
| **1** | 单线程，最稳定，最慢 / Single thread, slowest but stable |
| **2-4** | 推荐设置，平衡速度和稳定性 / Recommended, balanced |
| **8-16** | 高性能电脑，速度最快 / High-performance PC, fastest |

**建议 Recommendations：**
- 普通文件 Normal files：4
- 大文件 Large files (>50MB)：2
- 小文件 Small files (<1MB)：8-16

### 功能 2：切换主题 / Toggle Theme

按 `Ctrl+T` 或点击菜单「视图 → 切换主题」/ Press `Ctrl+T` or View → Toggle Theme

- **浅色主题 Light** - 默认主题，清晰明亮 / Default, clear and bright
- **深色主题 Dark** - 护眼，适合长时间使用 / Eye-friendly, for long sessions

### 功能 4：切换语言 / Switch Language

点击菜单栏 **「中文 / EN」** / Click **「中文 / EN」** in menu bar

- **中文** - 界面显示中文 / Chinese UI
- **English** - 界面显示英文 / English UI

### 功能 5：目录结构保持 / Keep Folder Structure

拖入文件夹时，自动保持原目录结构 / Auto-keep structure when dragging folder

```
输入 Input：
D:\工作\2024\
├── 报表.pdf
└── 总结.docx

输出 Output（选择目录后）：
输出目录\
├── 报表.md
└── 总结.md

嵌套目录 Nested：
输入：D:\工作\2024\一月\报表.pdf
输出：输出目录\一月\报表.md
```

---

## 常见场景 / Common Scenarios

### 场景 1：整理工作文档 / Organize Work Documents

**需求 Requirement：** 把一个月的工作文档全部转成 Markdown / Convert a month's documents to Markdown

```
步骤 Steps：
1. 把整个月的文件夹拖入        Drag the month's folder
2. 开始批量转换                Start batch convert
3. 保存到新目录                Save to new directory
4. 用 Markdown 编辑器整理      Organize with Markdown editor
```

### 场景 2：制作知识库 / Build Knowledge Base

**需求 Requirement：** 把各种资料转成 Markdown 导入知识库 / Convert materials to Markdown for knowledge base

```
步骤 Steps：
1. 按主题整理文件夹            Organize folders by topic
2. 分别拖入转换                Drag and convert separately
3. 保存时保持目录结构          Keep folder structure when saving
4. 导入 Obsidian/Notion 等工具  Import to Obsidian/Notion
```

### 场景 3：备份网页内容 / Backup Web Pages

**需求 Requirement：** 把重要网页转成 Markdown 备份 / Backup important web pages as Markdown

```
步骤 Steps：
1. 复制网页链接                Copy web URL
2. 粘贴到 URL 输入框           Paste into URL input
3. 转换并保存                  Convert and save
4. 定期备份                    Backup regularly
```

### 场景 4：处理扫描文档 / Process Scanned Documents

**需求 Requirement：** 把扫描的 PDF 转成可编辑文本 / Convert scanned PDF to editable text

```
步骤 Steps：
1. 拖入 PDF 文件               Drag PDF file
2. 程序自动 OCR 识别           Program auto-OCR
3. 保存为 Markdown             Save as Markdown
4. 编辑和搜索内容              Edit and search content
```

---

## 故障排除 / Troubleshooting

### 问题 1：程序打不开 / App Won't Launch

**Windows：**
- 检查是否被杀毒软件拦截 / Check if blocked by antivirus
- 尝试右键以管理员身份运行 / Try right-click → Run as administrator

**macOS：**
- 右键点击应用，选择「打开」/ Right-click app, choose "Open"
- 或在「系统设置 → 隐私与安全性」中允许 / Or allow in System Settings → Privacy & Security

### 问题 2：文件拖不进去 / Files Won't Drag In

- 确认文件格式支持 / Check if format is supported
- 尝试用「打开文件」按钮 / Try "Open File" button
- 重启程序后再试 / Restart app and try again

### 问题 3：转换很慢 / Slow Conversion

- 增加并发数 / Increase concurrency
- 关闭其他占用资源的程序 / Close other resource-heavy apps
- 检查文件大小 / Check file size

### 问题 4：转换失败 / Conversion Failed

- 检查文件是否损坏 / Check if file is corrupted
- 确认文件格式支持 / Confirm format is supported
- 尝试用其他软件打开原文件 / Try opening with other software
- 查看状态栏错误信息 / Check status bar error message

### 问题 5：保存失败 / Save Failed

- 检查输出目录是否有写入权限 / Check write permissions
- 确认磁盘空间足够 / Check disk space
- 尝试保存到其他位置 / Try saving elsewhere

### 问题 6：转换失败显示 0 个成功 / Conversion Shows 0 Success

- 确保使用的是最新版本的 exe / Ensure you're using the latest exe version
- 旧版本可能缺少 magika 模型文件 / Older versions may be missing magika model files
- 重新下载 Releases 中的最新版本 / Re-download latest from Releases

---

## 快捷键一览 / Shortcuts

| 快捷键 Shortcut | 功能 Function | 说明 Note |
|--------|------|------|
| `Ctrl+O` | 打开文件 / Open file | 弹出文件选择对话框 / Open file dialog |
| `Ctrl+S` | 保存 Markdown / Save | 弹出保存对话框 / Open save dialog |
| `Ctrl+T` | 切换主题 / Toggle theme | 浅色/深色切换 / Light/Dark toggle |
| `Ctrl+Q` | 退出程序 / Quit | 退出前确认 / Confirm before quit |

---

<div align="center">

**祝你使用愉快！/ Enjoy using MarkItDown Desktop!**

</div>
