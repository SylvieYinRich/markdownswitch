from __future__ import annotations

import os
from pathlib import Path

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from ..i18n import t

STATUS_ICONS = {
    "pending": "\u23f3",
    "success": "\u2713",
    "error": "\u2717",
    "idle": "\u25cb",
}

SHOW_ITEMS_LIMIT = 500


class FileListWidget(QWidget):
    files_changed = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._paths: list[str] = []
        self._status_map: dict[str, str] = {}
        self._base_dir = ""
        self._hidden_count = 0

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(4)

        header = QHBoxLayout()
        self._count_label = QLabel(t("file_queue", count=0))
        self._count_label.setStyleSheet("font-weight: bold; border: none;")
        self._clear_btn = QPushButton(t("file_clear"))
        self._clear_btn.setFixedHeight(32)
        self._clear_btn.setStyleSheet("QPushButton { padding: 6px 12px; font-size: 13px; min-width: 60px; }")
        self._clear_btn.clicked.connect(self.clear_all)
        header.addWidget(self._count_label)
        header.addStretch()
        header.addWidget(self._clear_btn)

        self._list = QListWidget()
        self._list.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        layout.addLayout(header)
        layout.addWidget(self._list)

    def retranslate(self):
        self._count_label.setText(t("file_queue", count=len(self._paths)))
        self._clear_btn.setText(t("file_clear"))
        self._rebuild_list()

    def add_files(self, paths: list[str], base_dir: str = ""):
        if base_dir:
            self._base_dir = base_dir

        self._list.setUpdatesEnabled(False)
        self._list.blockSignals(True)

        for p in paths:
            norm = os.path.normpath(p)
            if norm not in self._status_map:
                self._paths.append(norm)
                self._status_map[norm] = "idle"

        self._rebuild_list()

        self._list.blockSignals(False)
        self._list.setUpdatesEnabled(True)
        self._update_count()

    def _rebuild_list(self):
        self._list.clear()
        total = len(self._paths)

        if total <= SHOW_ITEMS_LIMIT:
            for path in self._paths:
                self._add_list_item(path)
            self._hidden_count = 0
        else:
            for path in self._paths[:SHOW_ITEMS_LIMIT]:
                self._add_list_item(path)
            self._hidden_count = total - SHOW_ITEMS_LIMIT
            hint_item = QListWidgetItem(t("file_other", count=self._hidden_count))
            hint_item.setFlags(hint_item.flags() & ~Qt.ItemFlag.ItemIsSelectable)
            self._list.addItem(hint_item)

    def _add_list_item(self, path: str):
        status = self._status_map.get(path, "idle")
        icon = STATUS_ICONS.get(status, "\u25cb")

        name = Path(path).name
        if len(name) > 50:
            name = name[:47] + "..."

        display = f"{icon}  {name}"
        item = QListWidgetItem(display)
        item.setData(Qt.ItemDataRole.UserRole, path)
        item.setToolTip(path)
        self._list.addItem(item)

    def get_all_paths(self) -> list[str]:
        return list(self._paths)

    def get_base_dir(self) -> str:
        return self._base_dir

    def get_relative_path(self, filepath: str) -> str:
        norm = os.path.normpath(filepath)
        if self._base_dir and norm.startswith(os.path.normpath(self._base_dir)):
            return os.path.relpath(norm, self._base_dir)
        return Path(norm).name

    def set_item_status(self, path: str, status: str):
        norm = os.path.normpath(path)
        if norm in self._status_map:
            self._status_map[norm] = status
            self._update_item_display(norm)
        else:
            for key in self._status_map:
                if Path(key).name == Path(norm).name:
                    self._status_map[key] = status
                    self._update_item_display(key)
                    break

    def set_item_pending(self, path: str):
        self.set_item_status(path, "pending")

    def set_item_success(self, path: str):
        self.set_item_status(path, "success")

    def set_item_error(self, path: str):
        self.set_item_status(path, "error")

    def _update_item_display(self, path: str):
        status = self._status_map.get(path, "idle")
        icon = STATUS_ICONS.get(status, "\u25cb")

        for i in range(self._list.count()):
            item = self._list.item(i)
            item_path = item.data(Qt.ItemDataRole.UserRole)
            if item_path and Path(item_path).name == Path(path).name:
                name = Path(path).name
                if len(name) > 50:
                    name = name[:47] + "..."
                item.setText(f"{icon}  {name}")
                break

    def clear_all(self):
        self._list.clear()
        self._paths.clear()
        self._status_map.clear()
        self._hidden_count = 0
        self._update_count()

    def _update_count(self):
        count = len(self._paths)
        self._count_label.setText(t("file_queue", count=count))
        self.files_changed.emit(count)
