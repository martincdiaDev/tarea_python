# Martin Forissi
# forissimartin@gmail.com
# Tarea 2_2

from math import pi

class Forma:
    def __init__(self, nombre: str) -> None:
        self.__nombre = nombre

    def get_nombre(self) -> str: 
        return self.__nombre
    
    def set_nombre(self, nombre: str) -> None:
        self.__nombre = nombre

    def calcular_area(self) -> float:
        pass
    
    def calcular_perimetro(self) -> float:
        pass
    
class Circulo(Forma):
    def __init__(self, radio: float) -> None:
        super().__init__("Círculo") # Nombre de la forma
        self.__radio = radio

    def calcular_area(self) -> float:
        return pi * (self.__radio ** 2)

    def calcular_perimetro(self) -> float:
        return 2 * pi * self.__radio
    
class Rectangulo(Forma):
    def __init__(self, alto: float, ancho: float) -> None:
        super().__init__("Rectángulo") # Nombre de la forma
        self.__ancho = ancho
        self.__alto = alto

    def calcular_area(self) -> float:
        return self.__ancho * self.__alto
    
    def calcular_perimetro(self) -> float:
        return 2 * (self.__ancho + self.__alto)
    
if __name__ == "__main__":

    formas = [Circulo(5), Rectangulo(4, 6)]
    
    for forma in formas:
        print(f'El área del {forma.get_nombre()} es: {forma.calcular_area()}')
        print(f'El perímetro del {forma.get_nombre()} es: {forma.calcular_perimetro()}')
        print()
