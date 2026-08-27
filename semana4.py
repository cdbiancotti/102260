'hola don pepito'

# print(len('hola don pepito'))

# for caracter in 'hola don pepito':
#     contador = 0
#     contador += 1

# print(contador)


# contador = 0
# for _ in 'hola don pepito':
#     contador += 1

# print(contador)

#######################################################################################################
#######################################################################################################


# def mi_len():
#     contador = 0
#     for _ in 'soy un bizcochito':
#         contador += 1

#     print(contador)
    

# print(len('hola don pepito'))
# print(len('soy un bizcochito'))
# mi_len()
# mi_len()


#######################################################################################################
#######################################################################################################

# def mi_len(texto):
#     contador = 0
#     for _ in texto:
#         contador += 1

#     print(contador)
    

# print(len('hola don pepito'))
# print(len('soy un bizcochito'))
# mi_len('hola don pepito')
# mi_len('soy un bizcochito')

#######################################################################################################
#######################################################################################################

# def mi_len(texto):
#     '''Esta funcion es un reemplazo manual de lo que hace len.'''
#     contador = 0
#     for _ in texto:
#         contador += 1

#     return contador
    

# # print(len('hola don pepito'))
# # print(len('soy un bizcochito'))
# # mi_len('hola don pepito')
# # mi_len('soy un bizcochito')
# # print(mi_len('hola don pepito'))
# print(mi_len('soy un bizcochito'))

#######################################################################################################
#######################################################################################################

# definicion
# def nombre_de_la_funcion(parametro, parametro2, *args, **kwargs):
#     ...
#     ...
#     ...
#     ...
#     ...
#     ...
#     ...
#     ...
#     ...
#     ...
#     return ...
    
# # llamada
# nombre_de_la_funcion(1,True,'pepito')

#######################################################################################################
#######################################################################################################


# # dato = input('Esta lloviendo? (si / no)')

# def comentario_del_clima():
#     if dato == 'si':
#         print('UUUUy, que mal clima')
#     elif dato == 'no':
#         print('Que bueno!')
#     else:
#         print('le erraste en el codigo.')
    
# # dato = input('Esta lloviendo? (si / no)')

# comentario_del_clima()

# dato = input('Esta lloviendo? (si / no)')

#######################################################################################################
#######################################################################################################


# dato = input('Esta lloviendo? (si / no)')

# def comentario_del_clima(esta_lloviendo):
#     if esta_lloviendo == 'si':
#         print('UUUUy, que mal clima')
#     elif esta_lloviendo == 'no':
#         print('Que bueno!')
#     else:
#         print('le erraste en el codigo.')
        
# dato = input('Esta lloviendo? (si / no)')
# comentario_del_clima(dato)

#######################################################################################################
#######################################################################################################


# def comentario_del_clima(esta_lloviendo):
#     if esta_lloviendo == 'si':
#         return 'UUUUy, que mal clima'
#     elif esta_lloviendo == 'no':
#         return 'Que bueno!'

#     return 'le erraste en el codigo.'
        
#     return
#     return None
#     # # return None
        
# dato = input('Esta lloviendo? (si / no)')

# print(comentario_del_clima(dato))

#######################################################################################################
#######################################################################################################
    
# def comentario_del_clima(esta_lloviendo):
#     # if esta_lloviendo == 'si':
#     #     return 'UUUUy, que mal clima'
#     # elif esta_lloviendo == 'no':
#     #     return 'Que bueno!'

#     # return 'le erraste en el codigo.'

#     while True:    
#         if esta_lloviendo == 'si':
#             # return 'UUUUy, que mal clima'
#             break
#         esta_lloviendo = input('Esta lloviendo? (si / no)')
#         print('no llueve que lindo...')
#     esta_lloviendo = input('Esta lloviendo? (si / no)')
#     print('no llueve que lindo...')
    
# dato = input('Esta lloviendo? (si / no)')

# print(comentario_del_clima(dato))

