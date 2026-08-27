# leer_posts.py
'''
with open("posts.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        titulo = linea.strip()
        print(titulo)
'''
with open("posts.txt", "r", encoding="utf-8") as archivo:
    contenido_completo = archivo.read()

print(contenido_completo)

