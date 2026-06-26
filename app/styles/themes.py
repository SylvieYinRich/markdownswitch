DARK_STYLE = """
QMainWindow {
    background-color: #1e1e2e;
}
QWidget {
    background-color: #1e1e2e;
    color: #cdd6f4;
    font-family: "Segoe UI", "Microsoft YaHei", "PingFang SC", sans-serif;
    font-size: 14px;
}
QLabel {
    color: #cdd6f4;
    font-size: 14px;
}
QLineEdit {
    background-color: #313244;
    border: 1px solid #45475a;
    border-radius: 6px;
    padding: 10px 14px;
    color: #cdd6f4;
    font-size: 14px;
    selection-background-color: #585b70;
}
QLineEdit:focus {
    border: 1px solid #89b4fa;
}
QPushButton {
    background-color: #89b4fa;
    color: #1e1e2e;
    border: none;
    border-radius: 6px;
    padding: 8px 20px;
    font-size: 14px;
    font-weight: bold;
    min-height: 24px;
}
QPushButton:hover {
    background-color: #74c7ec;
}
QPushButton:pressed {
    background-color: #89dceb;
}
QPushButton:disabled {
    background-color: #45475a;
    color: #6c7086;
}
QListWidget {
    background-color: #313244;
    border: 1px solid #45475a;
    border-radius: 6px;
    padding: 6px;
    outline: none;
    font-size: 13px;
}
QListWidget::item {
    padding: 10px;
    border-radius: 4px;
}
QListWidget::item:selected {
    background-color: #45475a;
}
QListWidget::item:hover {
    background-color: #3b3b52;
}
QProgressBar {
    background-color: #313244;
    border: 1px solid #45475a;
    border-radius: 6px;
    text-align: center;
    color: #cdd6f4;
    font-size: 12px;
    min-height: 22px;
}
QProgressBar::chunk {
    background-color: #89b4fa;
    border-radius: 5px;
}
QTextEdit, QPlainTextEdit {
    background-color: #313244;
    border: 1px solid #45475a;
    border-radius: 6px;
    padding: 10px;
    color: #cdd6f4;
    font-family: "Cascadia Code", "Consolas", "SF Mono", monospace;
    font-size: 13px;
}
QSplitter::handle {
    background-color: #45475a;
}
QSplitter::handle:horizontal {
    width: 4px;
}
QSplitter::handle:vertical {
    height: 4px;
}
QMenuBar {
    background-color: #181825;
    color: #cdd6f4;
    border-bottom: 1px solid #313244;
    font-size: 14px;
    padding: 2px;
}
QMenuBar::item {
    padding: 6px 12px;
    border-radius: 4px;
}
QMenuBar::item:selected {
    background-color: #45475a;
}
QMenu {
    background-color: #313244;
    border: 1px solid #45475a;
    border-radius: 6px;
    padding: 6px;
    font-size: 14px;
}
QMenu::item {
    padding: 8px 28px;
    border-radius: 4px;
}
QMenu::item:selected {
    background-color: #45475a;
}
QStatusBar {
    background-color: #181825;
    color: #a6adc8;
    border-top: 1px solid #313244;
    font-size: 13px;
}
QScrollBar:vertical {
    background-color: #1e1e2e;
    width: 12px;
    border-radius: 6px;
    margin: 2px;
}
QScrollBar::handle:vertical {
    background-color: #45475a;
    border-radius: 6px;
    min-height: 40px;
}
QScrollBar::handle:vertical:hover {
    background-color: #585b70;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}
QScrollBar:horizontal {
    background-color: #1e1e2e;
    height: 12px;
    border-radius: 6px;
    margin: 2px;
}
QScrollBar::handle:horizontal {
    background-color: #45475a;
    border-radius: 6px;
    min-width: 40px;
}
QScrollBar::handle:horizontal:hover {
    background-color: #585b70;
}
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0px;
}
QSpinBox {
    background-color: #313244;
    border: 1px solid #45475a;
    border-radius: 6px;
    padding: 8px;
    color: #cdd6f4;
    font-size: 14px;
}
QSpinBox:focus {
    border: 1px solid #89b4fa;
}
"""

