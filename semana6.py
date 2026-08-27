# # Trabajando con variables podriamos guardar datos sueltos como los siguientes y mostrarlos
# nombre = 'Juan'
# edad = 26

# print(nombre)
# print(edad)

# # Pero para crear mas cantidad con lo que sabemos tendrimos un monton de variables
# # nombre y edad, ademas de que no se relacionan entre si mas que por algo que
# # pongamos en el nombre de la variable

# nombre1 = 'Juan'
# edad1 = 26
# nombre2 = 'Pepe'
# edad2 = 21

# print(nombre1)
# print(edad1)
# print(nombre2)
# print(edad2)

# def sumar(a, b):
#     return a+b

# # entonces podriamos usar diccionarios y agruparlos un poco mas
# persona1 = {
#     'nombre': 'Juan',
#     'edad': 26
# }
# persona2 = {
#     'nombre': 'Pepe',
#     'edad': 21,
#     # 'operacion': sumar
#     'operacion': lambda a,b: a+b
# }

# print(persona1['nombre'])
# print(persona1['edad'])
# print(persona2['nombre'])
# print(persona2['edad'])
# print(persona2['operacion'](1,2))

# Pero si tiene mas datos o tenemos que crear varias personas mas serian un monton
# de lineas para cada persona. Y aca entra una clase (por lo menos un ejemplo
# simple y basico de mejora en relacion a todo lo que nos brindan las 56075)

# class Persona:
#     """
#     Esta es una clase donde se agregan todos los datos
#     respecto a una persona
#     """
#     def __init__(self, nombre, edad):
#         # Todo lo que definamos en __init__ se corre
#         # al crear una instancia de la clase
#         self.nombre = nombre
#         self.edad = edad

# #El parámetro self se refiere al objeto instanciado de esa clase sobre el cual se está invocando dicho método.
# #Link de Interes: https://ejemplos.net/que-significa-self-en-python/

# #Creamos un objeto persona1 que es una instancia de la clase Persona
# persona1 = Persona("Juan", 26)

# #Vemos el tipo de objeto que es persona1
# type(persona1)

# # Y si queremos crear a Pepe solo hariamos lo siguiente
# persona2 = Persona("pepe", 21)

# # Para acceder a los datos cambia de como lo haciamos con dicc
# print(persona1.nombre) #Le pedimos a persona1 su nombre
# print(persona1.edad) #Le pedimos a persona1 su edad
# print(persona2.nombre) #Le pedimos a p2 su nombre
# print(persona2.edad) #Le pedimos a p2 su edad

# ================================================================================
# ================================================================================

# UML

# ================================================================================
# ================================================================================

# class Auto:
#     ...
    
# auto1 = Auto()
# auto2 = Auto()

# print(auto1)
# print(auto2)

# ================================================================================
# ================================================================================

# class Auto:
    
#     @staticmethod
#     def tocar_bocina():
#         print('PIIIII PIIII!!')

#     def avanzar(self, metros):
#         print(f'El {self} avanzo {metros} mts')

#     @classmethod
#     def pasamos_el_minimo_de_produccion(cls):
#         ...

# auto1 = Auto()
# auto2 = Auto()

# print(auto1)
# auto1.tocar_bocina()
# auto1.avanzar(15)

# print(auto2)
# auto2.avanzar(15)
# ================================================================================
# ================================================================================

# class Auto:
    
#     def __init__(self):
#         self.marca = 'Ford'
#         self.modelo = 'K'
    
#     @staticmethod
#     def tocar_bocina():
#         print('PIIIII PIIII!!')

#     def avanzar(self, metros):
#         print(f'El {self} avanzo {metros} mts')
        
#     # def guardar_datos(self):
#     #     self.marca = 'Ford'
#     #     self.modelo = 'K'

#     @classmethod
#     def pasamos_el_minimo_de_produccion(cls):
#         ...

# auto1 = Auto()
# auto2 = Auto()

# print(auto1)
# auto1.tocar_bocina()
# auto1.avanzar(15)

# print(auto2)
# auto2.avanzar(15)

# # auto1.marca = 'Ford'
# # auto1.modelo = 'K'

# print(auto1)
# print(auto1.marca)
# print(auto1.modelo)

# ================================================================================
# ================================================================================

# class Auto:
    
#     cant_autos_creados = 0
    
#     def __init__(self, marca, modelo):
#         self.marca = marca
#         self.modelo = modelo
#         Auto.cant_autos_creados += 1
#         self.nro_chasis = Auto.cant_autos_creados
#         self.tocar_bocina()
    
#     def __str__(self):
#         return f'Soy un {self.marca} {self.modelo}'
    
#     @staticmethod
#     def tocar_bocina():
#         print('PIIIII PIIII!!')

#     def avanzar(self, metros):
#         print(f'El {self} avanzo {metros} mts')

#     @classmethod
#     def pasamos_el_minimo_de_produccion(cls):
#         return cls.cant_autos_creados > 5

