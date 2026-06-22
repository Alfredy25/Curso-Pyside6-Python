
class Madre():
    def __init__(self, nombre: str):
        print("Soy Madre", nombre)

class Padre:
    def __init__(self):
        print("Soy Padre")

class Hijo(Madre, Padre):
    def __init__(self):
        Madre.__init__(self, "Juana")
        Padre.__init__(self)
        print("Soy Hijo")

hijo = Hijo()