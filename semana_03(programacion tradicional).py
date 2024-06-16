
# Función para ingresar temperatura diaria
def ingresar_temperatura():
    temperatura = float(input("Ingresar temperatura diaria (en grados Celsius): "))
    return temperatura

# Función para calcular promedio semanal
def calcular_promedio_semanal(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Ingresar temperaturas diarias
temperaturas = []
for _ in range(7):
    temperatura = ingresar_temperatura()
    temperaturas.append(temperatura)

# Calcular promedio semanal
promedio_semanal = calcular_promedio_semanal(temperaturas)

print(f"Promedio semanal: {promedio_semanal:.2f} grados Celsius")