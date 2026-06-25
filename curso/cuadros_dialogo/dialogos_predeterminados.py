import sys
from pathlib import Path
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QMessageBox)
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

    def boton_clicado(self):
        # QMessageBox().about(self, "Acerca de", "Esto es un acerca de")
        # dial = QMessageBox().critical(self, "Error", "Ha ocurrido algo malo")
        # dial = QMessageBox().information(self, "Informacion", "Esto es un texto infomativo")
        dial = QMessageBox().warning(self,
                                     "Aviso",
                                     "Cuidado vas hacer algo importante",
                                     buttons= QMessageBox.StandardButton.Apply | QMessageBox.StandardButton.Cancel)
        if dial == QMessageBox.StandardButton.Apply:
            print("Aplicando cambios")
        else:
            print("no se hace nada")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    traductor = QTranslator(app)
    traducciones = QLibraryInfo.location(QLibraryInfo.LibraryPath.TranslationsPath)
    traductor.load("qt_es", traducciones)
    app.installTranslator(traductor)
    print(traducciones)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())