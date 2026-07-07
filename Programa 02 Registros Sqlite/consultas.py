
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from helpers import absPath
app = QApplication(sys.argv)

conexion = QSqlDatabase.addDatabase("QSQLITE")
conexion.setDatabaseName(absPath("contactos.db"))
if not conexion.open():
    print("No se puede conectar")
else:
    print("Conexión abierta?", conexion.isOpen())

consulta = QSqlQuery()
consulta.exec("DROP TABLE IF EXISTS contactos")
consulta.exec("""
    CREATE TABLE IF NOT EXISTS contactos (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        nombre VARCHAR(40) NOT NULL,
        empleo VARCHAR(50),
        email VARCHAR(40) NOT NULL
    )""")

print(conexion.tables())

nombre, empleo, email = "Alfredo", "Capacitador", "alfred@ejemplo.com"
consulta.exec(f"""
    INSERT INTO contactos (nombre, empleo, email) 
    VALUES ('{nombre}', '{empleo}', '{email}')
""")

contactos = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("javier", "Analista de datos", "javier@ejemplo.com"),
    ("marta", "Experta en Python", "marta@ejemplo.com")
]

consulta.prepare("INSERT INTO contactos (nombre, empleo, email) VALUES (?,?,?)")

for nombre, empleo, email in contactos:
    consulta.addBindValue(nombre)
    consulta.addBindValue(empleo)
    consulta.addBindValue(email)
    consulta.exec()

consulta.exec("SELECT nombre, empleo, email FROM contactos")

# if consulta.first():
#     print(consulta.value("nombre"),
#           consulta.value("empleo"),
#           consulta.value("email"))

while consulta.next():
    print(consulta.value("nombre"),
          consulta.value("empleo"),
          consulta.value("email"))

conexion.close()
print("Conexión cerrada?", not conexion.isOpen())
