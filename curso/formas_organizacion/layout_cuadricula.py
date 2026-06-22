from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QGridLayout
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

        layout_cuadricula = QGridLayout()
        #                                         fila, columna
        layout_cuadricula.addWidget(Caja("orange"), 0, 0)
        layout_cuadricula.addWidget(Caja("purple"), 1, 1)
        layout_cuadricula.addWidget(Caja("magenta"), 2, 2)
        layout_cuadricula.addWidget(Caja("gray"), 2, 0)
        layout_cuadricula.addWidget(Caja("red"), 0, 2)
        layout_cuadricula.addWidget(Caja("cyan"), 0, 1)


        # Contenedor central
        widget = QWidget()
        widget.setLayout(layout_cuadricula)

        self.setCentralWidget(widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())