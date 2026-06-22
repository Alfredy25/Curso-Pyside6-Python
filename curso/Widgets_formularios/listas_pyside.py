from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget
from PySide6.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.lista = QListWidget()
        self.lista.addItems(["Opción 1","Opcion 2","Opcion 3"])
        self.lista.currentItemChanged.connect(self.item_cambiado)

        print(self.lista.currentItem())
        self.setCentralWidget(self.lista)

    def item_cambiado(self, item):
        print("Nuevo item",item.text())
        print(self.lista.currentItem().text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())