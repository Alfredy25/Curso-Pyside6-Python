
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QStyle, QGridLayout, QFormLayout, QCheckBox, QRadioButton, QLabel,
    QLineEdit, QSpinBox, QPlainTextEdit, QVBoxLayout)

import sys
import qtawesome as qta

class EditorQSS(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.resize(480, 320)
        self.setWindowTitle("Editor QSS en vivo")

        self.editor = QPlainTextEdit()
        self.editor.setStyleSheet("""
            background-color: #212121;
            color: #e9e9e9;
            font-family: Consolas;
            font-size: 16px;
            """)
        self.editor.textChanged.connect(self.actualizar_estilos)
        layout = QVBoxLayout()
        layout.addWidget(self.editor)
        self.setLayout(layout)
        self.show()

    def actualizar_estilos(self):
        qss = self.editor.toPlainText()
        try:
            self.parent.setStyleSheet(qss)
        except:
            pass


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

        # self.setStyleSheet("""
        # QMainWindow {background-color: #212121}
        # QLabel {color: #e9e9e9}
        # QPushButton {
        #     background-color: orange;
        #     font-family: sans-serif;
        #     font-size: 14px;
        #     font-weight: bold;
        #     }
        # #etiqueta {
        #     background-color: cyan;
        #     color: black; padding: 10px;}
        # """)

        self.editorQSS = EditorQSS(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # estilo fusion
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())