LIGHT_STYLE = """
QMainWindow {
    background-color: #ffffff;
}
QWidget {
    background-color: #ffffff;
    color: #4c4f69;
    font-family: "Segoe UI", "Microsoft YaHei", "PingFang SC", sans-serif;
    font-size: 14px;
}
QLabel {
    color: #4c4f69;
    font-size: 14px;
}
QLineEdit {
    background-color: #eff1f5;
    border: 1px solid #ccd0da;
    border-radius: 6px;
    padding: 10px 14px;
    color: #4c4f69;
    font-size: 14px;
    selection-background-color: #bcc0cc;
}
QLineEdit:focus {
    border: 1px solid #1e66f5;
}
QPushButton {
    background-color: #1e66f5;
    color: #ffffff;
    border: none;
    border-radius: 6px;
    padding: 8px 20px;
    font-size: 14px;
    font-weight: bold;
    min-height: 24px;
}
QPushButton:hover {
    background-color: #2a7ae4;
}
QPushButton:pressed {
    background-color: #1a60d0;
}
QPushButton:disabled {
    background-color: #ccd0da;
    color: #9ca0b0;
}
QListWidget {
    background-color: #eff1f5;
    border: 1px solid #ccd0da;
    border-radius: 6px;
    padding: 6px;
    outline: none;
    font-size: 13px;
}
QListWidget::item {
    padding: 10px;
    border-radius: 4px;
}
QListWidget::item:selected {
    background-color: #ccd0da;
}
QListWidget::item:hover {
    background-color: #e6e9ef;
}
QProgressBar {
    background-color: #eff1f5;
    border: 1px solid #ccd0da;
    border-radius: 6px;
    text-align: center;
    color: #4c4f69;
    font-size: 12px;
    min-height: 22px;
}
QProgressBar::chunk {
    background-color: #1e66f5;
    border-radius: 5px;
}
QTextEdit, QPlainTextEdit {
    background-color: #eff1f5;
    border: 1px solid #ccd0da;
    border-radius: 6px;
    padding: 10px;
    color: #4c4f69;
    font-family: "Cascadia Code", "Consolas", "SF Mono", monospace;
    font-size: 13px;
}
QSplitter::handle {
    background-color: #ccd0da;
}
QSplitter::handle:horizontal {
    width: 4px;
}
QSplitter::handle:vertical {
    height: 4px;
}
QMenuBar {
    background-color: #ffffff;
    color: #4c4f69;
    border-bottom: 1px solid #ccd0da;
    font-size: 14px;
    padding: 2px;
}
QMenuBar::item {
    padding: 6px 12px;
    border-radius: 4px;
}
QMenuBar::item:selected {
    background-color: #ccd0da;
}
QMenu {
    background-color: #ffffff;
    border: 1px solid #ccd0da;
    border-radius: 6px;
    padding: 6px;
    font-size: 14px;
}
QMenu::item {
    padding: 8px 28px;
    border-radius: 4px;
}
QMenu::item:selected {
    background-color: #ccd0da;
}
QStatusBar {
    background-color: #ffffff;
    color: #8c8fa1;
    border-top: 1px solid #ccd0da;
    font-size: 13px;
}
QScrollBar:vertical {
    background-color: #ffffff;
    width: 12px;
    border-radius: 6px;
    margin: 2px;
}
QScrollBar::handle:vertical {
    background-color: #ccd0da;
    border-radius: 6px;
    min-height: 40px;
}
QScrollBar::handle:vertical:hover {
    background-color: #bcc0cc;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}
QScrollBar:horizontal {
    background-color: #ffffff;
    height: 12px;
    border-radius: 6px;
    margin: 2px;
}
QScrollBar::handle:horizontal {
    background-color: #ccd0da;
    border-radius: 6px;
    min-width: 40px;
}
QScrollBar::handle:horizontal:hover {
    background-color: #bcc0cc;
}
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0px;
}
QSpinBox {
    background-color: #eff1f5;
    border: 1px solid #ccd0da;
    border-radius: 6px;
    padding: 8px;
    color: #4c4f69;
    font-size: 14px;
}
QSpinBox:focus {
    border: 1px solid #1e66f5;
}
"""
