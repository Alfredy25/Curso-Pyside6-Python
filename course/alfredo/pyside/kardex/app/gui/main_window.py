from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog, QMainWindow, QPushButton, QTableWidget, QVBoxLayout, QWidget, QTableWidgetItem, QMessageBox
)

from course.alfredo.pyside.kardex.app.config.db import SessionLocal
from course.alfredo.pyside.kardex.app.entity.operation import Operation
from course.alfredo.pyside.kardex.app.gui.financial_form_dialog import FinancialFormDialog
from course.alfredo.pyside.kardex.app.repository.operation_repository_impl import OperationRepositoryImpl


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Control de Operaciones")
        self.resize(1000, 600)

        # Repository (session factory injected)
        self.operation_repo = OperationRepositoryImpl(SessionLocal)

        # Root central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout vertical raíz
        root_layout = QVBoxLayout(central_widget)

        # Botón superior
        self.register_button = QPushButton("Registrar operación")
        self.register_button.clicked.connect(self.open_register_dialog)
        root_layout.addWidget(self.register_button, alignment=Qt.AlignmentFlag.AlignLeft)
        self.table = QTableWidget()

        # Placeholder para futura tabla
        self.table = QTableWidget(0, 10)
        self.table.setHorizontalHeaderLabels(
            [
            "ID",
            "Compañía",
            "Número de cuenta",
            "Emisor",
            "Operacion",
            "Fecha movimiento",
            "Instrumento",
            "Cantidad",
            "Precio",
            "Acciones"
            ]
        )
        self._action_col_index = 9 # índice de la columna "Acciones"

        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setAlternatingRowColors(True)
        root_layout.addWidget(self.table)

        # Initial load from DB
        self.load_operations()

    def load_operations(self):
        """
        Load all operations from the database and fill the table
        """
        try:
            operations = self.operation_repo.find_all()
        except Exception as exc:
            QMessageBox.critical(
                self,
                "Error",
                f"Error al cargar operaciones desde la base de datos:\n{exc}"
            )
            return

        self.table.setRowCount(0)

        for op in operations:
            self._append_operation_to_table(op)

    def _append_operation_to_table(self, operation: Operation):
        """
        Append a single Operation row to the table
        """
        row = self.table.rowCount()
        self.table.insertRow(row)

        values = [
            operation.id,
            operation.company,
            operation.account_number,
            operation.issuer,
            operation.operation,
            operation.movement_date.isoformat() if operation.movement_date else None,
            operation.instrument,
            str(operation.quantity),
            str(operation.price)
        ]

        for col, value in enumerate(values):
            item = QTableWidgetItem(str(value) if value is not None else "")
            self.table.setItem(row, col, item)

        # Columna de acciones (botón eliminar)
        self._add_action_button(row, operation.id)

    def _add_action_button(self, row: int, operation_id: int):
        """
        Add an action to the table
        """
        btn = QPushButton("Eliminar")
        # Guardamos el id en la propiedad del botón
        btn.setProperty("operation_id", "operation_id")
        btn.clicked.connect(lambda _checked=False, b=btn: self.on_delete_clicked(b))

        self.table.setCellWidget(row, self._action_col_index, btn)


    # ------------ UI actions -------------
    def open_register_dialog(self):
        dialog = FinancialFormDialog(self)
        answer = dialog.exec()
        if answer == QDialog.DialogCode.Accepted:
            operation = dialog.get_operation_data()

            try:
                saved_operation = self.operation_repo.save(operation)
            except Exception as exc:
                QMessageBox.critical(
                    self,
                    "Error",
                    f"Error al guardar la operación en la base de datos:\n{exc}"
                )
                return

            self._append_operation_to_table(saved_operation)
