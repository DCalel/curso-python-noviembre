def saludar():
    print("Saludos a todos")

nombre = "Rafael"
print(nombre)

#Esta variable es un string
apellido = "Flores"

#Enteros
edad = 15
print(type(edad))

#Decimal
peso = 1.5
print(type(peso))

print(edad + peso)

is_adult = True
habilitar_noticias = False

print(nombre + " " + apellido)
print(f"{nombre} {apellido}")

#Evitar sumar distintos tipos de datos
#nombre + edad
print(nombre + str(edad))


#Lista
alumnos = ["Angle","Byron","Deivin","Diego"]

print(alumnos[1])

#Diccionarios
persona = {
    "nombre":"Diego",
    "apellido":"Calel",
    "genero":"masculino",
    "edad": 21,
    "es_adulto":True,
    "altura":1.66
}

#Lista de diccionarios
estudiante = [
    {"nombre":"Ruben","apellido":"Hernández"},
    {"nombre":"Oscar","apellido":"Carrera"},
    {"nombre":"David","apellido":"Zuñiga"},
]

print(estudiante[0]["nombre"])