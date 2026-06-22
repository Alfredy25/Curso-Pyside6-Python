from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QSpinBox
from PySide6.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        texto = QLineEdit()
        # texto.setMaxLength(10)
        texto.setPlaceholderText("Escribe máximo 10 caracteres")
        texto.textChanged.connect(self.texto_cambiado)
        texto.returnPressed.connect(self.enter_presionado)
        # texto.setText("Hola mundo") # Inserta un texto
        self.setCentralWidget(texto)

    def texto_cambiado(self, texto):
        print("Texto cambiado:", texto)

    def enter_presionado(self):
        texto = self.centralWidget().text()
        texto += "\n"
        self.centralWidget().setText(texto)
        print("Enter presionado, texto:", texto)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())