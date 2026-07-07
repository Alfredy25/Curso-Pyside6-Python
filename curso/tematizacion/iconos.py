
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QStyle, QGridLayout)

import sys


iconos = ["SP_CustomBase", "SP_TitleBarMenuButton", "SP_TitleBarMinButton", "SP_TitleBarMaxButton","SP_TitleBarCloseButton","SP_TitleBarNormalButton", "SP_TitleBarShadeButton", "SP_TitleBarUnshadeButton", "SP_TitleBarContextHelpButton","SP_DockWidgetCloseButton", "SP_MessageBoxInformation", "SP_MessageBoxWarning", "SP_MessageBoxCritical", "SP_MessageBoxQuestion","SP_DesktopIcon", "SP_TrashIcon", "SP_ComputerIcon", "SP_DriveFDIcon", "SP_DriveHDIcon", "SP_DriveCDIcon", "SP_DriveDVDIcon", "SP_DriveNetIcon", "SP_DirOpenIcon", "SP_DirClosedIcon","SP_DirLinkIcon", "SP_DirLinkOpenIcon", "SP_FileIcon", "SP_FileLinkIcon","SP_ToolBarHorizontalExtensionButton", "SP_ToolBarVerticalExtensionButton", "SP_FileDialogStart", "SP_FileDialogEnd", "SP_FileDialogToParent", "SP_FileDialogNewFolder", "SP_FileDialogDetailedView",
"SP_FileDialogInfoView", "SP_FileDialogContentsView", "SP_FileDialogListView", "SP_FileDialogBack","SP_DirIcon", "SP_DialogOkButton", "SP_DialogCancelButton", "SP_DialogHelpButton","SP_DialogOpenButton", "SP_DialogSaveButton", "SP_DialogCloseButton", "SP_DialogApplyButton", "SP_DialogResetButton", "SP_DialogDiscardButton", "SP_DialogYesButton", "SP_DialogNoButton","SP_ArrowUp", "SP_ArrowDown", "SP_ArrowLeft", "SP_ArrowRight", "SP_ArrowBack","SP_ArrowForward", "SP_DirHomeIcon", "SP_CommandLink", "SP_VistaShield", "SP_BrowserReload","SP_BrowserStop", "SP_MediaPlay", "SP_MediaStop", "SP_MediaPause", "SP_MediaSkipForward",
"SP_MediaSkipBackward", "SP_MediaSeekForward","SP_MediaSeekBackward", "SP_MediaVolume","SP_MediaVolumeMuted", "SP_LineEditClearButton", "SP_DialogYesToAllButton","SP_DialogNoToAllButton", "SP_DialogSaveAllButton", "SP_DialogAbortButton","SP_DialogRetryButton", "SP_DialogIgnoreButton", "SP_RestoreDefaultsButton","SP_TabCloseButton", "NStandardPixmap"]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        for contador, nombre in enumerate(iconos):
            icono = self.style().standardIcon(getattr(QStyle, nombre))

            boton = QPushButton(icono, nombre)

            layout.addWidget(boton, contador // 5, contador % 5)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # estilo fusion
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())