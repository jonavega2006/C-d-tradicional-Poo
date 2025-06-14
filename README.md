# Comparación: Programación Tradicional vs Programación Orientada a Objetos (POO) en Python

Este repositorio contiene dos implementaciones en Python para calcular el promedio semanal de las temperaturas:

* **Programación Tradicional** (`promedio_tradicional.py`)
* **Programación Orientada a Objetos (POO)** (`promedio_poo.py`)

---

## 1. Programación Tradicional

**Archivo:** `promedio_tradicional.py`

**Descripción:**

* Utiliza un enfoque estructurado mediante funciones.
* Se organiza en tres bloques principales:

  1. **Ingreso de datos** (`ingresar_temperaturas`): solicita al usuario las temperaturas de los 7 días y las guarda en una lista.
  2. **Procesamiento** (`calcular_promedio`): recibe la lista de temperaturas, suma sus valores y calcula el promedio.
  3. **Salida de resultados** (`main`): controla el flujo del programa (entrada → proceso → salida) e imprime el promedio con formato.

**Ventajas:**

* Código sencillo y fácil de seguir para problemas con lógica lineal.
* Ideal para quienes están iniciando en programación.

**Estructura del Código:**

```python
def ingresar_temperaturas():  # Entrada de datos
    ...

def calcular_promedio(temperaturas):  # Lógica de cálculo
    ...

def main():  # Control de flujo
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(...)

main()  # Punto de entrada
```

---

## 2. Programación Orientada a Objetos (POO)

**Archivo:** `promedio_poo.py`

**Descripción:**

* Aplica los tres pilares fundamentales de la POO:

  * **Encapsulamiento:** el atributo `__temperaturas` se mantiene privado dentro de la clase base `ClimaSemanal`.
  * **Herencia:** la clase `ClimaConComentario` hereda de `ClimaSemanal`, reutilizando métodos e identidad.
  * **Polimorfismo:** `ClimaConComentario` redefine (`override`) el método `mostrar_promedio` para añadir comentarios al resultado.
* Se complementa con una función externa `comentar_clima` que provee una observación según el promedio.

**Estructura del Código:**

```python
class ClimaSemanal:  # Clase base
    def __init__(self):
        self.__temperaturas = []  # Encapsulamiento
    def ingresar_temperaturas(self):
        ...
    def calcular_promedio(self):
        ...
    def mostrar_promedio(self):
        ...  # Método puede ser sobrescrito

class ClimaConComentario(ClimaSemanal):  # Herencia + Polimorfismo
    def mostrar_promedio(self):
        ...  # Redefinición para agregar comentario


def main():
    clima = ClimaConComentario()
    clima.ingresar_temperaturas()
    clima.mostrar_promedio()

main()  # Punto de entrada
```

**Ventajas:**

* Promueve la reutilización y extensibilidad del código.
* Separa de forma clara la gestión de datos (temperaturas) y la lógica de presentación.
* Facilita la incorporación de nuevas funcionalidades mediante herencia y polimorfismo.

---

## Cómo usar este repositorio

1. Clona el repositorio en tu máquina local:

   ```bash
   git clone <URL-del-repositorio>
   ```
2. Navega a la carpeta del proyecto:

   ```bash
   cd Cód-tradicional-Poo
   ```
3. Ejecuta cada script según el paradigma:

   * Tradicional:

     ```bash
     python3 Cod-tradicional,py
     ```
   * Orientado objetos:

     ```bash
     python3 Cod-Programacion-Poo.py
     ```

---

## Conclusión
Este ejemplo muestra cómo abordar el mismo problema (cálculo de promedio semanal de temperatura) usando dos paradigmas distintos. La programación tradicional es directa y fácil de entender para tareas pequeñas, mientras que la POO aporta estructuras más flexibles y mantenibles para proyectos de mayor envergadura.

Gracias
