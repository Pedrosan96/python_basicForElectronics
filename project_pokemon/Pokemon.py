class Pokemon:
    def __init__(self, nombre, id, tipo):
        self.nombre = nombre
        self.id = id
        self.tipo = tipo

def __init__(self, data):
    self.from_dict(data)

  def print_pokemon(self):
    print("ID: " + str(self.id))
    print("Nombre: " + self.nombre)
    print("Tipo: " + self.tipo)
    print("")


  def to_dic(self):
    data = {
        'id': self.id
        'nombre': self.nombre
        'tipo': self.tipo
    }
    return data

    def from_dict(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.tipo = data['tipo']

class PokeEsteroides(Pokemon):  #herencia
    def __init__(self, data):
        super(data)
        self.movimientos = []

    def print_pokemon(self):
        Pokemon.print_pokemon()
        for mov in self.movimientos():
            

class Movimiento:
    def __init__(self)
        pass
