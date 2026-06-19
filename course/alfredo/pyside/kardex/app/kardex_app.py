import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QFormLayout,
    QLineEdit,
    QDateEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox
)
from PySide6.QtCore import QDate


class FinancialForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Formulario de Movimientos Financieros")
        self.setGeometry(100, 100, 400, 300)

        # Inputs
        self.company_input = QLineEdit()
        self.account_number_input = QLineEdit()
        self.issuer_input = QLineEdit()
        self.operation_input = QLineEdit()
        self.movement_date_input = QDateEdit()
        self.movement_date_input.setCalendarPopup(True)
        self.movement_date_input.setDate(QDate.currentDate())
        self.instrument_input = QLineEdit()
        self.quantity_input = QLineEdit()
        self.price_input = QLineEdit()

        # Form layout
        form_layout = QFormLayout()

        form_layout.addRow("Compañía:", self.company_input)
        form_layout.addRow("Número de cuenta:", self.account_number_input)
        form_layout.addRow("Emisor:", self.issuer_input)
        form_layout.addRow("Operación:", self.operation_input)
        form_layout.addRow("Fecha de movimiento:", self.movement_date_input)
        form_layout.addRow("Instrumento:", self.instrument_input)
        form_layout.addRow("Cantidad:", self.quantity_input)
        form_layout.addRow("Precio:", self.price_input)

        # Buttons
        self.save_button = QPushButton("Guardar")
        self.save_button.clicked.connect(self.save_record)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.save_button)

        self.setLayout(main_layout)

    def save_record(self):
        record_data = {
            "company": self.company_input.text(),
            "account_number": self.account_number_input.text(),
            "issuer": self.issuer_input.text(),
            "operation": self.operation_input.text(),
            "movement_date": self.movement_date_input.date().toString("yyyy-MM-dd"),
            "instrument": self.instrument_input.text(),
            "quantity": self.quantity_input.text(),
            "price": self.price_input.text()
        }

        QMessageBox.information(
            self,
            "Información",
            "Registro guardado correctamente."
        )

        print(record_data)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = FinancialForm()
    window.show()

    sys.exit(app.exec())