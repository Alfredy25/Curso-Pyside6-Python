import json

from helpers import absPath

datos = [{
    "nombre": "Héctor",
    "empleo": "Instructor",
    "email": "hektor@ejemplo.com"
}]

contactos = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("javier", "Analista de datos", "javier@ejemplo.com"),
    ("marta", "Experta en Python", "marta@ejemplo.com")
]

for nombre, empleo, email in contactos:
    datos.append({
        "nombre": nombre,
        "empleo": empleo,
        "email": email
    })


with open(absPath("contactos.json"), "w") as fichero:
    json.dump(datos, fichero)

with open(absPath("contactos.json")) as fichero:
    datos_json = json.load(fichero)
    print(datos_json[0]["nombre"])
    for contacto in datos_json:
        print(contacto["nombre"], contacto["empleo"], contacto["email"])
