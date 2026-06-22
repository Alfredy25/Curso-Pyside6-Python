import sys

from PySide6.QtCore import QDate
from PySide6.QtWidgets import (
    QApplication,
    QDateEdit,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QTableWidget,
    QVBoxLayout,
    QWidget, QComboBox, QDoubleSpinBox
)


class FinancialFormDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Registrar operación")
        self.resize(450, 300)

        self.company_input = QLineEdit()
        self.account_number_input = QLineEdit()
        self.issuer_input = QLineEdit()

        self.operation_input = QComboBox()
        self.operation_input.addItems(["COMPRA", "VENTA", "COSTO"])

        self.movement_date_input = QDateEdit()
        self.movement_date_input.setCalendarPopup(True)
        self.movement_date_input.setDate(QDate.currentDate())

        self.instrument_input = QLineEdit()

        self.quantity_input = QDoubleSpinBox()
        self.quantity_input.setDecimals(4)
        self.quantity_input.setMaximum(1_000_000_000)

        self.price_input = QDoubleSpinBox()
        self.price_input.setDecimals(6)
        self.price_input.setMaximum(1_000_000_000)

        # Form layout (textos en español)
        form_layout = QFormLayout()
        form_layout.addRow("Compañía:", self.company_input)
        form_layout.addRow("Número de cuenta:", self.account_number_input)
        form_layout.addRow("Emisor:", self.issuer_input)
        form_layout.addRow("Operación:", self.operation_input)
        form_layout.addRow("Fecha movimiento:", self.movement_date_input)
        form_layout.addRow("Instrumento:", self.instrument_input)
        form_layout.addRow("Cantidad:", self.quantity_input)
        form_layout.addRow("Precio:", self.price_input)

        # Botones OK/Cancel
        button_box = QDialogButtonBox(
            QDialogButtonBox.Save | QDialogButtonBox.Cancel
        )

        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(button_box)

        self.setLayout(main_layout)

    def get_data(self):
        return {
            "company": self.company_input.text(),
            "account_number": self.account_number_input.text(),
            "issuer": self.issuer_input.text(),
            "operation": self.operation_input.text(),
            "movement_date": self.movement_date_input.date().toString("yyyy-MM-dd"),
            "instrument": self.instrument_input.text(),
            "quantity": self.quantity_input.text(),
            "price": self.price_input.text(),
        }


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Control de Operaciones")
        self.resize(1000, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.register_button = QPushButton("Registrar operación")
        self.register_button.clicked.connect(self.open_operation_dialog)

        # Placeholder para futura tabla
        self.operations_table = QTableWidget()

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.register_button)
        main_layout.addWidget(self.operations_table)

        central_widget.setLayout(main_layout)

    def open_operation_dialog(self):
        dialog = FinancialFormDialog(self)

        if dialog.exec():
            operation_data = dialog.get_data()

            print("Registro capturado:")
            print(operation_data)

            # Aquí más adelante:
            # self.load_operation(operation_data)
            # self.save_to_database(operation_data)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())