from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QSpinBox, QDoubleSpinBox
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # numero = QSpinBox(self)
        numero = QDoubleSpinBox()

        # numero.setMinimum(0)
        # numero.setMaximum(999)
        numero.setRange(0, 2000)
        numero.setSingleStep(2)
        numero.setPrefix("$")
        numero.setSuffix("%")
        numero.setValue(8)
        print(numero.value())

        numero.valueChanged.connect(self.valor_cambiado)

        self.setCentralWidget(numero)

    def valor_cambiado(self, numero):
        print("Valor cambiado: ", numero)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())