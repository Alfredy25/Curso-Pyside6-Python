from datetime import date
from decimal import Decimal

from PySide6.QtCore import QDate
from PySide6.QtWidgets import (
    QDateEdit,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QComboBox, QDoubleSpinBox
)

from course.alfredo.pyside.kardex.app.entity.operation import Operation


class FinancialFormDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Registrar operación")
        self.resize(450, 300)

        self.company_input = QLineEdit()
        self.account_number_input = QLineEdit()
        self.issuer_input = QLineEdit()

        self.operation_input = QComboBox()
        self.operation_input.addItems(["", "COMPRA", "VENTA", "COSTO"])

        self.movement_date_input = QDateEdit()
        self.movement_date_input.setCalendarPopup(True)
        self.movement_date_input.setDate(QDate.currentDate())

        self.instrument_input = QLineEdit()

        self.quantity_input = QDoubleSpinBox()
        self.quantity_input.setDecimals(4)
        self.quantity_input.setMaximum(1_000_000_000)

        self.price_input = QDoubleSpinBox()
        self.price_input.setDecimals(4)
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
        button_box = QDialogButtonBox()
        save_btn = button_box.addButton(QDialogButtonBox.StandardButton.Save)
        save_btn.setText("Guardar")
        cancel_btn = button_box.addButton(QDialogButtonBox.StandardButton.Cancel)
        cancel_btn.setText("Cancelar")

        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(button_box)

        self.setLayout(main_layout)

    def get_operation_data(self) -> Operation:
        """
        Return raw data (Python types) to build Operation.
        """
        qdate: QDate = self.movement_date_input.date()
        movement_date_py: date = date(
            qdate.year(), qdate.month(), qdate.day()
        )
        operation = Operation()

        operation.company = self.company_input.text()
        operation.account_number = self.account_number_input.text()
        operation.issuer = self.issuer_input.text()
        operation.operation = self.operation_input.currentText()
        operation.movement_date = movement_date_py
        operation.instrument = self.instrument_input.text()
        operation.quantity = Decimal(self.quantity_input.text())
        operation.price = Decimal(self.price_input.text())

        return operation

