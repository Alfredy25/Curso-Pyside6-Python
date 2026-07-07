
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QStyle, QGridLayout, QFormLayout, QCheckBox, QRadioButton, QLabel,
    QLineEdit, QSpinBox, QPlainTextEdit, QVBoxLayout)

import sys
import qtawesome as qta
from pathlib import Path


def absPath(file):
    ruta = Path(__file__).parent.absolute() / file
    print(ruta)
    return str(ruta)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        formulario = QFormLayout()

        formulario.addRow("CheckBox", QCheckBox())
        formulario.addRow("QRadioButton", QRadioButton())
        etiqueta = QLabel("QLabel")
        etiqueta.setObjectName("etiqueta")
        formulario.addRow("etiqueta", etiqueta)
        formulario.addRow("QLabel", QLabel("QLabel"))
        formulario.addRow("QPushButton", QPushButton("QPushButton"))
        formulario.addRow("Nombre", QLineEdit("Hector"))
        formulario.addRow("Edad", QSpinBox(value=32))

        widget = QWidget()
        widget.setLayout(formulario)
        self.setCentralWidget(widget)
        self.cargar_qss("qss/Aqua.qss")

    def cargar_qss(self, fichero):
        path = absPath(fichero)
        try:
            with open(path) as style:
                self.setStyleSheet(style.read())
        except FileNotFoundError:
            print("No se pudo cargar el fichero")
        except:
            print("Error abriendo los estilos")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    # estilo fusion
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())