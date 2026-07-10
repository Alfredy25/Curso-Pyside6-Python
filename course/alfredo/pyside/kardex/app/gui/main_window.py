from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog, QMainWindow, QPushButton, QTableWidget, QVBoxLayout, QWidget, QTableWidgetItem, QMessageBox, QHBoxLayout
)

from course.alfredo.pyside.kardex.app.config.db import SessionLocal
from course.alfredo.pyside.kardex.app.entity import operation
from course.alfredo.pyside.kardex.app.entity.operation import Operation
from course.alfredo.pyside.kardex.app.gui.financial_form_dialog import FinancialFormDialog
from course.alfredo.pyside.kardex.app.repository.operation_repository_impl import OperationRepositoryImpl

def absPath(file):
    ruta = Path(__file__).parent.absolute() / file
    return str(ruta)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Control de Operaciones")
        self.resize(1100, 700)
        self.operations_by_id: dict[int, Operation] = {}

        # Repository (session factory injected) Creación del repositorio
        self.operation_repo = OperationRepositoryImpl(SessionLocal)

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout vertical raíz
        root_layout = QVBoxLayout(central_widget)

        # Botón Registrar operación
        # Crea el botón
        self.register_button = QPushButton("Registrar operación")
        # Conecta la señal de boton al hacer click
        self.register_button.clicked.connect(self.open_register_dialog)
        # Agrega el boton al layout y lo alinea a la izquierda
        root_layout.addWidget(self.register_button, alignment=Qt.AlignmentFlag.AlignLeft)

        # Crea la tabla con 0 filas y 10 columnas
        self.table = QTableWidget(0, 10)
        # Agrega encabezados a la tabla
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
        # La columna 9 corresponde a acciones donde irá el botón "Eliminar".
        self._action_col_index = 9
        # Ajustes visuales
        # Hace que la última columna ocupe el espacio restante
        self.table.horizontalHeader().setStretchLastSection(True)
        # Alterna colores entre las filas
        self.table.setAlternatingRowColors(True)
        # Agrega la tabla al layout para que quede debajo del botón
        root_layout.addWidget(self.table)

        # Cargar operaciones Al abrir la ventana carga todas las operaciones desde la BD
        self.load_operations()

        self.cargar_qss("qss/QDark.qss")

    def cargar_qss(self, fichero):
        path = absPath(fichero)
        try:
            with open(path) as style:
                self.setStyleSheet(style.read())
        except FileNotFoundError:
            print("No se pudo cargar el fichero")
        except:
            print("Error abriendo los estilos")

    # Obtiene todas las operaciones.
    def load_operations(self):
        """
        Load all operations from the database and fill the table
        """
        try:
            # Obtiene todas las operaciones de la bd
            operations = self.operation_repo.find_all()
        # Si algo falla Muestra un mensaje de error.
        except Exception as exc:
            QMessageBox.critical(self,"Error",
                f"Error al cargar operaciones desde la base de datos:\n{exc}"
            )
            return

        self.operations_by_id.clear()
        # Borra todas las filas.
        self.table.setRowCount(0)
        # Agregar filas
        for op in operations:
            if op.id is None:
                continue
            self.operations_by_id[int(op.id)] = op
            # Inserta una fila por cada operación.
            self._append_operation_to_table(op)

    def _append_operation_to_table(self, operation: Operation):
        """
        Append a single Operation row to the table
        """
        # obtiene el número de fila
        row = self.table.rowCount()
        # Crear nueva fila y la Inserta al final.
        self.table.insertRow(row)
        # Extraer valores del objeto operation
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
        # Llenar celdas del 0 al 8
        for col, value in enumerate(values):
            # Crea el item visual con el valor de la obtenido de operation
            item = QTableWidgetItem(str(value) if value is not None else "") # si no tiene valor asigna vacio
            item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            # Agrega la celda creada o item en la fila y columna que corresponde
            self.table.setItem(row, col, item)

        # Botones editar + eliminar
        self._add_action_button(row, operation.id)

    # Se le pasa la fila actual en donde se agrega la operacion y el id del Objeto Operacion
    def _add_action_button(self, row: int, operation_id: int):
        container = QWidget()

        layout = QHBoxLayout(container)
        layout.setContentsMargins(2, 2, 2, 2)
        layout.setSpacing(4)

        btn_edit = QPushButton("Editar")
        btn_delete = QPushButton("Eliminar")

        btn_edit.setProperty("operation_id", operation_id)
        btn_delete.setProperty("operation_id", operation_id)

        btn_edit.clicked.connect(self.on_edit_clicked)
        btn_delete.clicked.connect(self.on_delete_clicked)

        layout.addWidget(btn_edit)
        layout.addWidget(btn_delete)
        layout.addStretch()

        self.table.setCellWidget(row, self._action_col_index, container)

    def _update_operation_row(self, row: int, operation: Operation):
        values = [
            operation.id,
            operation.company,
            operation.account_number,
            operation.issuer,
            operation.operation,
            operation.movement_date.isoformat() if operation.movement_date else "",
            operation.instrument,
            str(operation.quantity),
            str(operation.price)
        ]

        for col, value in enumerate(values):
            item = self.table.item(row, col)
            if item is None:
                item = QTableWidgetItem()
                self.table.setItem(row, col, item)
            item.setText(str(value) if value is not None else "")


    def _find_row_for_button(self, button: QPushButton) -> int:
        """
        Busca la fila que contiene el botón dado dentro de la columna Actions.
        """
        for row in range(self.table.rowCount()):
            container = self.table.cellWidget(row, self._action_col_index)
            if container is None:
                continue
            # el boton es hijo del contenedor
            if button in container.findChildren(QPushButton):
                return row

        return -1


    # ------------ UI actions -------------
    def open_register_dialog(self):
        # Abrir formulario
        # Crear diálogo
        dialog = FinancialFormDialog(self)
        # Muestra el dialogo exec() es modal.
        # El usuario debe cerrarlo antes de seguir usando la ventana principal.
        answer = dialog.exec()
        # Verificar aceptación
        if answer == QDialog.DialogCode.Accepted:
            # Obtener datos
            operation = dialog.get_new_operation_data() # Regresa una entidad Operation.
            try:
                # Guardar en BD
                saved_operation = self.operation_repo.save(operation)
            except Exception as exc:
                QMessageBox.critical(self,"Error",
                    f"Error al guardar la operación en la base de datos:\n{exc}"
                )
                return

            if saved_operation.id is None:
                return

            self.operations_by_id[int(saved_operation.id)] = saved_operation
            # Agrega la operación a la tabla sin recargar la bd
            self._append_operation_to_table(saved_operation)

    def on_edit_clicked(self):
        button = self.sender()
        if not isinstance(button, QPushButton):
            return

        op_id = button.property("operation_id")
        if op_id is None:
            return

        op_id = int(op_id)
        operation = self.operations_by_id.get(op_id)
        if operation is None:
            QMessageBox.warning(self, "No encontrado", "La operación no existe")
            return

        # Abrimos el dialogo en modo edición
        dialog = FinancialFormDialog(self, operation= operation)
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return

        # Aplicamos cambios sobre la instancia y guardamos en la BD
        dialog.apply_to_operation(operation)

        try:
            saved = self.operation_repo.save(operation)
        except Exception as exc:
            QMessageBox.critical(self, "Error",
                        "Error al actualizar Operacion en BD"
            )
            return

        self.operations_by_id[op_id] = saved

        # Actualizamos solo la fila correspondiente
        row = self._find_row_for_button(button)
        if row >= 0:
            self._update_operation_row(row, saved)


    def on_delete_clicked(self):
        # Obtiene el id que se guardo en el botón id del objeto Operation
        button = self.sender()
        if not isinstance(button, QPushButton):
            return

        op_id = button.property("operation_id")
        if op_id is None:
            return

        reply = QMessageBox.question(
            self,"Confirmar Eliminación",
            "¿Desea eliminar esta operación?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply != QMessageBox.StandardButton.Yes:
            return

        # Borrar el registro de la BD
        try:
            deleted = self.operation_repo.delete(int(op_id))
        except Exception as exc:
            QMessageBox.critical(
                self,
                "Error",
                f"Error al eliminar la operación en la base de datos:\n{exc}"
            )
            return
        # Muestra advertencia si no fue posible eliminar la operacion en la bd
        if not deleted:
            QMessageBox.warning(
                self,
                "No ncontrado",
                "La operación ya no existe en la base de datos"
            )
            # refrescamos la tabla
            # self.load_operations()
            return
        # Buscar la fila que contiene este boton
        row = self._find_row_for_button(button)
        if row >= 0:
            self.table.removeRow(row)

        # quitamos del diccionario
        self.operations_by_id.pop(op_id, None)
