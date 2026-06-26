from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QHBoxLayout, QLineEdit, QPushButton, QWidget

from ..i18n import t


class UrlInput(QWidget):
    convert_requested = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)

        self._input = QLineEdit()
        self._input.setPlaceholderText(t("url_placeholder"))
        self._input.returnPressed.connect(self._on_convert)

        self._btn = QPushButton(t("url_convert"))
        self._btn.setMinimumWidth(100)
        self._btn.clicked.connect(self._on_convert)

        layout.addWidget(self._input, 1)
        layout.addWidget(self._btn)

    def retranslate(self):
        self._input.setPlaceholderText(t("url_placeholder"))
        self._btn.setText(t("url_convert"))

    def _on_convert(self):
        url = self._input.text().strip()
        if url:
            self.convert_requested.emit(url)

    def set_enabled(self, enabled: bool):
        self._input.setEnabled(enabled)
        self._btn.setEnabled(enabled)
