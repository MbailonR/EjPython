"""*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
 """

class Poligono:
    def __init__(self, numeroLados):
        self.numeroLados = numeroLados

class Cuadrado(Poligono):
    def __init__(self, lado):
        super().__init__(4)
        self.lado = lado

class Triangulo(Poligono):
    def __init__(self, base, altura):
        super().__init__(3)
        self.base = base
        self.altura = altura

class Rectangulo(Poligono):
    def __init__(self, base, altura):
        super().__init__(4)
        self.base = base
        self.altura = altura

def calcularAreaPoligono(poligono):
    if isinstance(poligono, Cuadrado):
        area = poligono.lado * poligono.lado
        return area

    elif isinstance(poligono, Triangulo):
        area = (poligono.base * poligono.altura) / 2
        return area

    elif isinstance(poligono, Rectangulo):
        area = poligono.base * poligono.altura
        return area


cuadrado = Cuadrado(4)
triangulo = Triangulo(5, 8)
rectangulo = Rectangulo(6, 3)

print(f"Área del cuadrado: {calcularAreaPoligono(cuadrado)}")
print(f"Área del triángulo: {calcularAreaPoligono(triangulo)}")
print(f"Área del rectángulo: {calcularAreaPoligono(rectangulo)}")