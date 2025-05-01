#ejercicio 1
class Animal:
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def mostrar_datos(self):
        print("Nombre:",self.nombre ,"Edad: ",self.edad , "Peso: ",self.peso,"kg")

    def calcular_dosis(self):
        print("Dosis estándar: Consultar al veterinario")

    def ficha_medica(self):
        self.mostrar_datos()
        self.calcular_dosis()

class Perro(Animal):
    def __init__(self, nombre, edad, peso, raza):
        super().__init__(nombre, edad, peso)
        self.raza = raza

    def calcular_dosis(self):
        dosis = self.peso * 0.5
        print("Dosis para perro: ", dosis ,"ml")

class Gato(Animal):
    def __init__(self, nombre, edad, peso, color):
        super().__init__(nombre, edad, peso)
        self.color = color

    def calcular_dosis(self):
        dosis = self.peso * 0.3
        print("Dosis para gato: ",dosis ,"ml")

class Ave(Animal):
    def __init__(self, nombre, edad, peso, tipo):
        super().__init__(nombre, edad, peso)
        self.tipo = tipo

    def calcular_dosis(self):
        dosis = self.peso * 0.1
        print("Dosis para ave: ",dosis ,"ml")

class Reptil(Animal):
    def __init__(self, nombre, edad, peso, habitat):
        super().__init__(nombre, edad, peso)
        self.habitat = habitat

    def calcular_dosis(self):
        dosis = self.peso * 0.2
        print("Dosis para reptil: ",dosis, "ml")

p = Perro("Firulais", 5, 20, "Labrador")
p.ficha_medica()






#ejercicio 2
class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrar_info(self):
        print("Nombre: ", self.nombre ,"Edad: ",self.edad , "DNI: ",self.dni)

class Estudiante(Persona):
    def __init__(self, nombre, edad, dni, carrera):
        super().__init__(nombre, edad, dni)
        self.carrera = carrera

    def mostrar_info(self):
        super().mostrar_info()
        print("Carrera: ",self.carrera)

class Profesor(Persona):
    def __init__(self, nombre, edad, dni, especialidad):
        super().__init__(nombre, edad, dni)
        self.especialidad = especialidad

    def mostrar_info(self):
        super().mostrar_info()
        print("Especialidad: ",self.especialidad)

class Administrativo(Persona):
    def __init__(self, nombre, edad, dni, departamento):
        super().__init__(nombre, edad, dni)
        self.departamento = departamento

    def mostrar_info(self):
        super().mostrar_info()
        print("Departamento: ",self.departamento)


e = Estudiante("Ana", 21, "123456789", "Ingeniería en Sistemas")
e.mostrar_info()
