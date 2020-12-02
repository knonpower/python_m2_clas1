
from math import pi

def area_circulo(radio):
    Area = pi * radio ** 2
    return Area
    
def perimetro_circulo(diametro):
    p_circulo = pi * diametro
    return p_circulo

def area_triangulo(base, altura):
    a_triangulo = (base * altura) / 2
    return a_triangulo

    
def perimetro_triangulo(a, b , c):
    p_triangulo = (a+ b + c)
    return p_triangulo

def area_rectangulo(base,altura):
    a_rectangulo = base * altura
    return a_rectangulo

def perimetro_rectangulo(base, altura):
    p_rectangulo = base + base + altura + altura
    return p_rectangulo

def distancia_recorrida(t,v):
    d_recorrida = t / v
    return d_recorrida    