# auto1 = Auto('Ford', 'K')
# auto2 = Auto('Fiat', 'Uno')
# auto3 = Auto('Fiat', 'Uno')
# auto4 = Auto('Fiat', 'Uno')
# auto5 = Auto('Fiat', 'Uno')
# # auto6 = Auto('Fiat', 'Uno')

# print(auto1)
# auto1.avanzar(15)
# print(auto1.marca)
# print(auto1.modelo)
# print(auto1.nro_chasis)
# print(auto1.cant_autos_creados)

# print(auto2)
# auto2.avanzar(15)
# print(auto2.marca)
# print(auto2.modelo)
# print(auto2.nro_chasis)
# print(auto2.cant_autos_creados)

# print(Auto.cant_autos_creados)
# print(Auto.pasamos_el_minimo_de_produccion())

# ================================================================================
# ================================================================================

# class Auto:
    
#     cant_autos_creados = 0
    
#     def __init__(self, marca, modelo):
#         self.marca = marca
#         self.modelo = modelo
#         Auto.cant_autos_creados += 1
#         self.__nro_chasis = Auto.cant_autos_creados
#         self.tocar_bocina()
    
#     def __str__(self):
#         return f'Soy un {self.marca} {self.modelo}'
    
#     @staticmethod
#     def tocar_bocina():
#         print('PIIIII PIIII!!')

#     def avanzar(self, metros):
#         print(f'El {self} avanzo {metros} mts')

#     @classmethod
#     def pasamos_el_minimo_de_produccion(cls):
#         return cls.cant_autos_creados > 5
    
#     def ver_nro_chasis(self, es_el_duenio):
#         if es_el_duenio:
#             return self.__nro_chasis

# auto1 = Auto('Ford', 'K')
# # print(auto1.__nro_chasis)
# # print(auto1._Auto__nro_chasis)
# print(auto1.ver_nro_chasis(True))
# print(auto1.ver_nro_chasis(False))

# ================================================================================
# ================================================================================

# https://www.seas.es/blog/informatica/agregacion-vs-composicion-en-diagramas-de-clases-uml/

# ================================================================================
# ================================================================================

# class Vehiculo:
    
#     sonido_bocina = ''
    
#     def avanzar(self, metros):
#         print(f'El {self} avanzo {metros} mts')
    
#     @classmethod
#     def tocar_bocina(cls):
#         print(f'{cls.sonido_bocina}!!')

# class Auto(Vehiculo):
    
#     sonido_bocina = 'PIIIII PIIII'
    
#     # @staticmethod
#     # def tocar_bocina():
#     #     print(f'{Auto.sonido_bocina}!!')

#     # def avanzar(self, metros):
#     #     print(f'El {self} avanzo {metros} mts')

# class Camion(Vehiculo):
    
#     sonido_bocina = 'CUAAAAA'
    
#     # @staticmethod
#     # def tocar_bocina():
#     #     print(f'{Camion.sonido_bocina}!!')

#     # def avanzar(self, metros):
#     #     print(f'El {self} avanzo {metros} mts')

# class Moto(Vehiculo):
    
#     sonido_bocina = 'sonido de moto'

# auto = Auto()
# camion = Camion()

# print(auto)
# print(camion)

# auto.tocar_bocina()
# camion.tocar_bocina()

# auto.avanzar(15)
# camion.avanzar(55)


# moto = Moto()
# moto.tocar_bocina()


# ================================================================================
# ================================================================================

# class Vehiculo:
    
#     sonido_bocina = ''
    
#     def __init__(self, marca, modelo, color):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
    
#     def avanzar(self, metros):
#         print(f'El {self} avanzo {metros} mts')
    
#     @classmethod
#     def tocar_bocina(cls):
#         print(f'{cls.sonido_bocina}!!')

# class Auto(Vehiculo):
    
#     sonido_bocina = 'PIIIII PIIII'
#     cant_autos_creados = 0
    
#     # v1
#     # def __init__(self, marca, modelo, color):
#     #     self.marca = marca
#     #     self.modelo = modelo
#     #     self.color = color
#     #     Auto.cant_autos_creados += 1
#     #     self.nro_chasis = Auto.cant_autos_creados
    
#     # v2
#     def __init__(self, marca, modelo, color):
#         super().__init__(marca, modelo, color)
#         Auto.cant_autos_creados += 1
#         self.nro_chasis = Auto.cant_autos_creados
        
#     @classmethod
#     def tocar_bocina(cls):
#         print(super().sonido_bocina)
#         return super().tocar_bocina()


# auto = Auto('Ford', 'K', 'Rojo')

# print(auto)
# print(auto.marca)
# print(auto.modelo)
# print(auto.color)
# print(auto.nro_chasis)
# print(auto.cant_autos_creados)
# print(auto.tocar_bocina())

# ================================================================================
# ================================================================================

# class Vehiculo:
    
#     sonido_bocina = ''
#     cant_vehiculos_creados = 0
    
#     def __init__(self, marca, modelo, color):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
#         Vehiculo.cant_vehiculos_creados += 1
    
#     def avanzar(self, metros):
#         print(f'El {self} avanzo {metros} mts')
    
#     @classmethod
#     def tocar_bocina(cls):
#         print(f'{cls.sonido_bocina}!!')


