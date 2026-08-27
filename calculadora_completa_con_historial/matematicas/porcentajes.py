# matematicas/porcentajes.py

def calcular_porcentaje(valor, porcentaje):
    return valor * porcentaje / 100


def aplicar_descuento(precio, porcentaje_descuento):
    descuento = calcular_porcentaje(precio, porcentaje_descuento)
    return precio - descuento