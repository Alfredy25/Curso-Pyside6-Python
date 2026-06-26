import sys


from PySide6.QtGui import QIcon, QAction
from pathlib import Path
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QStatusBar, QToolBar, QLabel, QDockWidget
from PySide6.QtCore import Qt


def absPath(file):
    return str(Path(__file__).parent.parent.absolute() / file)

class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)
        icono = QIcon(absPath('extractor_ocr.png'))
        self.setWindowIcon(icono)
        self.setStatusBar(QStatusBar(self))
        self.construir_menu()
        self.construir_herramientas()

        self.construir_docks()

        self.setCentralWidget(Caja("gray"))

    def construir_docks(self):
        dock1 = QDockWidget()
        dock1.setWindowTitle("DOCK")
        dock1.setWidget(Caja("green"))
        # dock.setMinimumHeight(100)
        # dock.setMinimumWidth(200)
        dock1.setMinimumSize(120, 100)
        dock1.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures |
                         QDockWidget.DockWidgetFeature.DockWidgetFloatable |
                         QDockWidget.DockWidgetFeature.DockWidgetClosable | QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock1)

        dock2 = QDockWidget()
        dock2.setWindowTitle("DOCK 2")
        dock2.setWidget(Caja("yellow"))
        dock2.setMinimumSize(120, 100)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock2)

        dock3 = QDockWidget()
        dock3.setWindowTitle("DOCK 3")
        dock3.setWidget(Caja("blue"))
        dock3.setMinimumSize(120, 100)
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, dock3)


    def construir_herramientas(self):
        herramientas = QToolBar("Barra de herramientas")
        herramientas.addAction(
            QIcon(absPath('x_icon.png')),"S&alir", self.close)

        herramientas.addAction(self.accion_info)
        self.addToolBar(herramientas)

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

        self.accion_info = accion_info

    def mostrar_info(self):
        # QMessageBox.information(self, 'Infomacion', 'Esto es un texto informativo')
        QMessageBox.about(self, 'Infomacion', 'Esto es un texto informativo')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())