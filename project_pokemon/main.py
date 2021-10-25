from Pokemon import *
import json

POKEMON_FILE = pokemon.json

def ejemplo1():
  x, y, z = "Bulbasor", "Charmander", "Pikachu"
  print(x)
  print(y)
  print(z)

#Numeros complejos
 def ejemplo2():
     x = 5j
     print(type(x))

#Listas
def ejemplo3():
    lista = [5, 4, 3, 2, 78]
    for numero in lista:
        print(numero)

#tuplas
def ejemplo4():
    tupla= ("Bulbsaur", "Squirtle", "Charmander")
    x, y, z = tupla
    print(y)

#Diccionario
def ejemplo5():
    diccionario = {
        "nombre": "Juanito",
        "edad": 5,
        "esMenor": True,
        "arreglo": [],
        "objeto": {
            "movimiento": "cabezaso"
        },
        "nulo": None
    }
    print(diccionario['objeto']['movimiento'])


# Bytes
def ejemplo6():
  bytes = bytearray("Hola mundo", "utf-8")
  print(bytes)
  mv = memoryview(bytes)
  print(mv[0:2])

def ejemplo7():
    pikachu = Pokemon(tipo="electrico", id=25, nombre="Pikachu")
    #pikachu.print_pokemon()
    dataPikachu = pikachu.to_dic()
    dataPikachu['otro'] = "otroValor"
    for key in dataPikachu:
        print(key + ": " + str(dataPikachu[key]))

def ejemplo8():
    file = open("pokemons.txt", "wt", encoding='utf-8')#wt=to write, in text
    file.write("Hola Mundo!")
    flie.close()
    print("Archivo creado :)")

def ejemplo9():
    file = open("pokemons.txt", "rt", encoding='utf-8')
    #leido = file.read(5)#esta linea lee solo 5 caracteres, si se deja vacia lee todo
    leido = file.readline()
    print(leido)
    file.close()

def ejemplo10():
    pikachu = Pokemon("Pikachu", 25, "electrico")
    bulbasaur = Pokemon("Bolbasaur", 1, "planta")
    squirtle =Pokemon("Squirtle", 7, "agua")
    pokemons = [pikachu, bulbasaur, squirtle]
    data = {
        'pokemons': pokemons
    }

    pokemonsFile = open("pokemons.json", "w", encoding='utf-8')
    pokemonsFile.write(json.dumos(data))
    pokemonsFile.close()
    print("!Pokemons escritos con exito")
def ejemplo11():
    file = open(POKEMON_FILE, "r", encoding='utf-8')
    data = json.loads(file.read())
    file.close()
    pokemons = []
    for pokemon in data['pokemons']:
        pokemons.append(Pokemon(pokemon))
        #pokemons.append(Pokemon(pokemon['nombre'], pokemon['id'], pokemon['tipo']))

    for pokemon in pokemons:
        pokemons.print_pokemon()

def ejemplo12():    #switch y for normal
    x = 2
    if x==0:
        print("x igual a cero")
    elif x==1:
        print("x igual a uno")
    else:
        print("No equivale a nada")

    for i in range(5):  #(2,8) inicio y final   (2, 8, 2) inicio, final y salto
        print(str(i))


if __name__ == '__main__':
  ejemplo8()