#######################################################################################################
#######################################################################################################

# # def mostrar_datos(param1=1, param2, param3, param4, param5=55555, param6=666666):
# def mostrar_datos(param1, param2, param3, param4, param5=55555, param6=666666):
#     print(param1, param2, param3, param4, param5, param6)
    
# # mostrar_datos(1, 22, 333, 4444, 55555, 666666)
# # mostrar_datos(22, 1, 333, 4444, 55555, 666666)
# # mostrar_datos(param2=22, param1=1, param3=333, param4=4444, param5=55555, param6=666666)
# # # mostrar_datos(param2=22, param1=1, 333, 4444, 55555, 666666)
# # mostrar_datos(1, 22, 333, param6=666666, param5=55555, param4=4444)


# mostrar_datos(1, 22, 333, 4444, 55555, 12341233123123)
# mostrar_datos(1, 22, 333, 4444, 55555)
# mostrar_datos(1, 22, 333, 4444, 12341233123123)
# mostrar_datos(1, 22, 333, 4444)
# mostrar_datos(1, 22, 333, 12341233123123)

#######################################################################################################
#######################################################################################################

# def comentario_del_clima():
#     '''alguna definicion'''
#     # pass
#     # ...
    
# var = ...

# print(var)
# print(type(...))


#######################################################################################################
#######################################################################################################
# variable = 'a                    hola don pepito a a a a aaaaaaaa a a a a aaaa a a a       aaa'

# print(variable)
# print(variable.strip())
# print(variable.strip(' a'))

#######################################################################################################
#######################################################################################################

# Sintaticos

# print('hola)
# if True
#     print('pepe')

# Semanticos
# var = 4/0

#######################################################################################################
#######################################################################################################

# https://docs.python.org/es/3/library/exceptions.html#exception-hierarchyc

# var1 = int(input('Ingrese un valor: '))
# var2 = int(input('Ingrese otro valor: '))

# if var2 != 0:
#     print(var1/var2)
# else:
#     print('Ingresaste como segundo valor un 0 y no se puede dividir por 0.')
    
# try - except

# try:
#     ...
# except:    
#     ...

# try:
#     var1 = int(input('Ingrese un valor: '))
#     var2 = int(input('Ingrese otro valor: '))

#     if var2 != 0:
#         print(var1/var2)
#     else:
#         print('Ingresaste como segundo valor un 0 y no se puede dividir por 0.')
# except:
#     print('Mira, ingresaste un valor erroneo... fijate que sea numerico.')


#######################################################################################################
#######################################################################################################

# try:
#     var1 = int(input('Ingrese un valor: '))
#     var2 = int(input('Ingrese otro valor: '))

#     print(var1/var2)
#     # print('Ingresaste como segundo valor un 0 y no se puede dividir por 0.')
# except:
#     # print('Mira, ingresaste un valor erroneo... fijate que sea numerico.')
#     print('Mira, ingresaste un valor erroneo...')


# try:
#     var1 = int(input('Ingrese un valor: '))
#     var2 = int(input('Ingrese otro valor: '))

#     print(var1/var2)

# except ZeroDivisionError:
#     print('Ingresaste como segundo valor un 0 y no se puede dividir por 0.')
#     # print('Mira, ingresaste un valor erroneo... fijate que sea numerico.')
#     # print('Mira, ingresaste un valor erroneo...')
# except ArithmeticError:
#     print('Mira, ingresaste un valor erroneo...')
# except ValueError:
#     # print('Ingresaste como segundo valor un 0 y no se puede dividir por 0.')
#     print('Mira, ingresaste un valor erroneo... fijate que sea numerico.')
#     # print('Mira, ingresaste un valor erroneo...')
# except:
#     print('Ocurrio un error no controlado.')

#######################################################################################################
#######################################################################################################

# try:
#     var1 = int(input('Ingrese un valor: '))
#     var2 = int(input('Ingrese otro valor: '))

