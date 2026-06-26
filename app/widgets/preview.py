from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QPlainTextEdit,
    QSplitter,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from ..i18n import t


class MarkdownPreview(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        splitter = QSplitter(Qt.Orientation.Horizontal)

        self._rendered = QTextEdit()
        self._rendered.setReadOnly(True)
        self._rendered.setPlaceholderText("Markdown Preview...")

        self._source = QPlainTextEdit()
        self._source.setReadOnly(True)
        self._source.setPlaceholderText("Markdown Source...")

        splitter.addWidget(self._rendered)
        splitter.addWidget(self._source)
        splitter.setSizes([500, 500])

        layout.addWidget(splitter)

        self._current_md = ""

    def set_markdown(self, text: str):
        self._current_md = text
        self._rendered.setMarkdown(text)
        self._source.setPlainText(text)

    def clear(self):
        self._current_md = ""
        self._rendered.clear()
        self._source.clear()

    def get_markdown(self) -> str:
        return self._current_md

    def set_rendered_font_size(self, size: int):
        self._rendered.zoomIn(size - 12)

    def set_source_font_size(self, size: int):
        self._source.zoomIn(size - 12)
