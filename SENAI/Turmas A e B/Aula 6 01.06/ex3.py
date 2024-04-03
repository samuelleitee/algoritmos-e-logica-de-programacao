# import math

# class Figura:
    
#     def __init__(self, x1, y1, x2, y2):
#         self.x1=x1
#         self.x2=x2
#         self.y1=y1
#         self.y2=y2
        
#     def distancia(self, x1, y1, x2=0, y2=0):
#         return math.sqrt((x1-x2)**2+(y1-y2)**2)

# class Circulo (Figura):
    
#     def __init__(self, x1, y1, x2, y2):
#         self.x1=x1
#         self.x2=x2
#         self.y1=y1
#         self.y2=y2    
    
#     def calcArea(self):
#         self.dist = self.distancia(self.x1, self.y1, self.x2, self.y2)
#         self.area = math.pi * (self.dist**2)
#         return self.area
    
#     def calcPerimetro(self):
#         self.dist = self.distancia(self.x1, self.y1, self.x2, self.y2)
#         self.perimetro = 2 * math.pi * self.dist
#         return self.perimetro
    
# class Retangulo(Figura):
    
#     def __init__(self, x1, y1, x2, y2):
#         self.x1=x1
#         self.x2=x2
#         self.y1=y1
#         self.y2=y2
    
#     def calcArea1 (self):
#         self.base = self.x2-self.x1
#         self.altura = self.y2-self.y1  
#         self.area=self.base*self.altura
#         return self.area
    
#     def calcArea (self):
#         return self.calcArea1()
    
#     def calcPerimetro(self):
#         return (2*self.distancia(self.x1, self.x2))+(2*self.distancia(self.y1, self.y2))
    
# class Triangulo (Retangulo):
    
#     def __init__(self, x1, y1, x2, y2):
#         self.x1=x1
#         self.x2=x2
#         self.y1=y1
#         self.y2=y2
    
#     def calcArea (self):
#         return self.calcArea1()/2
    
#     def calcPerimetro(self):
#         return self.distancia(self.x1, self.x2)+self.distancia(self.y1, self.y2)+self.distancia(self.x1, self.y1, self.x2, self.y2)

class FormaGeometrica:
    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * self.raio ** 2

    def calcular_perimetro(self):
        return 2 * 3.14 * self.raio

class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

class Triangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return 0.5 * self.base * self.altura

    def calcular_perimetro(self):
        return self.base + self.altura + (self.base ** 2 + self.altura ** 2) ** 0.5

def calcular_area_total(formas):
    area_total = 0
    for forma in formas:
        area_total += forma.calcular_area()
    return area_total

# Exemplo de uso:
formas = [Circulo(5), Quadrado(3), Triangulo(4, 6)]
area_total = calcular_area_total(formas)
print(area_total)  # Saída: 77.85