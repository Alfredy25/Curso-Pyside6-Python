import random
import sys


from PySide6.QtGui import QIcon, QAction
from pathlib import Path
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QStatusBar, QToolBar, QLabel, QDockWidget, \
    QVBoxLayout, QWidget, QPushButton
from PySide6.QtCore import Qt
import random

def absPath(file):
    return str(Path(__file__).parent.parent.absolute() / file)

class Subventana(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(240, 120)
        self.setWindowTitle("Subventana")

        etiqueta = QLabel(f"Soy una subventana.. {random.randint(0,100)}")
        layout = QVBoxLayout()
        layout.addWidget(etiqueta)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana principal")
        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.subventana = Subventana()

        # Boton para abrir la subventana
        boton_mostrar = QPushButton("Mostrar subventana")
        boton_mostrar.clicked.connect(self.subventana.show)
        layout.addWidget(boton_mostrar)

        boton_ocultar = QPushButton("ocultar subventana")
        boton_ocultar.clicked.connect(self.subventana.hide)
        layout.addWidget(boton_ocultar)

    # def ocultar_subventana(self):
    #     if self.subventana and self.subventana.isVisible():
    #         self.subventana.hide()
    #
    # def mostrar_subventana(self):
    #     if not self.subventana:
    #         self.subventana = Subventana()
    #     self.subventana.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())