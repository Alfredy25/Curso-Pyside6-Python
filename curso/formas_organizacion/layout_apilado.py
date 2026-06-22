from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QStackedLayout
from PySide6.QtCore import Qt
import sys


class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color: {color}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #          ancho,alto px
        self.resize(500, 400)

        layout = QStackedLayout()
        layout.addWidget(Caja("orange"))
        layout.addWidget(Caja("magenta"))
        layout.addWidget(Caja("purple"))
        layout.addWidget(Caja("red"))

        # Contenedor central
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        self.layout = layout

    def keyPressEvent(self, event):
        indice = self.layout.currentIndex()
        indice_maximo = self.layout.count() - 1
        print(indice)
        print(indice_maximo)
        if event.key() == Qt.Key.Key_Right:
            print("Flecha derecha presionada")
            indice += 1
        elif event.key() == Qt.Key.Key_Left:
            print("Flecha izquierda presionada")
            indice -= 1

        if indice > indice_maximo:
            indice = 0
        elif indice < 0:
            indice = indice_maximo

        self.layout.setCurrentIndex(indice)

        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())