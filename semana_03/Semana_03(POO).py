class Clima:
    def __init__(self):
        self.temperaturas = []

    # Método para ingresar temperatura diaria
    def ingresar_temperatura(self):
        temperatura = float(input("Ingresar temperatura diaria (en grados Celsius): "))
        self.temperaturas.append(temperatura)

    # Método para calcular promedio semanal
    def calcular_promedio_semanal(self):
        return sum(self.temperaturas) / len(self.temperaturas)

    # Método para mostrar promedio semanal
    def mostrar_promedio_semanal(self):
        promedio_semanal = self.calcular_promedio_semanal()
        print(f"Promedio semanal: {promedio_semanal:.2f} grados Celsius")

# Crear objeto Clima
clima = Clima()

# Ingresar temperaturas diarias
for _ in range(7):
    clima.ingresar_temperatura()

# Mostrar promedio semanal
clima.mostrar_promedio_semanal()