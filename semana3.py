# Operadores


## Aritmeticos

### Suma
suma = 2 + 2

### Resta
resta = 2 - 2

### Multiplicacion
multiplicacion = 2 * 2

### Potencia
potencia = 2 ** 2

### Division
division = 5 / 3

### Division Entera
division_entera = 5 // 3

### Modulo
modulo = 5 % 3

# print('Suma 2 + 2:', suma)
# print('Resta 2 - 2:', resta)
# print('Multiplicacion 2 * 2:', multiplicacion)
# print('Potencia 2 ** 2:', potencia)
# print('Division 5 / 3:', division)
# print('Division Entera 5 // 3:', division_entera)
# print('Modulo 5 % 3:', modulo)
# print()
# print('5 % 3.0:', 5 % 3.0)
# print('5.0 % 3:', 5.0 % 3)
# print('5.0 / 3:', 5.0 / 3)
# print('5 / 3.0:', 5 / 3.0)
# print('5.0 // 3:', 5.0 // 3)
# print('5 // 3.0:', 5 // 3.0)
# print()


## Relacionales

# =======================================================
# Nota

# Existe el tipo de dato Boolean que maneja los valores True (verdadero) y False (falso). 
# Estos valores tambien son considerados en python como 1 y 0 y tambien pueden ser considerados con los nombres de binarios, logicos, etc...
# =======================================================

### Mayor que
mayor_que = 2 > 2

### Menor que
menor_que = 2 < 2

### Mayor o igual que
mayor_o_igual_que = 2 >= 2 # > =

### Menor o igual que
menor_o_igual_que = 2 <= 2 # < =

### Igualdad
igualdad = 5 == 3

### Desigualdad
desigualdad = 5 != 3 # ! =

# print('Mayor que 2 > 2:', mayor_que)
# print('Menor que 2 < 2:', menor_que)
# print('Mayor o igual que 2 >= 2:', mayor_o_igual_que)
# print('Menor o igual que 2 <= 2:', menor_o_igual_que)
# print('Igualdad 5 == 3:', igualdad)
# print('Desigualdad 5 != 3:', desigualdad)
# print()
# print('"pepe" == "casa":', "pepe" == "casa")
# print('"pepe" != "casa":', "pepe" != "casa")
# print('"pepe" > "casa":', "pepe" > "casa")
# print('"pepe" < "casa":', "pepe" < "casa")
# print('"A" < "a":', "A" < "a")
# print("'ahorrar' < 'aHorrar':", 'ahorrar' < 'aHorrar')
# print("'ah' < 'aHorrar':", 'ah' < 'aHorrar')
# print("'ah' > 'ahorrar':", 'ah' > 'ahorrar')
# print("'ah' < 'ahorraR':", 'ah' < 'ahorraR')
# print("'a' >= 'ahorrar':", 'a' >= 'ahorrar')
# print()

# =======================================================
# Nota

# https://elcodigoascii.com.ar/

# Python utiliza por detras de los caracteres valores que los representan.
# chr() -> brinda gracias a un numero su representacion en caracter
# ord() -> brinda gracias a un caracter su representacion numerica

# print('ord("r"): ', ord("r"))
# print('chr(97): ', chr(97))

# =======================================================


## Logicos

### and
"pepe" == "casa" and 5 != 3
#  False         and  True
#         False

# True and True    ----> True
# False and True   ----> False
# True and False   ----> False
# False and False  ----> False

# 4/0
# 4/0 and True
# True and 4/0
# 4/0 and False
# False and 4/0


### or
"pepe" == "casa" or 5 != 3
#  False         or  True
#         True


# True or True    ----> True  
# False or True   ----> True  
# True or False   ----> True  
# False or False  ----> False 

# 4/0
# 4/0 or True
# True or 4/0
# 4/0 or False
# False or 4/0

### not

# print(4)
# print(bool(4))
# print(not 4)
# print(not bool(4))

###########################################################################################################
###########################################################################################################
###########################################################################################################

# if

# if concdicion:
#      copdigo


# if 4:
#     print('hola')

# dato = input('Esta lloviendo? (si / no)')
# if dato == 'si':
#     print('UUUUy, que mal clima')
# elif dato == 'no':
#     print('Que bueno!')
# elif dato == 'no':
#     print('Que bueno!')
# elif dato == 'no':
#     print('Que bueno!')
# elif dato == 'no':
#     print('Que bueno!')
# elif dato == 'no':
#     print('Que bueno!')
# else:
#     print('le erraste en el codigo.')


########################################################################

# operacion = input('''Ingrese la operacion a realizar (suma/resta/multiplicacion/division): ''')

# valor1 = int(input('Ingrese el primer valor a operar: '))
# valor2 = int(input('Ingrese el segundo valor a operar: '))

# if operacion == 'suma':
#     print(valor1 + valor2)
# elif operacion == 'resta':
#     print(valor1 - valor2)
# elif operacion == 'multiplicacion':
#     print(valor1 * valor2)
# elif operacion == 'division':
#     print(valor1 / valor2)
# else:
#     print('No se esta ingresando una operacion valida para la calculadora.')

########################################################################


# def calculadora():
#     try:
#         operacion = input('''Ingrese la operacion a realizar (suma/restar/multiplicar/dividir)\n''').lower()
#         valor1 = int(input('Ingrese el primer valor\n'))
#         valor2 = int(input('Ingrese el segundo valor\n'))

#         if operacion == 'suma':
#             print(valor1 + valor2)
#         elif operacion == 'resta':
#             print(valor1 - valor2)
#         elif operacion == 'multiplicar':
#             print(valor1 * valor2)
#         elif operacion == 'dividir':
#             print(valor1 // valor2)
#         else:
#             print('No se esta ingresando una operacion valida para la calculadora.')
#     except KeyboardInterrupt:
#         print('Operacion Cancelada')
#     except ZeroDivisionError:
#         print('No se Puede Dividir por 0')
#     except ValueError:
#         print('Valor introducido no valido')
#     except Exception:
#         print('Hubo un error no capturado')
        
# calculadora()


########################################################################

# def suma(valor1, valor2):
#     return valor1 + valor2

# def resta(valor1, valor2):
#     return valor1 - valor2

# def multiplicacion(valor1, valor2):
#     return valor1 * valor2

# def division(valor1, valor2):
#     return valor1 / valor2

# operacion = input('''Ingrese la operacion a realizar (suma/resta/multiplicacion/division): ''')

# try:
#     valor1 = int(input('Ingrese el primer valor a operar: '))
#     valor2 = int(input('Ingrese el segundo valor a operar: '))
    
#     if operacion == 'suma':
#         print(suma(valor1, valor2))
#     elif operacion == 'resta':
#         print(resta(valor1, valor2))
#     elif operacion == 'multiplicacion':
#         print(multiplicacion(valor1, valor2))
#     elif operacion == 'division':
#         print(division(valor1, valor2))
#     else:
#         print('No se esta ingresando una operacion valida para la calculadora.')

# except Exception as e:
#     print(f'Ocurrio un error no controlado. {e}')


# ########################################################################


