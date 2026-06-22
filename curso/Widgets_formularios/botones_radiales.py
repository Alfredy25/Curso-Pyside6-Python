from PySide6.QtWidgets import QApplication, QMainWindow, QRadioButton
from PySide6.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        radial = QRadioButton("Botón radial")
        radial.toggled.connect(self.estado_cambiado)
        radial.setChecked(True)

        print("Radial activado? ", radial.isChecked())

        self.setCentralWidget(radial)

    def estado_cambiado(self, estado):
        if estado:
            print(f"Radial marcado {estado}")
        else:
            print("Radial desmarcado")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())