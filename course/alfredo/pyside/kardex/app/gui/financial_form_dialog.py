from datetime import date
from decimal import Decimal

from PySide6.QtCore import QDate, Qt
from PySide6.QtWidgets import (
    QDateEdit,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QComboBox, QDoubleSpinBox, QMessageBox
)

from course.alfredo.pyside.kardex.app.entity.operation import Operation


class FinancialFormDialog(QDialog):
    def __init__(self, parent=None, operation: Operation | None = None):
        super().__init__(parent)

        self.setWindowTitle("Registrar operación")
        self.resize(450, 300)
        self.setModal(True)
        self._operation = operation

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

        # Si viene una operación, pre-rellenamos
        if self._operation is not None:
            self._fill_from_operation(self._operation)

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

        # button_box.accepted.connect(self.accept)
        button_box.accepted.connect(self._on_accept)
        button_box.rejected.connect(self.reject)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(button_box)

        self.setLayout(main_layout)
    def _on_accept(self):
        if not self.validate_form():
            return # No cerrar el dialogo
        self.accept() # Cerrar solo si esta todo valido

    def _fill_from_operation(self, operation: Operation):
        self.company_input.setText(operation.company or "")
        self.account_number_input.setText(operation.account_number or "")
        self.issuer_input.setText(operation.issuer or "")

        idx = self.operation_input.findText(operation.operation or "", Qt.MatchFlag.MatchExactly)
        if idx >= 0:
            self.operation_input.setCurrentIndex(idx)

        if operation.movement_date:
            qd = QDate(operation.movement_date.year, operation.movement_date.month, operation.movement_date.day)
            self.movement_date_input.setDate(qd)

        self.instrument_input.setText(operation.instrument or "")
        self.quantity_input.setValue(float(operation.quantity or 0.00))
        self.price_input.setValue(float(operation.price or 0.00))

    def apply_to_operation(self, operation: Operation):
        """
        Copia los valores del form a la instancia Operation recibida.
        No guarda en BD, eso lo hace el repo.
        """

        qdate: QDate = self.movement_date_input.date()
        movement_date_py = date(qdate.year(), qdate.month(), qdate.day())

        operation.company = self.company_input.text().strip()
        operation.account_number = self.account_number_input.text().strip()
        operation.issuer = self.issuer_input.text().strip()
        operation.operation = self.operation_input.currentText()
        operation.movement_date = movement_date_py
        operation.instrument = self.instrument_input.text().strip()
        operation.quantity = Decimal(self.quantity_input.value())
        operation.price = Decimal(self.price_input.value())

    def get_new_operation_data(self) -> Operation:
        """
        Return raw data (Python types) to build Operation.
        """
        qdate: QDate = self.movement_date_input.date()
        movement_date_py: date = date(
            qdate.year(), qdate.month(), qdate.day()
        )
        operation = Operation()

        operation.company = self.company_input.text().strip()
        operation.account_number = self.account_number_input.text().strip()
        operation.issuer = self.issuer_input.text().strip()
        operation.operation = self.operation_input.currentText()
        operation.movement_date = movement_date_py
        operation.instrument = self.instrument_input.text()
        operation.quantity = Decimal(self.quantity_input.value())
        operation.price = Decimal(self.price_input.value())

        return operation

    def validate_form(self) -> bool:

        errors = []
        first_error_widget = None

        # Campos obligatorios
        required_fields = [
            (self.company_input, "Company"),
            (self.account_number_input, "Número de cuenta"),
            (self.issuer_input, "Emisor"),
            (self.instrument_input, "Instrumento")
        ]

        for widget, label in required_fields:
            if not widget.text().strip():
                errors.append(f"• El campo '{label}' es obligatorio")
                if first_error_widget is None:
                    first_error_widget = widget

        # Operación seleccionada
        if not self.operation_input.currentText().strip():
            errors.append("• Debe seleccionar una operación")
            if first_error_widget is None:
                first_error_widget = self.operation_input

        # Fecha válida
        if not self.movement_date_input.date().isValid():
            errors.append("• La fecha de movimiento no es válida")
            if first_error_widget is None:
                first_error_widget = self.movement_date_input

        # Cantidad
        qty = self.quantity_input.value()
        if qty <= Decimal("0.00"):
            errors.append("• La cantidad debe ser mayor que cero")
            if first_error_widget is None:
                first_error_widget = self.quantity_input

        # Precio
        price = self.price_input.value()
        if price <= 0:
            errors.append("• El precio debe ser mayor que cero")
            if first_error_widget is None:
                first_error_widget = self.price_input

        # Mostrar todos los errores encontrados
        if errors:
            QMessageBox.warning(
                self,
                "Validación",
                "Se encontraron los siguientes errores:\n\n" + "\n".join(errors)
            )

            if first_error_widget:
                first_error_widget.setFocus()

            return False

        return True
