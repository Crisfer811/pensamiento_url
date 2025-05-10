#ejercicio 1
class ExperimentoFisico:
    def realizar_experimento(self):
        print("Este método debe ser implementado en una subclase.")
        return None

class CaidaLibre(ExperimentoFisico):
    def __init__(self, altura, gravedad=9.81):
        self.altura = altura
        self.gravedad = gravedad

    def realizar_experimento(self):
        if self.altura < 0:
            print("Error: la altura no puede ser negativa.")
            return None
        if self.gravedad == 0:
            print("Error: la gravedad no puede ser cero.")
            return None
        tiempo = (2 * self.altura / self.gravedad) ** 0.5
        return tiempo

  #ejercicio 2
  class OperacionCientifica:
    def calcular(self):
        print("Este método debe ser implementado en una subclase.")
        return None

class RaizCuadrada(OperacionCientifica):
    def __init__(self, numero):
        self.numero = numero

    def calcular(self):
        if self.numero < 0:
            print("Error: raíz cuadrada de número negativo no permitida.")
            return None
        return self.numero ** 0.5

class Potencia(OperacionCientifica):
    def __init__(self, base, exponente):
        self.base = base
        self.exponente = exponente

    def calcular(self):
        return self.base ** self.exponente

class Logaritmo(OperacionCientifica):
    def __init__(self, numero, base=2.71828):
        self.numero = numero
        self.base = base

    def calcular(self):
        if self.numero <= 0:
            print("Error: el logaritmo solo se calcula para números positivos.")
            return None
        if self.base <= 0 or self.base == 1:
            print("Error: la base del logaritmo debe ser positiva y distinta de 1.")
            return None
        return self.ln(self.numero) / self.ln(self.base)

    def ln(self, x):
        n = 100  # precisión
        x = (x - 1) / (x + 1)
        suma = 0
        for i in range(1, 2 * n, 2):
            suma += (x ** i) / i
        return 2 * suma

class Factorial(OperacionCientifica):
    def __init__(self, numero):
        self.numero = numero

    def calcular(self):
        if self.numero < 0 or int(self.numero) != self.numero:
            print("Error: el factorial solo se calcula para enteros no negativos.")
            return None
        resultado = 1
        for i in range(1, int(self.numero) + 1):
            resultado *= i
        return resultado
