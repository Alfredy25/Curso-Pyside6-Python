import sys

from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox,QStatusBar
from pathlib import Path


def absPath(file):
    ruta = Path(__file__).parent.parent.parent.absolute() / file
    print(ruta)
    return str(ruta)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480,330)
        icon = QIcon(absPath('extractor_ocr.png'))
        self.setWindowIcon(icon)
        self.setStatusBar(QStatusBar(self))

        self.construir_menu()

    def construir_menu(self):
        menu = self.menuBar()
        menu_archivo = menu.addMenu('&Menú')
        menu_archivo.addAction("&Prueba")

        submenu = menu_archivo.addMenu('&SubMenu')
        submenu.addAction("Subopción &1")
        submenu.addAction("Subopción &2")

        menu_archivo.addSeparator()
        menu_archivo.addAction(QIcon(absPath("X_Red.png")),"S&alir", self.close, "Ctrl+Q")

        menu_ayuda = menu.addMenu('Ay&uda')
        accion_info = QAction('&Informacion', self)
        accion_info.setIcon(QIcon(absPath("info.png")))
        accion_info.setShortcut('Ctrl+I')
        accion_info.triggered.connect(self.mostrar_info)
        accion_info.setStatusTip("Muestra informacion irrelevante")
        menu_ayuda.addAction(accion_info)

    def mostrar_info(self):
        QMessageBox().about(self, "Información","Esto es un texto informativo")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())