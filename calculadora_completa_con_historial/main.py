import historial
from matematicas.basicas import *
from matematicas.porcentajes import calcular_porcentaje as cp
from matematicas.geometria.areas import area_rectangulo as ar, area_circulo as ac


def ingresar_valores_para_operar(ac=False):
    
    msj = 'Ingrese un valor a operar: '
    msj_siguiente = 'Ingrese el siguiente valor a operar: '

    if ac:
        msj = 'Ingrese el radio de la circunferencia: '
        valor1 = float(input(msj))
        return valor1

    valor1 = float(input(msj))
    valor2 = float(input(msj_siguiente))

    return valor1, valor2


def menu():
    while True:
        print(''' -- Menu --

    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Porcentaje
    6. Area Rectangulo
    7. Area Circulo
    8. Mostrar historial
    9. Salir

    -----------------------
    ''')
        opcion_elegida = input('Ingrese una opcion: ')
        match opcion_elegida:
            case '1':
                valor1, valor2 = ingresar_valores_para_operar()
                resultado = sumar(valor1, valor2)
                print(resultado)
                historial.agregar_a_historial(valor1, valor2, operacion='Suma', resultado=resultado)
            
            case '2':
                valor1, valor2 = ingresar_valores_para_operar()
                resultado = restar(valor1, valor2)
                print(resultado)
                historial.agregar_a_historial(valor1, valor2, operacion='Resta', resultado=resultado)
            
            case '3':
                valor1, valor2 = ingresar_valores_para_operar()
                resultado = multiplicar(valor1, valor2)
                print(resultado)
                historial.agregar_a_historial(valor1, valor2, operacion='multiplicacion', resultado=resultado)
            
            case '4':
                valor1, valor2 = ingresar_valores_para_operar()
                resultado = dividir(valor1, valor2)
                print(resultado)
                historial.agregar_a_historial(valor1, valor2, operacion='Division', resultado=resultado)
            
            case '5':
                valor1, valor2 = ingresar_valores_para_operar()
                resultado = cp(valor1, valor2)
                print(resultado)
                historial.agregar_a_historial(valor1, valor2, operacion='Porcentaje', resultado=resultado)
            
            case '6':
                valor1, valor2 = ingresar_valores_para_operar()
                resultado = ar(valor1, valor2)
                print(resultado)
                historial.agregar_a_historial(valor1, valor2, operacion='Area del rectangulo', resultado=resultado)
            case '7':
                valor1 = ingresar_valores_para_operar(ac=True)
                resultado = ac(valor1)
                print(resultado)
                historial.agregar_a_historial(valor1, operacion='Area del circulo', resultado=resultado)
            case '8':
                historial.listar_operaciones()
            case '9':
                print('Adios...')
                break
            case _:
                print('Ingreso una opcion invalida. Vuelva a intentarlo.')
                
menu()