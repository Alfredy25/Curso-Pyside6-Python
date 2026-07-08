import sys
from PySide6.QtWidgets import QApplication
from course.alfredo.pyside.kardex.app.gui.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    # estilo fusion
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
