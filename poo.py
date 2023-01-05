class Casa():
    # Atributos
    color = "Amarillo"
    numeracion = None
    frente = "10 mts"
    fondo = "20 mts"
    dueño = None
    registrada = None

    # Constructor
    def __init__(self, is_registrada):
        self.registrada = is_registrada

    # Muestra un mensaje cuando entendible cuando se llama
    # la funcion print(casa)
    def __str__(self) -> str:
        return f"""
Esta es una casa
El dueño es {self.dueño}
El color es {self.color}
"""

    def __repr__(self) -> str:
        return f"Casa numero {self.numeracion}"

    # Métodos
    def pintar(self, nuevo_color):
        self.color = nuevo_color

    def vender(self, nuevo_dueño):
        self.dueño = nuevo_dueño
        return print("Casa vendida exitosamente")

    # Privado porque comienza con __
    def __entregar_llaves(self):
        print("Se entregan las llaves de la casa")

    def gestionar_llaves(self, receptor):
        if receptor != self.dueño:
            raise Exception("No se pueden entregar llaves a alguien que no sea el dueño")
        self.__entregar_llaves()

    @staticmethod
    def get_atributos_Obligatorios():
        return ["is_registrada"]


casa1 = Casa(is_registrada=True)

print("\n")
print(type(casa1))
print(casa1.color)
print(casa1.numeracion)
#casa1.numeracion = "A1"
print(casa1.numeracion)

casa1.pintar("Azul")
print(casa1.color)

casa1.vender("Diego")


casa2 = Casa(is_registrada=False)
print(casa1)
print(casa2)

casa1.gestionar_llaves("Diego")
print(Casa.get_atributos_Obligatorios())

print(repr(casa1))
