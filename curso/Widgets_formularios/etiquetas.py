from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtCore import Qt
import sys
from pathlib import Path

def absPath(file):
    return str(Path(__file__).parent.absolute() / file)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)

        # Etiqueta
        etiqueta = QLabel("Soy una etiqueta")
        # fuente = etiqueta.font()
        # fuente.setPointSize(24)
        # etiqueta.setFont(fuente)
        fuente = QFont("Comic Sans MS", 24)
        etiqueta.setFont(fuente)
        etiqueta.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        print(Path(__file__).parent.absolute())
        print(Path("chat_bot.jpg"))
        print(Path("chat_bot.jpg").absolute())


        # poner una imagen en la etiqueta
        # imagen = QPixmap(absPath("chat_bot.jpg"))
        # etiqueta.setPixmap(imagen)
        # etiqueta.setScaledContents(True)

        self.setCentralWidget(etiqueta)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())