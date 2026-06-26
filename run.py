"""MarkItDown Desktop - Standalone Launcher"""
import sys
import os

if getattr(sys, 'frozen', False):
    _base = sys._MEIPASS
else:
    _base = os.path.dirname(os.path.abspath(__file__))
    _pkg = os.path.join(_base, '..', 'packages', 'markitdown', 'src')
    if os.path.isdir(_pkg):
        sys.path.insert(0, _pkg)

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFont

from app.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("MarkItDown")
    app.setOrganizationName("MarkItDown")

    font = QFont("Microsoft YaHei", 10)
    font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
    app.setFont(font)

    app.setStyle("Fusion")

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
