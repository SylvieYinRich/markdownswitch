# MarkItDown Desktop

<div align="center">

**将任意文件一键转换为 Markdown 的桌面工具**
**Desktop tool to convert any file to Markdown with one click**

[![Windows](https://img.shields.io/badge/Windows-下载%20Download-blue)](#下载--download)
[![macOS](https://img.shields.io/badge/macOS-下载%20Download-green)](#下载--download)
[![License](https://img.shields.io/badge/License-MIT-yellow)](#license)

</div>

---

## 功能特性 / Features

| 功能 Feature | 说明 Description |
|------|------|
| **文件拖拽 Drag & Drop** | 直接拖入文件或整个文件夹 / Drag files or entire folders |
| **批量转换 Batch Convert** | 支持上千文件并发处理 / Process thousands of files concurrently |
| **目录结构保持 Keep Structure** | 自动按原文件夹结构保存 .md 文件 / Save .md files preserving original folder structure |
| **URL 转换 URL Convert** | 输入网页链接直接转换 / Convert web pages by URL |
| **Markdown 预览 Preview** | 实时渲染预览 + 源码双栏显示 / Live render preview + source code side by side |
| **深色/浅色主题 Dark/Light Theme** | 默认浅色，一键切换 / Default light, one-click toggle |
| **中英文切换 Bilingual** | 菜单栏切换中文 / English / Switch between Chinese & English |
| **跨平台 Cross-Platform** | 支持 Windows / macOS / Supports Windows & macOS |

## 支持格式 / Supported Formats

| 类型 Type | 格式 Formats |
|------|------|
| **文档 Documents** | PDF, Word (.doc/.docx), PowerPoint (.ppt/.pptx), Excel (.xls/.xlsx) |
| **文本 Text** | TXT, Markdown, RST, CSV, JSON, XML |
| **网页 Web** | HTML, HTM, RSS |
| **图片 Images** | JPG, PNG, GIF, BMP, TIFF, WebP (EXIF + OCR) |
| **音频 Audio** | MP3, WAV, FLAC, OGG, M4A (语音转文字 / Speech to text) |
| **压缩包 Archives** | ZIP (递归转换内部文件 / Recursively convert internal files) |
| **电子书 E-books** | EPUB |
| **其他 Others** | Jupyter Notebook (.ipynb), Outlook (.msg) |

## 下载 / Download

### Windows

1. 点击 [Releases](../../releases) 下载最新版本 / Download latest from [Releases](../../releases)
2. 解压 `MarkItDown-Windows.zip` / Extract `MarkItDown-Windows.zip`
3. 双击 `MarkItDown.exe` 运行（无需安装 Python）/ Double-click `MarkItDown.exe` (no Python needed)

> **注意 Notice：** Windows 版本约 250MB（包含所有转换引擎和模型文件）
> Windows version is ~250MB (includes all conversion engines and model files)

### macOS

1. 点击 [Releases](../../releases) 下载最新版本 / Download latest from [Releases](../../releases)
2. 解压 `MarkItDown-Mac.zip` / Extract `MarkItDown-Mac.zip`
3. 双击 `MarkItDown` 运行 / Double-click `MarkItDown` to run

> **注意 Notice：** macOS 首次运行可能需要在「系统设置 → 隐私与安全性」中允许运行
> First launch on macOS may require allowing in "System Settings → Privacy & Security"

---

## 使用教程 / Tutorial

### 快速开始 / Quick Start

```
1. 拖入文件或文件夹    Drag files or folder
2. 点击「开始批量转换」  Click "Start Batch Convert"
3. 点击「保存 Markdown」 Click "Save Markdown"
4. 选择输出目录         Choose output directory
```

### 场景一：转换单个文件 / Convert Single File

```
步骤 Steps：
1. 拖入文件 → 文件出现在队列    Drag file → appears in queue
2. 点击「开始批量转换」          Click "Start Batch Convert"
3. 等待转换完成                  Wait for conversion
4. 点击「保存 Markdown 文件」    Click "Save Markdown"
5. 选择保存位置                  Choose save location
```

### 场景二：批量转换 / Batch Convert

```
步骤 Steps：
1. 拖入多个文件（或整个文件夹）  Drag multiple files (or entire folder)
2. 点击「开始批量转换」          Click "Start Batch Convert"
3. 等待所有文件转换完成          Wait for all files
4. 点击「保存 Markdown 文件」    Click "Save Markdown"
5. 选择保存目录                  Choose output directory
```

### 场景三：转换整个文件夹（推荐）/ Convert Entire Folder (Recommended)

拖入文件夹时，自动保持目录结构 / Auto-keep folder structure when dragging folder

```
输入 Input：
D:\文档\
├── 财务\报表.pdf
└── 技术\架构.docx

输出 Output（选择目录后）：
输出目录\
├── 财务\报表.md
└── 技术\架构.md
```

### 场景四：URL 转换 / URL Convert

```
步骤 Steps：
1. 复制网页链接                  Copy web URL
2. 粘贴到 URL 输入框             Paste into URL input
3. 点击「转换 URL」              Click "Convert URL"
4. 预览 Markdown 结果            Preview Markdown result
5. 点击「保存 Markdown 文件」    Click "Save Markdown"
```

### 切换语言 / Switch Language

菜单栏点击 **「中文 / EN」** 即可切换界面语言
Click **「中文 / EN」** in the menu bar to switch UI language

### 切换主题 / Switch Theme

按 `Ctrl+T` 或菜单 **「视图 → 切换主题」**
Press `Ctrl+T` or **View → Toggle Theme**

### 快捷键 / Shortcuts

| 快捷键 Shortcut | 功能 Function |
|--------|------|
| `Ctrl+O` | 打开文件 / Open file |
| `Ctrl+S` | 保存 Markdown / Save Markdown |
| `Ctrl+T` | 切换主题 / Toggle theme |

---

## 从源码构建 / Build from Source

### Windows

```bash
# 克隆仓库 / Clone repo
git clone https://github.com/your-username/markitdown-desktop.git
cd markitdown-desktop

# 安装依赖 / Install dependencies
pip install PySide6 markitdown[all] pyinstaller

# 构建 / Build
pyinstaller MarkItDown.spec --clean --noconfirm

# 输出 / Output
dist/MarkItDown/MarkItDown.exe
```

### macOS

```bash
# 克隆仓库 / Clone repo
git clone https://github.com/your-username/markitdown-desktop.git
cd markitdown-desktop

# 安装依赖 / Install dependencies
pip install PySide6 markitdown[all] pyinstaller

# 构建 / Build
pyinstaller MarkItDown-Mac.spec --clean --noconfirm

# 输出 / Output
dist/MarkItDown/MarkItDown
```

### 注意事项 / Build Notes

- `MarkItDown.spec` 中包含 magika 模型和配置文件的打包配置
- The spec includes magika model & config file bundling
- 如需重新打包，确保 Python 环境中已安装所有可选依赖
- Make sure all optional dependencies are installed before rebuilding

## 项目结构 / Project Structure

```
markitdown-desktop/
├── run.py                    # 入口脚本 / Entry point
├── MarkItDown.spec           # Windows 构建配置 / Windows build config
├── MarkItDown-Mac.spec       # macOS 构建配置 / macOS build config
├── app/
│   ├── __init__.py
│   ├── main_window.py        # 主窗口 / Main window
│   ├── theme.py              # 主题管理 / Theme manager (默认浅色 / Default light)
│   ├── workers.py            # 异步转换 / Async conversion worker
│   ├── i18n.py               # 国际化 / i18n (中英文 / Chinese & English)
│   ├── styles/
│   │   ├── __init__.py
│   │   └── themes.py         # QSS 样式 / QSS styles
│   └── widgets/
│       ├── __init__.py
│       ├── drop_zone.py      # 拖拽区域 / Drop zone
│       ├── file_list.py      # 文件队列 / File queue
│       ├── url_input.py      # URL 输入 / URL input
│       └── preview.py        # Markdown 预览 / Markdown preview
├── TUTORIAL.md               # 详细教程 / Detailed tutorial
├── .github/
│   └── workflows/
│       └── build.yml         # CI/CD 自动构建 / CI/CD auto build
└── .gitignore
```

## 技术栈 / Tech Stack

- **GUI 框架 Framework：** PySide6 (Qt for Python)
- **转换引擎 Engine：** [MarkItDown](https://github.com/microsoft/markitdown) by Microsoft
- **打包工具 Packaging：** PyInstaller
- **文件检测 Content Detection：** [Magika](https://github.com/google/magika) (ONNX model)
- **Python：** 3.10+

## 致谢 / Credits

- 本项目基于微软开源的 [MarkItDown](https://github.com/microsoft/markitdown) 库构建桌面 GUI
- Built with [MarkItDown](https://github.com/microsoft/markitdown) by Microsoft
- 文件类型检测使用 Google [Magika](https://github.com/google/magika)
- Content detection powered by Google [Magika](https://github.com/google/magika)

## License

MIT License

---

<div align="center">

**如果觉得有用，请给个 Star 支持一下！**
**If you find this useful, please give it a Star!**

</div>
