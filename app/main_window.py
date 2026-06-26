from __future__ import annotations

import os
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence, QAction, QFont
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QFontComboBox,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMenu,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QSpinBox,
    QSplitter,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)

from .i18n import t, set_lang, get_lang, LANGUAGES
from .theme import ThemeManager
from .workers import ConversionRunner, BatchConversionRunner, ConversionResult
from .widgets.drop_zone import DropZone, SUPPORTED_EXTENSIONS
from .widgets.file_list import FileListWidget
from .widgets.url_input import UrlInput
from .widgets.preview import MarkdownPreview


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._theme = ThemeManager()
        self._single_runner = ConversionRunner()
        self._batch_runner = BatchConversionRunner(max_workers=4)
        self._current_markdown = ""
        self._batch_results: list[ConversionResult] = []

        self._setup_ui()
        self._setup_menu()
        self._setup_connections()
        self._retranslate()

        self._theme.apply(QApplication.instance())

    def _setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.setSpacing(12)

        top_splitter = QSplitter(Qt.Orientation.Vertical)

        top_widget = QWidget()
        top_layout = QVBoxLayout(top_widget)
        top_layout.setContentsMargins(0, 0, 0, 0)
        top_layout.setSpacing(10)

        self._drop_zone = DropZone()

        input_row = QHBoxLayout()
        input_row.setSpacing(10)
        self._url_input = UrlInput()
        self._open_btn = QPushButton()
        self._open_btn.setMinimumWidth(120)
        self._open_btn.clicked.connect(self._open_file_dialog)
        input_row.addWidget(self._url_input, 1)
        input_row.addWidget(self._open_btn)

        self._file_list = FileListWidget()

        btn_row = QHBoxLayout()
        btn_row.setSpacing(10)
        self._batch_btn = QPushButton()
        self._batch_btn.setMinimumWidth(140)
        self._batch_btn.setEnabled(False)
        self._batch_btn.clicked.connect(self._start_batch)

        self._cancel_btn = QPushButton()
        self._cancel_btn.setMinimumWidth(80)
        self._cancel_btn.setEnabled(False)
        self._cancel_btn.clicked.connect(self._cancel_batch)

        self._save_btn = QPushButton()
        self._save_btn.setMinimumWidth(180)
        self._save_btn.setEnabled(False)
        self._save_btn.clicked.connect(self._save_markdown)

        worker_label = QLabel()
        self._worker_spin = QSpinBox()
        self._worker_spin.setRange(1, 16)
        self._worker_spin.setValue(4)
        self._worker_spin.setFixedWidth(60)
        self._worker_spin.valueChanged.connect(self._on_workers_changed)

        btn_row.addWidget(self._batch_btn)
        btn_row.addWidget(self._cancel_btn)
        btn_row.addWidget(worker_label)
        btn_row.addWidget(self._worker_spin)
        btn_row.addStretch()
        btn_row.addWidget(self._save_btn)

        self._progress = QProgressBar()
        self._progress.setVisible(False)
        self._progress.setTextVisible(True)

        self._stats_label = QLabel("")
        self._stats_label.setVisible(False)

        top_layout.addWidget(self._drop_zone)
        top_layout.addLayout(input_row)
        top_layout.addWidget(self._file_list)
        top_layout.addLayout(btn_row)
        top_layout.addWidget(self._progress)
        top_layout.addWidget(self._stats_label)

        self._preview = MarkdownPreview()

        top_splitter.addWidget(top_widget)
        top_splitter.addWidget(self._preview)
        top_splitter.setSizes([400, 500])

        main_layout.addWidget(top_splitter)

        self._status = QStatusBar()
        self.setStatusBar(self._status)

    def _setup_menu(self):
        menubar = self.menuBar()

        self._file_menu = menubar.addMenu("")
        self._open_action = QAction("", self)
        self._open_action.setShortcut(QKeySequence.StandardKey.Open)
        self._open_action.triggered.connect(self._open_file_dialog)
        self._file_menu.addAction(self._open_action)

        self._save_action = QAction("", self)
        self._save_action.setShortcut(QKeySequence.StandardKey.SaveAs)
        self._save_action.triggered.connect(self._save_markdown)
        self._save_action.setEnabled(False)
        self._file_menu.addAction(self._save_action)

        self._file_menu.addSeparator()

        self._quit_action = QAction("", self)
        self._quit_action.setShortcut(QKeySequence.StandardKey.Quit)
        self._quit_action.triggered.connect(self.close)
        self._file_menu.addAction(self._quit_action)

        self._view_menu = menubar.addMenu("")
        self._toggle_theme = QAction("", self)
        self._toggle_theme.setShortcut(QKeySequence("Ctrl+T"))
        self._toggle_theme.triggered.connect(self._on_toggle_theme)
        self._view_menu.addAction(self._toggle_theme)

        self._lang_menu = menubar.addMenu("中文 / EN")
        self._lang_actions = {}
        for code, name in [("zh", "中文"), ("en", "English")]:
            action = QAction(name, self)
            action.setCheckable(True)
            action.triggered.connect(lambda checked, c=code: self._switch_lang(c))
            self._lang_menu.addAction(action)
            self._lang_actions[code] = action

    def _setup_connections(self):
        self._drop_zone.files_dropped.connect(self._on_files_added)
        self._file_list.files_changed.connect(self._on_files_changed)
        self._url_input.convert_requested.connect(self._on_url_convert)

        self._single_runner.result_ready.connect(self._on_single_result)
        self._batch_runner.finished_all.connect(self._on_batch_done)

    def _retranslate(self):
        self.setWindowTitle(t("app_title"))
        self._file_menu.setTitle(t("menu_file"))
        self._open_action.setText(t("menu_open"))
        self._save_action.setText(t("menu_save"))
        self._quit_action.setText(t("menu_quit"))
        self._view_menu.setTitle(t("menu_view"))
        self._toggle_theme.setText(t("menu_theme"))

        current_lang = get_lang()
        for code, action in self._lang_actions.items():
            action.setChecked(code == current_lang)

        self._open_btn.setText(t("btn_open"))
        self._batch_btn.setText(t("btn_batch"))
        self._cancel_btn.setText(t("btn_cancel"))
        self._save_btn.setText(t("btn_save"))

        worker_label = self._worker_spin.parent().findChild(QLabel)
        if worker_label:
            worker_label.setText(t("btn_workers"))

        self._drop_zone.retranslate()
        self._url_input.retranslate()
        self._file_list.retranslate()
        self._status.showMessage(t("status_ready"))

    def _switch_lang(self, lang: str):
        set_lang(lang)
        self._retranslate()

    def _on_files_added(self, paths: list[str], base_dir: str = ""):
        self._file_list.add_files(paths, base_dir)
        self._status.showMessage(t("status_files_added", count=len(paths)))

    def _on_files_changed(self, count: int):
        if not self._batch_runner.is_running:
            self._batch_btn.setEnabled(count > 0)
        if count == 0 and not self._current_markdown:
            self._preview.clear()
            self._save_action.setEnabled(False)
            self._save_btn.setEnabled(False)

    def _on_workers_changed(self, value: int):
        self._batch_runner._max_workers = value

    def _on_url_convert(self, url: str):
        if self._single_runner.is_running:
            return
        self._url_input.set_enabled(False)
        self._status.showMessage(t("status_converting_url", url=url))
        self._single_runner.convert(url, is_url=True)

    def _on_single_result(self, result: ConversionResult):
        self._url_input.set_enabled(True)
        if result.success:
            self._current_markdown = result.markdown
            self._preview.set_markdown(result.markdown)
            self._save_action.setEnabled(True)
            self._save_btn.setEnabled(True)
            title = result.title or Path(result.source).name
            self._status.showMessage(t("status_convert_success", title=title))
        else:
            self._status.showMessage(t("status_convert_fail", error=result.error))
            QMessageBox.warning(self, t("dialog_convert_fail"), t("dialog_convert_fail_msg", error=result.error))

    def _open_file_dialog(self):
        exts = " ".join(f"*{e}" for e in sorted(SUPPORTED_EXTENSIONS))
        paths, _ = QFileDialog.getOpenFileNames(
            self,
            t("dialog_open_title"),
            "",
            t("dialog_open_filter", exts=exts),
        )
        if paths:
            base_dir = str(Path(paths[0]).parent)
            self._on_files_added(paths, base_dir)

    def _start_batch(self):
        paths = self._file_list.get_all_paths()
        if not paths or self._batch_runner.is_running:
            return

        self._progress.setVisible(True)
        self._progress.setMaximum(len(paths))
        self._progress.setValue(0)
        self._stats_label.setVisible(True)
        self._stats_label.setText(t("progress_preparing"))
        self._batch_btn.setEnabled(False)
        self._cancel_btn.setEnabled(True)
        self._drop_zone.setEnabled(False)
        self._url_input.set_enabled(False)
        self._worker_spin.setEnabled(False)

        workers = self._worker_spin.value()
        self._status.showMessage(t("status_batch_start", count=len(paths), workers=workers))

        for p in paths:
            self._file_list.set_item_pending(p)

        self._batch_runner._max_workers = workers
        self._batch_runner.convert_all(paths)

    def _cancel_batch(self):
        if self._batch_runner.is_running:
            self._batch_runner.cancel()
            self._status.showMessage(t("status_batch_cancel"))

    def _on_stats_updated(self, success: int, fail: int, total: int):
        self._stats_label.setText(t("progress_stats", done=success+fail, total=total, ok=success, fail=fail))

    def _on_batch_progress(self, current: int, total: int, result: ConversionResult):
        self._progress.setValue(current)
        if result.success:
            self._file_list.set_item_success(result.source)
        else:
            self._file_list.set_item_error(result.source)

    def _on_batch_done(self, results: list[ConversionResult]):
        self._batch_btn.setEnabled(True)
        self._cancel_btn.setEnabled(False)
        self._drop_zone.setEnabled(True)
        self._url_input.set_enabled(True)
        self._worker_spin.setEnabled(True)
        self._progress.setVisible(False)
        self._stats_label.setVisible(False)

        self._batch_results = [r for r in results if r.success]
        success = len(self._batch_results)
        fail = len(results) - success

        self._status.showMessage(t("status_batch_done", success=success))

        if success > 0:
            self._save_btn.setEnabled(True)
            self._save_action.setEnabled(True)

        QMessageBox.information(
            self,
            t("dialog_batch_complete"),
            t("dialog_batch_result", total=len(results), success=success, fail=fail),
        )

    def _save_markdown(self):
        if self._batch_results:
            self._save_batch()
        elif self._current_markdown:
            self._save_single()
        else:
            QMessageBox.information(self, t("dialog_save_title"), t("dialog_save_prompt"))

    def _save_single(self):
        path, _ = QFileDialog.getSaveFileName(
            self,
            t("dialog_save_title"),
            "",
            t("dialog_save_filter"),
        )
        if path:
            try:
                Path(path).write_text(self._current_markdown, encoding="utf-8")
                self._status.showMessage(t("status_saved", path=path))
                QMessageBox.information(self, t("dialog_save_success"), t("dialog_save_success_msg", path=path))
            except Exception as e:
                QMessageBox.warning(self, t("dialog_save_fail"), str(e))

    def _save_batch(self):
        dir_path = QFileDialog.getExistingDirectory(
            self,
            t("dialog_save_dir_title"),
        )
        if not dir_path:
            return

        saved = 0
        errors = []
        for result in self._batch_results:
            try:
                rel_path = self._file_list.get_relative_path(result.source)
                out_stem = Path(rel_path).stem
                out_dir = Path(dir_path) / Path(rel_path).parent
                out_dir.mkdir(parents=True, exist_ok=True)
                out_path = out_dir / (out_stem + ".md")
                out_path.write_text(result.markdown, encoding="utf-8")
                saved += 1
            except Exception as e:
                errors.append(f"{Path(result.source).name}: {e}")

        msg = t("dialog_batch_save_msg", count=saved, dir=dir_path)
        if errors:
            msg += t("dialog_batch_save_errors", count=len(errors), errors="\n".join(errors[:5]))
        self._status.showMessage(t("status_saved_batch", count=saved))
        QMessageBox.information(self, t("dialog_batch_save_title"), msg)
        self._batch_results = []

    def _on_toggle_theme(self):
        self._theme.toggle(QApplication.instance())
        name = "Dark" if self._theme.is_dark else "Light"
        if get_lang() == "zh":
            name = "深色" if self._theme.is_dark else "浅色"
        self._status.showMessage(t("status_theme_changed", name=name))

    def closeEvent(self, event):
        if self._batch_runner.is_running or self._single_runner.is_running:
            reply = QMessageBox.question(
                self,
                t("dialog_quit_title"),
                t("dialog_quit_msg"),
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No,
            )
            if reply == QMessageBox.StandardButton.No:
                event.ignore()
                return
            self._batch_runner.cancel()
            self._single_runner.cancel()
        event.accept()
