class Vehiculo():
    ruedas = None

    def avanzar(self):
        print("El vehiculo está avanzando")

class Carro(Vehiculo):
    ruedas = 4

    def avanzar(self):
        print("Avanzando en un carro")

class Moto(Vehiculo):
    ruedas = 2
    pass

nissan = Carro()
nissan.avanzar()
print(nissan.ruedas)

yamaha = Moto()
yamaha.avanzar();

