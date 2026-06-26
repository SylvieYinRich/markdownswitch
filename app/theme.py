from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QPalette, QColor

from .styles.themes import DARK_STYLE, LIGHT_STYLE


class ThemeManager:
    DARK = "dark"
    LIGHT = "light"

    def __init__(self):
        self._current = self.LIGHT

    @property
    def current(self) -> str:
        return self._current

    @property
    def is_dark(self) -> bool:
        return self._current == self.DARK

    def apply(self, app: QApplication):
        app.setStyleSheet(DARK_STYLE if self._current == self.DARK else LIGHT_STYLE)

    def toggle(self, app: QApplication) -> str:
        self._current = self.LIGHT if self._current == self.DARK else self.DARK
        self.apply(app)
        return self._current
