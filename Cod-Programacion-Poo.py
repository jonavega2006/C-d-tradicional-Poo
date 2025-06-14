
# Programa usando Programación Orientada a Objetos (POO)
# para calcular el promedio semanal de temperatura.
# ------------------------------
# Clase base: ClimaSemanal
# ------------------------------
class ClimaSemanal:
    def __init__(self):
        # Encapsulamiento: Lista privada para almacenar temperaturas de la semana.
        self.__temperaturas = []
    def ingresar_temperaturas(self):
        # Método para pedir al usuario que ingrese 7 temperaturas, una por cada día.
        print("Ingrese las temperaturas de los 7 días:")
        for dia in range(1, 8):  # Recorre del día 1 al 7
            temp = float(input(f"Día {dia}: "))
            self.__temperaturas.append(temp)
    def calcular_promedio(self):
        # Método para calcular el promedio de temperaturas.
        if len(self.__temperaturas) == 0:
            return 0  # Evita división por cero
        return sum(self.__temperaturas) / len(self.__temperaturas)
    def mostrar_promedio(self):
        # Método que imprime el promedio calculado.
        # Este método podrá ser sobrescrito (polimorfismo).
        promedio = self.calcular_promedio()
        print(f"El promedio de la semana es: {promedio:.2f}°C")
# ------------------------------
# Función externa para comentarios según el clima
# (separada para mantener la lógica clara y modular)
# ------------------------------
def comentar_clima(promedio):
    # Función que da un comentario dependiendo del valor del promedio.
    if promedio >= 30:
        print("→ Semana muy calurosa.")
    elif promedio >= 20:
        print("→ Temperatura agradable.")
    else:
        print("→ Semana fría o fresca.")
# ------------------------------
# Clase derivada: ClimaConComentario
# Hereda de ClimaSemanal y aplica polimorfismo
# ------------------------------
class ClimaConComentario(ClimaSemanal):
    def __init__(self):
        # Llama al constructor de la clase base
        super().__init__()
    def mostrar_promedio(self):
        # Polimorfismo: se redefine el método de la clase base
        # para agregar un comentario adicional.
        promedio = self.calcular_promedio()
        print(f"El promedio semanal es: {promedio:.2f}°C")
        comentar_clima(promedio)  # Llama a la función que genera el comentario
# ------------------------------
# Función principal
# ------------------------------
def main():
    print("== PROMEDIO SEMANAL DEL CLIMA (POO) ==")
    # Creamos un objeto de la clase hija (usa herencia)
    clima = ClimaConComentario()
    # Se ingresan los datos a través del método heredado
    clima.ingresar_temperaturas()
    # Se muestra el promedio usando el método sobrescrito
    clima.mostrar_promedio()
# ------------------------------
# Ejecución del programa
# ------------------------------
main()
