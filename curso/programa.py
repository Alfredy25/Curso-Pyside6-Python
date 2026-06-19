from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow
# from PySide6.QtCore import QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Madre")
        # self.setMinimumSize(QSize(480, 320))
        #                         ancho, alto
        # self.setMaximumSize(QSize(200, 800))
        # self.setFixedSize(QSize(600, 400))
        self.resize(800, 600)

        # Creamos un botón
        boton = QPushButton("Soy un botón")
        # boton.clicked.connect(self.boton_clicado)
        # boton.pressed.connect(self.boton_pulsado)
        # boton.released.connect(self.boton_liberado)
        boton.setCheckable(True)
        boton.clicked.connect(self.boton_alternado)
        self.setCentralWidget(boton)
        self.boton = boton

    def boton_alternado(self, valor):
        if valor:
            self.boton.setText("Estoy activado")
        else:
            self.boton.setText("Estoy deactivado")

    # def boton_clicado(self):
    #     print("Botón clicado")
    #
    # def boton_pulsado(self):
    #     print("Botón pulsado")
    #
    # def boton_liberado(self):
    #     print("Botón liberado")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


