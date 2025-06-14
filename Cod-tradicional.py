# promedio_tradicional.py
# Programa en estilo tradicional para calcular el promedio semanal de temperatura
# Utiliza funciones para estructurar el flujo del programa
# ---------------------------------------------
# FUNCIÓN: ingresar_temperaturas
# Solicita al usuario que ingrese la temperatura de cada uno de los 7 días de la semana.
# Devuelve una lista con todas las temperaturas ingresadas.
# ---------------------------------------------
def ingresar_temperaturas():
    temperaturas = []  # Lista vacía para guardar las temperaturas diarias
    print("Ingrese las temperaturas de los 7 días:")
    for dia in range(1, 8):  # Bucle del día 1 al 7 (inclusive)
        temp = float(input(f"Día {dia}: "))  # Lee la temperatura como número decimal
        temperaturas.append(temp)  # Agrega la temperatura a la lista
    return temperaturas  # Devuelve la lista completa
# ---------------------------------------------
# FUNCIÓN: calcular_promedio
# Calcula el promedio de una lista de temperaturas recibida como parámetro.
# ---------------------------------------------
def calcular_promedio(temperaturas):
    suma = sum(temperaturas)  # Suma todas las temperaturas
    promedio = suma / len(temperaturas)  # Calcula el promedio (suma / cantidad de elementos)
    return promedio  # Devuelve el promedio calculado
# ---------------------------------------------
# FUNCIÓN PRINCIPAL: main
# Controla el flujo general del programa: entrada, proceso y salida.
# ---------------------------------------------
def main():
    print("== PROMEDIO SEMANAL DEL CLIMA ==")
    # Paso 1: Ingreso de temperaturas
    temperaturas = ingresar_temperaturas()
    # Paso 2: Cálculo del promedio
    promedio = calcular_promedio(temperaturas)
    # Paso 3: Mostrar resultado
    print(f"El promedio de la semana es: {promedio:.2f}°C")
# ---------------------------------------------
# PUNTO DE ENTRADA DEL PROGRAMA
# Llama a la función principal para ejecutar el programa completo.
# ---------------------------------------------
main()
