"""Internationalization - Language strings"""
from typing import Dict

LANGUAGES: Dict[str, Dict[str, str]] = {
    "zh": {
        # Window
        "app_title": "MarkItDown - 文件转 Markdown 工具",
        # Menu
        "menu_file": "文件(&F)",
        "menu_open": "打开(&O)",
        "menu_save": "保存 Markdown(&S)",
        "menu_quit": "退出(&Q)",
        "menu_view": "视图(&V)",
        "menu_theme": "切换主题 (Ctrl+T)",
        "menu_language": "语言(&L)",
        "lang_zh": "中文",
        "lang_en": "English",
        # Drop zone
        "drop_hint": "拖拽文件或文件夹到此处",
        "drop_scanning": "正在扫描文件夹...",
        # URL input
        "url_placeholder": "输入 URL（支持 http/https 链接）",
        "url_convert": "转换 URL",
        # File list
        "file_queue": "文件队列 ({count})",
        "file_clear": "清空",
        "file_other": "... 及其他 {count} 个文件",
        # Buttons
        "btn_open": "打开文件",
        "btn_batch": "开始批量转换",
        "btn_cancel": "取消",
        "btn_save": "保存 Markdown 文件",
        "btn_workers": "并发数:",
        # Progress
        "progress_preparing": "准备中...",
        "progress_stats": "已完成: {done}/{total}  成功: {ok}  失败: {fail}",
        # Status
        "status_ready": "就绪 - 支持 PDF, Word, Excel, PPT, 图片, HTML, CSV, JSON, ZIP, EPUB 等格式",
        "status_files_added": "已添加 {count} 个文件",
        "status_converting_url": "正在转换: {url}",
        "status_convert_success": "转换成功: {title} - 点击「保存 Markdown 文件」按钮保存",
        "status_convert_fail": "转换失败: {error}",
        "status_batch_start": "正在批量转换 {count} 个文件 ({workers} 个并发线程)...",
        "status_batch_cancel": "已取消批量转换",
        "status_batch_done": "批量转换完成: 成功 {success} 个",
        "status_saved": "✓ 已保存: {path}",
        "status_saved_batch": "✓ 已保存 {count} 个文件",
        "status_theme_changed": "已切换主题: {name}",
        # Dialogs
        "dialog_convert_fail": "转换失败",
        "dialog_convert_fail_msg": "无法转换 URL:\n{error}",
        "dialog_batch_complete": "批量转换完成",
        "dialog_batch_result": "总计: {total} 个文件\n成功: {success}\n失败: {fail}",
        "dialog_save_title": "保存 Markdown 文件",
        "dialog_save_filter": "Markdown 文件 (*.md);;所有文件 (*)",
        "dialog_save_dir_title": "选择保存目录",
        "dialog_save_success": "保存成功",
        "dialog_save_success_msg": "Markdown 文件已保存到:\n{path}",
        "dialog_save_fail": "保存失败",
        "dialog_save_prompt": "请先转换文件或 URL",
        "dialog_batch_save_title": "批量保存完成",
        "dialog_batch_save_msg": "已保存 {count} 个 Markdown 文件到:\n{dir}",
        "dialog_batch_save_errors": "\n\n保存失败 {count} 个:\n{errors}",
        "dialog_quit_title": "确认退出",
        "dialog_quit_msg": "当前有任务正在执行，确定要退出吗？",
        "dialog_open_title": "选择文件",
        "dialog_open_filter": "支持的文件 ({exts});;所有文件 (*)",
        # File dialog
        "file_dialog_title": "选择文件",
        "file_dialog_dir": "选择保存目录",
    },
    "en": {
        # Window
        "app_title": "MarkItDown - File to Markdown Converter",
        # Menu
        "menu_file": "&File",
        "menu_open": "&Open",
        "menu_save": "Save &Markdown",
        "menu_quit": "&Quit",
        "menu_view": "&View",
        "menu_theme": "Toggle Theme (Ctrl+T)",
        "menu_language": "&Language",
        "lang_zh": "中文",
        "lang_en": "English",
        # Drop zone
        "drop_hint": "Drag files or folder here",
        "drop_scanning": "Scanning folder...",
        # URL input
        "url_placeholder": "Enter URL (http/https links supported)",
        "url_convert": "Convert URL",
        # File list
        "file_queue": "File Queue ({count})",
        "file_clear": "Clear",
        "file_other": "... and {count} more files",
        # Buttons
        "btn_open": "Open Files",
        "btn_batch": "Start Batch Convert",
        "btn_cancel": "Cancel",
        "btn_save": "Save Markdown",
        "btn_workers": "Threads:",
        # Progress
        "progress_preparing": "Preparing...",
        "progress_stats": "Done: {done}/{total}  OK: {ok}  Failed: {fail}",
        # Status
        "status_ready": "Ready - Supports PDF, Word, Excel, PPT, Images, HTML, CSV, JSON, ZIP, EPUB",
        "status_files_added": "Added {count} files",
        "status_converting_url": "Converting: {url}",
        "status_convert_success": "Convert OK: {title} - Click 'Save Markdown' to save",
        "status_convert_fail": "Convert failed: {error}",
        "status_batch_start": "Batch converting {count} files ({workers} threads)...",
        "status_batch_cancel": "Batch conversion cancelled",
        "status_batch_done": "Batch complete: {success} succeeded",
        "status_saved": "✓ Saved: {path}",
        "status_saved_batch": "✓ Saved {count} files",
        "status_theme_changed": "Theme: {name}",
        # Dialogs
        "dialog_convert_fail": "Conversion Failed",
        "dialog_convert_fail_msg": "Cannot convert URL:\n{error}",
        "dialog_batch_complete": "Batch Complete",
        "dialog_batch_result": "Total: {total} files\nSuccess: {success}\nFailed: {fail}",
        "dialog_save_title": "Save Markdown File",
        "dialog_save_filter": "Markdown files (*.md);;All files (*)",
        "dialog_save_dir_title": "Choose Output Directory",
        "dialog_save_success": "Saved",
        "dialog_save_success_msg": "Markdown file saved to:\n{path}",
        "dialog_save_fail": "Save Failed",
        "dialog_save_prompt": "Please convert a file or URL first",
        "dialog_batch_save_title": "Batch Save Complete",
        "dialog_batch_save_msg": "Saved {count} Markdown files to:\n{dir}",
        "dialog_batch_save_errors": "\n\n{count} files failed:\n{errors}",
        "dialog_quit_title": "Confirm Quit",
        "dialog_quit_msg": "Tasks are still running. Are you sure you want to quit?",
        "dialog_open_title": "Open Files",
        "dialog_open_filter": "Supported files ({exts});;All files (*)",
        # File dialog
        "file_dialog_title": "Open Files",
        "file_dialog_dir": "Choose Output Directory",
    },
}


class I18n:
    def __init__(self, lang: str = "zh"):
        self._lang = lang

    @property
    def lang(self) -> str:
        return self._lang

    @lang.setter
    def lang(self, value: str):
        if value in LANGUAGES:
            self._lang = value

    def t(self, key: str, **kwargs) -> str:
        text = LANGUAGES.get(self._lang, LANGUAGES["zh"]).get(key, key)
        if kwargs:
            text = text.format(**kwargs)
        return text

    def toggle(self) -> str:
        self._lang = "en" if self._lang == "zh" else "zh"
        return self._lang


_i18n = I18n("zh")


def t(key: str, **kwargs) -> str:
    return _i18n.t(key, **kwargs)


def set_lang(lang: str):
    _i18n.lang = lang


def get_lang() -> str:
    return _i18n.lang


def toggle_lang() -> str:
    return _i18n.toggle()
