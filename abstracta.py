from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def avanzar(self):
        pass

class Carro(Vehiculo):
    def avanzar(self):
        print("Avanzando en un carro")


toyota = Carro()
toyota.avanzar()
