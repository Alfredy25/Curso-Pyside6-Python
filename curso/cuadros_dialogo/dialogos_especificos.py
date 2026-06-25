import sys
from pathlib import Path
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QFileDialog, QInputDialog, QFontDialog,QColorDialog)
from PySide6.QtCore import QTranslator, QLibraryInfo

def absPath(file):
    ruta = Path(__file__).parent.parent.parent.absolute() / file
    print(ruta)
    return str(ruta)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)
        self.setWindowIcon(QIcon(absPath('extractor_ocr.png')))

        boton = QPushButton('Mostrar Dialogo')
        boton.clicked.connect(self.boton_clicado)

        self.setCentralWidget(boton)
        self.boton = boton


    def boton_clicado(self):
        # fichero, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", ".") # Abrir fichero
        # fichero, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", ".") # Guardar fichero
        # print(fichero)
        # valor, confirmacion = QInputDialog.getText(self, "Titulo", "Texto de introduce algo")
        # valor, confirmacion = QInputDialog.getInt(self, "Titulo", "Texto de introduce numero entero")
        # valor, confirmacion = QInputDialog.getDouble(self, "Titulo", "Texto numero decimal")
        # valor, confirmacion = QInputDialog.getItem(self, "Titulo", "Colores", ["Rojo","Azul","Blanco","Verde"],editable=False)
        # print(valor)
        # print(confirmacion)
        confirmado, fuente = QFontDialog.getFont(self)
        if confirmado:
            print(fuente)
            self.boton.setFont(fuente)
        color = QColorDialog.getColor()
        print(color)
        print(color.name())
        if color.isValid():
            self.boton.setStyleSheet(f"background-color: {color.name()}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())