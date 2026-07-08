from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog, QMainWindow, QPushButton, QTableWidget, QVBoxLayout, QWidget, QTableWidgetItem, QMessageBox
)

from course.alfredo.pyside.kardex.app.config.db import SessionLocal
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

        self._action_col_index = 9 # La columna 9 corresponde a acciones donde irá el botón "Eliminar".
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
            QMessageBox.critical(
                self,
                "Error",
                f"Error al cargar operaciones desde la base de datos:\n{exc}"
            )
            return
        # Borra todas las filas.
        self.table.setRowCount(0)
        # Agregar filas
        for op in operations:
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
            # Agrega la celda creada o item en la fila y columna que corresponde
            self.table.setItem(row, col, item)

        # Columna de acciones agregar botones (botón eliminar)
        self._add_action_button(row, operation.id)

    # Se le pasa la fila actual en donde se agrega la operacion y el id del Objeto Operacion
    def _add_action_button(self, row: int, operation_id: int):
        """
        Add an action to the table
        """
        # Se crea el botón con el texto de Eliminar
        btn = QPushButton("Eliminar")
        # Guardamos el id en la propiedad del botón
        btn.setProperty("operation_id", operation_id)
        # conecta boton al evento on_delete_clicked(btn)
        btn.clicked.connect(lambda _checked=False, b=btn: self.on_delete_clicked(b))
        # Insertar botón en la fila actual en la columna de acciones
        self.table.setCellWidget(row, self._action_col_index, btn) # La celda contiene un botón en lugar de texto.


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
            operation = dialog.get_operation_data() # Regresa una entidad Operation.

            try:
                # Guardar en BD
                saved_operation = self.operation_repo.save(operation)
            except Exception as exc:
                QMessageBox.critical(
                    self,
                    "Error",
                    f"Error al guardar la operación en la base de datos:\n{exc}"
                )
                return
            # Agrega la operación a la tabla sin recargar la bd
            self._append_operation_to_table(saved_operation)

    def on_delete_clicked(self, button):
        # Obtiene el id que se guardo en el botón id del objeto Operation
        op_id = button.property("operation_id")
        if op_id is None:
            return

        reply = QMessageBox.question(
            self,
            "Confirmar Eliminación",
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
        row_to_remove = -1
        for row in range(self.table.rowCount()):
            cell_widget = self.table.cellWidget(row, self._action_col_index)
            # verifica si el botón de eliminar es el mismo que el boton actual del recorrido
            if cell_widget is button:
                row_to_remove = row
                break
        if row_to_remove >= 0:
            # elimina la fila completa
            self.table.removeRow(row_to_remove)



