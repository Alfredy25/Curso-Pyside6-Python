
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QStyle, QGridLayout)

import sys
import qtawesome as qta

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        icono = qta.icon("fa6.floppy-disk", color=('red', 100))
        boton = QPushButton(icono, "Boton")

        self.setCentralWidget(boton)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # estilo fusion
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())