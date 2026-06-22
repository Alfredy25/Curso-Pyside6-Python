from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QFormLayout, QLineEdit, QHBoxLayout
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

        layout_form = QFormLayout()
        layout_form.addRow("Naranja", Caja("orange"))
        layout_form.addRow("Morado", Caja("purple"))
        layout_form.addRow("Magenta", Caja("magenta"))
        layout_form.addRow("Gris", Caja("gray"))
        layout_form.addRow("Rojo", Caja("red"))

        layout_form.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        layout_form.setFormAlignment(Qt.AlignmentFlag.AlignCenter)

        # Contenedor central
        widget = QWidget()
        widget.setLayout(layout_form)

        self.setCentralWidget(widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())