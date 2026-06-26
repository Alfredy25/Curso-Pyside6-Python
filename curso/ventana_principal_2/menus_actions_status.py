import sys


from PySide6.QtGui import QIcon, QAction
from pathlib import Path
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QStatusBar


def absPath(file):
    return str(Path(__file__).parent.parent.absolute() / file)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)
        icono = QIcon(absPath('extractor_ocr.png'))
        self.setWindowIcon(icono)
        self.setStatusBar(QStatusBar(self))

        self.construir_menu()

    def construir_menu(self):
        menu = self.menuBar()

        menu_archivo = menu.addMenu('&Menú')
        menu_archivo.addAction('&Prueba')

        submenu_archivo = menu_archivo.addMenu('&Submenu')
        submenu_archivo.addAction('Subopcion &1')
        submenu_archivo.addAction('Subopcion &2')

        menu_archivo.addSeparator()
        menu_archivo.addAction(QIcon(absPath("x_icon.png")), 'S&alir', self.close, "Ctrl+Q")

        menu_ayuda = menu.addMenu('Ay&uda')
        accion_info = QAction("&Informacion", self)
        accion_info.setIcon(QIcon(absPath("informacion_ico.png")))
        accion_info.setShortcut("Ctrl+I")
        accion_info.triggered.connect(self.mostrar_info)
        accion_info.setStatusTip("Muestra informacion irrelevante")
        menu_ayuda.addAction(accion_info)

    def mostrar_info(self):
        # QMessageBox.information(self, 'Infomacion', 'Esto es un texto informativo')
        QMessageBox.about(self, 'Infomacion', 'Esto es un texto informativo')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())