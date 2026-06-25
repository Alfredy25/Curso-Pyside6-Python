import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QMessageBox)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)

        boton = QPushButton('Mostrar Dialogo')
        boton.clicked.connect(self.boton_clicado)

        self.setCentralWidget(boton)

    def boton_clicado(self):
        dialogo = QMessageBox(self)
        dialogo.setWindowTitle('Titulo de ejemplo')
        dialogo.setText('Esto es un dialogo de prueba')
        dialogo.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        dialogo.button(QMessageBox.StandardButton.Ok).setText('Aceptar')
        dialogo.button(QMessageBox.StandardButton.Cancel).setText('Cancelar')
        dialogo.setIcon(QMessageBox.Icon.Information)
        respuesta = dialogo.exec()
        if respuesta == QMessageBox.StandardButton.Ok:
            print('Dialogo aceptado')
        else:
            print('Dialogo denegado')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())