# matematicas/geometria/areas.py
from math import pi
from .validaciones import medida_valida


def area_rectangulo(base, altura):
    if not medida_valida(base) or not medida_valida(altura):
        return None
    return base * altura


def area_circulo(radio):
    if not medida_valida(radio):
        return None
    return pi * radio ** 2
