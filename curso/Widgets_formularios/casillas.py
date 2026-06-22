from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox
from PySide6.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        casilla = QCheckBox("Casilla de verificación")
        casilla.setCheckState(Qt.CheckState.PartiallyChecked)
        casilla.stateChanged.connect(self.estado_cambiado)
        # casilla.setChecked(True)
        # casilla.setEnabled(False) para desactivar la casilla para que no se pueda checkear
        print(f"esta Activa? {casilla.isChecked()}")
        print(f"es de tres estados? {casilla.isTristate()}")


        self.setCentralWidget(casilla)

    def estado_cambiado(self, estado):
        if Qt.CheckState(estado) == Qt.CheckState.Checked:
            print("Casilla marcada")
        if Qt.CheckState(estado) == Qt.CheckState.Unchecked:
            print("Casilla desmarcada")
        if Qt.CheckState(estado) == Qt.CheckState.PartiallyChecked:
            print("Casilla parcialmente marcada")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())