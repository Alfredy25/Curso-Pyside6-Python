import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLabel, QDialogButtonBox)

class Dialogo(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(240, 120)
        self.setWindowTitle('Hola')

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(QLabel('Dialogo de prueba'))
        layout.addWidget(QLabel('Dialogo de prueba2'))

        botones = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)

        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)

        botones.button(QDialogButtonBox.StandardButton.Ok).setText('Aceptar')
        botones.button(QDialogButtonBox.StandardButton.Cancel).setText('Cancelar')
        layout.addWidget(botones)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)

        boton = QPushButton('Mostrar Dialogo')
        boton.clicked.connect(self.boton_clicado)

        self.setCentralWidget(boton)

    def boton_clicado(self):
        dialogo = Dialogo()
        respuesta = dialogo.exec()
        if respuesta:
            print("Diálogo aceptado", respuesta)
        else:
            print("Dialogo denegado", respuesta)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())