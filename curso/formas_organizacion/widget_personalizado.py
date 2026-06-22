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
        layout = QVBoxLayout()
        # layout = QHBoxLayout()
        layout.addWidget(Caja("green"))
        layout.addWidget(Caja("blue"))
        layout.addWidget(Caja("red"))
        #                      (left, top, right, bottom)
        layout.setContentsMargins(10,50,20,15)
        #              20 px entre cada caja
        layout.setSpacing(20)

        # Contenedor central
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())