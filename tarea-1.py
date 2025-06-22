from numbers import Number 

# EJERCICIO 1
class Animal:

    def __init__(self, raza: str, genero: str) -> None:
        self.raza = raza
        self.genero = genero

    def informacion(self) -> None:
        print(f'La raza es {self.raza} y el genero es {self.genero}')

animal1 = Animal('Perro', 'Macho')
animal1.informacion()
print(f'El animal {animal1.raza} es de genero {animal1.genero}')
print()

# EJERCICIO 2
class Coche:
    def __init__(self, marca: str) -> None:
        self.marca = marca

    def acelerar(self) -> None:
        print(f"El coche de marca {self.marca} esta acelerando...")

coche1 = Coche('Ford')
coche1.acelerar()
coche1.marca = 'Chevrolet'
coche1.acelerar()
print()

# EJERCICIO 3
class Calculadora:
    def __init__(self):
        self.resultado = 0

    def sumar(self, num1: Number, num2: Number) -> None:
        self.resultado = num1 + num2
        print(f'El resultado de la suma es: {self.resultado}')

    def restar(self, num1: Number, num2: Number) -> None:
        self.resultado = num1 - num2
        print(f'El resultado de la resta es: {self.resultado}')

calc = Calculadora()
calc.sumar(10, 15)
calc.restar(25, 20.7)