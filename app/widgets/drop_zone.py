from __future__ import annotations

import os
from pathlib import Path

from PySide6.QtCore import Qt, Signal, QThread, QObject
from PySide6.QtGui import QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from ..i18n import t

SUPPORTED_EXTENSIONS = {
    ".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx",
    ".csv", ".json", ".xml", ".html", ".htm", ".txt", ".md", ".rst",
    ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".webp",
    ".mp3", ".wav", ".flac", ".ogg", ".m4a", ".wma", ".mp4",
    ".zip", ".epub", ".rtf", ".msg", ".ipynb",
}


class _FolderScanner(QObject):
    done = Signal(list, str)

    def __init__(self, folder: str):
        super().__init__()
        self._folder = folder

    def run(self):
        paths = []
        base = self._folder
        for f in Path(base).rglob("*"):
            if f.is_file() and f.suffix.lower() in SUPPORTED_EXTENSIONS:
                paths.append(str(f))
        self.done.emit(paths, base)


class DropZone(QWidget):
    files_dropped = Signal(list, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setMinimumHeight(120)
        self.setMaximumHeight(160)
        self._scanner: QThread | None = None

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._icon_label = QLabel("\u2b07")
        self._icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._icon_label.setStyleSheet("font-size: 32px; border: none;")

        self._text_label = QLabel(t("drop_hint"))
        self._text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._text_label.setStyleSheet("font-size: 14px; border: none; color: #a6adc8;")

        self._status_label = QLabel("")
        self._status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._status_label.setStyleSheet("font-size: 12px; border: none; color: #f9e2af;")
        self._status_label.setVisible(False)

        layout.addWidget(self._icon_label)
        layout.addWidget(self._text_label)
        layout.addWidget(self._status_label)

        self._set_default_style()

    def retranslate(self):
        self._text_label.setText(t("drop_hint"))

    def _set_default_style(self):
        self.setStyleSheet(
            "DropZone { background-color: #313244; border: 2px dashed #585b70; border-radius: 12px; }"
        )

    def _set_hover_style(self):
        self.setStyleSheet(
            "DropZone { background-color: #45475a; border: 2px dashed #89b4fa; border-radius: 12px; }"
        )

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            self._set_hover_style()
        else:
            event.ignore()

    def dragLeaveEvent(self, event):
        self._set_default_style()

    def dropEvent(self, event: QDropEvent):
        self._set_default_style()
        urls = event.mimeData().urls()
        if not urls:
            return

        has_dirs = any(Path(url.toLocalFile()).is_dir() for url in urls)

        if has_dirs:
            for url in urls:
                path = url.toLocalFile()
                if Path(path).is_dir():
                    self._scan_folder(path)
        else:
            paths = [url.toLocalFile() for url in urls if Path(url.toLocalFile()).is_file()]
            if paths:
                base_dir = str(Path(paths[0]).parent)
                self.files_dropped.emit(paths, base_dir)

    def _scan_folder(self, folder: str):
        self._text_label.setText(t("drop_scanning"))
        self._status_label.setText("")
        self._status_label.setVisible(True)
        self.setEnabled(False)

        self._worker = _FolderScanner(folder)
        self._scanner = QThread()
        self._worker.moveToThread(self._scanner)
        self._scanner.started.connect(self._worker.run)
        self._worker.done.connect(self._on_scan_done)
        self._worker.done.connect(self._scanner.quit)
        self._scanner.start()

    def _on_scan_done(self, paths: list[str], base_dir: str):
        self._text_label.setText(t("drop_hint"))
        self._status_label.setVisible(False)
        self.setEnabled(True)
        if paths:
            self.files_dropped.emit(paths, base_dir)
