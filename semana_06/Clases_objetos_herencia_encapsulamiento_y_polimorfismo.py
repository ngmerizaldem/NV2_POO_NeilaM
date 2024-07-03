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

        class Coche(Vehiculo):
            def __init__(self, marca, modelo, puertas):
                super().__init__(marca, modelo)
                self.puertas = puertas

            def describir(self):
                super().describir()
                print(f"Es un coche de {self.puertas} puertas.")