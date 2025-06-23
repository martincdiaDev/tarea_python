# Martin Forissi
# forissimartin@gmail.com
# Tarea 2_1

class Animal:
    def __init__(self, nombre: str, edad: int, raza: str) -> None:
        self.__nombre = nombre
        self.__edad = edad 
        self.__raza = raza

    def get_nombre(self) -> str:
        return self.__nombre
    
    def get_edad(self) -> int:
        return self.__edad
    
    def get_raza(self) -> str:
        return self.__raza

    def set_nombre(self, nombre: str) -> None:
        self.__nombre = nombre

    def set_edad(self, edad: int) -> None:
        self.__edad = edad

    def set_raza(self, raza: str) -> None:
        self.__raza = raza

    def hacer_sonido(self) -> str:
        return "El animal hace un sonido"

    def comer(self) -> str:
        return "El animal está comiendo."

class Perro(Animal):
    def __init__(self, nombre: str, edad: int) -> None:
        super().__init__(nombre, edad, "Perro")

    def hacer_sonido(self) -> str:
        return "¡Guau guau!"

class Gato(Animal):
    def __init__(self, nombre: str, edad: int) -> None:
        super().__init__(nombre, edad, "Gato")

    def hacer_sonido(self) -> str:
        return "¡Miau miau!"

# Ejemplo de uso
if __name__ == "__main__":
    
    animales = [Gato("Michi", 2), Perro("Mia", 10)]

    for animal in animales:
        print(f'El {animal.get_raza()} de nombre {animal.get_nombre()} tiene {animal.get_edad()} años')
        print(animal.comer())
        print(f'El {animal.get_raza()} hace {animal.hacer_sonido()}')
        print()
