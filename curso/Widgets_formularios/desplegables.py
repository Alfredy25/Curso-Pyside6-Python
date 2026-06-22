from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox
from PySide6.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        desplegable = QComboBox()
        desplegable.addItems(["Opción 1", "Opcion 2", "Opcion 3"])
        desplegable.currentIndexChanged.connect(self.indice_cambiado)
        desplegable.currentTextChanged.connect(self.texto_cambiado)

        print("índice actual", desplegable.currentIndex())
        print("Texto actual", desplegable.currentText())
        self.setCentralWidget(desplegable)

    def indice_cambiado(self, indice):
        print("Nuevo índice", indice)
    def texto_cambiado(self, valor):
        print("Nuevo texto", valor)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())