# class Auto(Vehiculo):
    
#     sonido_bocina = 'PIIIII PIIII'
    
#     def __init__(self, marca, modelo, color):
#         super().__init__(marca, modelo, color)
#         self.__nro_chasis = self.cant_vehiculos_creados
        
#     @classmethod
#     def tocar_bocina(cls):
#         print(super().sonido_bocina)
#         return super().tocar_bocina()

#     def ver_nro_chasis(self, es_el_duenio):
#         if es_el_duenio:
#             return self.__nro_chasis


# auto = Auto('Ford', 'K', 'Rojo')

# print(auto)
# print(auto.ver_nro_chasis(True))


# class Consesionaria:
    
#     @staticmethod
#     def ver_chasis(auto: Auto) -> None:
#         print(auto.__nro_chasis)
        
# consesionaria = Consesionaria()
# consesionaria.ver_chasis(auto)


# ================================================================================
# ================================================================================

# class Vehiculo:
    
#     sonido_bocina = ''
#     cant_vehiculos_creados = 0
    
#     def __init__(self, marca, modelo, color):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
#         Vehiculo.cant_vehiculos_creados += 1
#         self.__nro_chasis = self.cant_vehiculos_creados
    
#     def avanzar(self, metros):
#         print(f'El {self} avanzo {metros} mts')
    
#     @classmethod
#     def tocar_bocina(cls):
#         print(f'{cls.sonido_bocina}!!')


# class Auto(Vehiculo):
    
#     sonido_bocina = 'PIIIII PIIII'
    
#     @classmethod
#     def tocar_bocina(cls):
#         print(super().sonido_bocina)
#         return super().tocar_bocina()

#     def ver_nro_chasis(self, es_el_duenio):
#         if es_el_duenio:
#             return self.__nro_chasis

# auto = Auto('Ford', 'K', 'Rojo')

# print(auto)
# # print(auto.__nro_chasis)
# # print(auto.ver_nro_chasis(True))

# # ================================================================================
# # ================================================================================

# class Vehiculo:
    
#     sonido_bocina = ''
    
#     def avanzar(self, metros):
#         print(f'El {self} avanzo {metros} mts')
    
#     @classmethod
#     def tocar_bocina(cls):
#         print(f'{cls.sonido_bocina}!!')

# class Auto(Vehiculo):
    
#     sonido_bocina = 'PIIIII PIIII'
    
#     # @staticmethod
#     # def tocar_bocina():
#     #     print(f'{Auto.sonido_bocina}!!')

#     # def avanzar(self, metros):
#     #     print(f'El {self} avanzo {metros} mts')

# class Camion(Vehiculo):
    
#     sonido_bocina = 'CUAAAAA'
    
#     # @staticmethod
#     # def tocar_bocina():
#     #     print(f'{Camion.sonido_bocina}!!')

#     # def avanzar(self, metros):
#     #     print(f'El {self} avanzo {metros} mts')
    
#     @classmethod
#     def tocar_bocina(cls):
#         super().tocar_bocina()
#         print(input('Ingresa un texto y te lo paso a minuscula: ').lower())

# class Moto(Vehiculo):
    
#     sonido_bocina = 'sonido de moto'
    
#     @classmethod
#     def tocar_bocina(cls):
#         super().tocar_bocina()
#         print('Consume 15lts de nafta')

# auto = Auto()
# camion = Camion()
# moto = Moto()


# for vehiculo in [auto, camion, moto]:
#     vehiculo.tocar_bocina()


# ================================================================================
# ================================================================================

class Terrestre:
    
    @staticmethod
    def indentificar_tipo():
        print('Soy terrestre')

class Vehiculo:
    
    sonido_bocina = ''
    
    def avanzar(self, metros):
        print(f'El {self} avanzo {metros} mts')
    
    @classmethod
    def tocar_bocina(cls):
        print(f'{cls.sonido_bocina}!!')

class Auto(Vehiculo, Terrestre):
    
    sonido_bocina = 'PIIIII PIIII'
    
    # @staticmethod
    # def tocar_bocina():
    #     print(f'{Auto.sonido_bocina}!!')

    # def avanzar(self, metros):
    #     print(f'El {self} avanzo {metros} mts')

class Camion(Vehiculo):
    
    sonido_bocina = 'CUAAAAA'
    
    # @staticmethod
    # def tocar_bocina():
    #     print(f'{Camion.sonido_bocina}!!')

    # def avanzar(self, metros):
    #     print(f'El {self} avanzo {metros} mts')
    
    @classmethod
    def tocar_bocina(cls):
        super().tocar_bocina()
        print(input('Ingresa un texto y te lo paso a minuscula: ').lower())

class Moto(Vehiculo):
    
    sonido_bocina = 'sonido de moto'
    
    @classmethod
    def tocar_bocina(cls):
        super().tocar_bocina()
        print('Consume 15lts de nafta')

auto = Auto()
auto.indentificar_tipo()
print(Auto.__mro__)
camion = Camion()
moto = Moto()


for vehiculo in [auto, camion, moto]:
    vehiculo.tocar_bocina()

