from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QTabWidget
from PySide6.QtCore import Qt
import sys


class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color: {color}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #          ancho,alto px
        self.resize(500, 400)

        # Contenedor central
        layout_tabs = QTabWidget()
        layout_tabs.addTab(Caja("orange"), "Naranja")
        layout_tabs.addTab(Caja("gray"), "Gris")
        layout_tabs.addTab(Caja("pink"), "Rosa")

        layout_tabs.setTabPosition(QTabWidget.TabPosition.West)
        layout_tabs.setMovable(True)
        self.setCentralWidget(layout_tabs)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())