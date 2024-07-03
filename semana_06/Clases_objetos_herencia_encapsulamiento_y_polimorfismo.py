class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.__modelo = modelo  # Encapsulamos el atributo modelo

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def describir(self):
        print(f"Vehículo de marca {self.marca}, modelo {self.__modelo}")
        