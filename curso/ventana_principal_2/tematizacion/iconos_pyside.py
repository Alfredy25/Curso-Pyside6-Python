import sys
from PySide6.QtGui import QPalette, QColor
from pathlib import Path
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QStyle


def absPath(file):
    return str(Path(__file__).parent.parent.absolute() / file)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana principal")
        icono = self.style().standardIcon(QStyle.StandardPixmap.SP_DialogSaveButton)
        boton = QPushButton(icono, "Botón guardar")
        self.setCentralWidget(boton)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())