#     print(var1/var2)

# except ZeroDivisionError:
#     print('Ingresaste como segundo valor un 0 y no se puede dividir por 0.')
# except ArithmeticError:
#     print('Mira, ingresaste un valor erroneo...')
# except ValueError:
#     print('Mira, ingresaste un valor erroneo... fijate que sea numerico.')
# except Exception:
#     print('Ocurrio un error no controlado.')

#######################################################################################################
#######################################################################################################

# try:
#     var1 = int(input('Ingrese un valor: '))
#     var2 = int(input('Ingrese otro valor: '))

#     print(var1/var2)

# # except ZeroDivisionError as e:
# #     print('Ingresaste como segundo valor un 0 y no se puede dividir por 0.')
# # except ArithmeticError as e:
# #     print('Mira, ingresaste un valor erroneo...')
# # except ValueError as e:
# #     print('Mira, ingresaste un valor erroneo... fijate que sea numerico.')
# except Exception as e:
#     print('Ocurrio un error no validado.', type(e).__name__, e)

#######################################################################################################
#######################################################################################################


# try:
#     var1 = int(input('Ingrese un valor: '))
#     var2 = int(input('Ingrese otro valor: '))

#     print(var1/var2)

# except ZeroDivisionError as e:
#     print('Ingresaste como segundo valor un 0 y no se puede dividir por 0.')
# except ArithmeticError as e:
#     print('Mira, ingresaste un valor erroneo...')
# except ValueError as e:
#     print('Mira, ingresaste un valor erroneo... fijate que sea numerico.')
# except Exception as e:
#     print('Ocurrio un error no validado.', type(e).__name__, e)
# else:
#     print('Pase por el else')
# finally:
#     print('Pase por el finally')


# print('Pase por el finally')

#######################################################################################################
#######################################################################################################

# def mi_funcion():
#     try:
#         var1 = int(input('Ingrese un valor: '))
#         var2 = int(input('Ingrese otro valor: '))

#         return var1/var2
    
#     except Exception as e:
#         return f'Ocurrio un error no validado. {type(e).__name__} {e}'
#     finally:
#         print('Pase por el finally')

# print(mi_funcion())


#######################################################################################################
#######################################################################################################

def mi_funcion():
    try:
        var1 = int(input('Ingrese un valor: '))
        var2 = int(input('Ingrese otro valor: '))

        return var1/var2
    finally:
        print('Pase por el finally')

print(mi_funcion())

#######################################################################################################
#######################################################################################################

# def mi_funcion():
#     try:
#         var1 = int(input('Ingrese un valor: '))
#         var2 = int(input('Ingrese otro valor: '))

#         return var1/var2
#     finally:
#         print('Pase por el finally')


# try:
#     print(mi_funcion())
# except Exception as e:
#     print(f'Ocurrio un error no validado. {type(e).__name__} {e}')
    

# try:
#     try:
#         ...
#     except:
#         try:
#             ...
#         except:
#             ...
# except:
#     try:
#         try:
#             ...
#         except:
#             ...
#     except:
#         ...
        


# try:
#     try:
#         ...
#     finally:
#         ...
# except:
#     ...

#######################################################################################################
#######################################################################################################

# def pepito(nombre):
#     print('Hola, soy Pepito', nombre)


# def pepito2(otra_funcion):
#     otra_funcion('ricardo')
    
# pepito2(pepito)
# pepito2(lambda nombre: print('Hola, soy Pepito', nombre))
# pepito2(
#     lambda nombre: 
#         print('Hola, soy Pepito', nombre)
#         print('Hola, soy Pepito', nombre)
#         print('Hola, soy Pepito', nombre)
#         print('Hola, soy Pepito', nombre)
#         print('Hola, soy Pepito', nombre)
#         print('Hola, soy Pepito', nombre)
#         print('Hola, soy Pepito', nombre) 
# )



#######################################################################################################
#######################################################################################################
#######################################################################################################

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


