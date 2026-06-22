from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout
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

        # Layouts
        layout_hor = QHBoxLayout()
        layout_ver1 = QVBoxLayout()
        layout_ver2 = QVBoxLayout()

        layout_hor2 = QHBoxLayout()
        layout_hor2.addWidget(Caja("yellow"))

        layout_hor.addWidget(Caja("green"))
        layout_hor.addLayout(layout_ver1)
        layout_hor.addLayout(layout_ver2)

        layout_ver1.addLayout(layout_hor2)
        layout_ver1.addWidget(Caja("blue"))
        layout_ver1.addWidget(Caja("red"))

        layout_ver2.addWidget(Caja("orange"))
        layout_ver2.addWidget(Caja("magenta"))
        layout_ver2.addWidget(Caja("purple"))

        layout_hor2.addWidget(Caja("red"))


        # Contenedor central
        widget = QWidget()
        widget.setLayout(layout_hor)

        self.setCentralWidget(widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())