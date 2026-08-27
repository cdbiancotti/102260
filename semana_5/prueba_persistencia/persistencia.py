ARCHIVO = "posts.txt"


def guardar_post(titulo):
    with open(ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write(titulo.strip() + "\n")


def listar_posts():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            return [
                linea.strip()
                for linea in archivo
                if linea.strip() != ""
            ]
    except FileNotFoundError:
        return []


def buscar_posts(termino):
    termino = termino.strip().lower()
    encontrados = []

    for titulo in listar_posts():
        if termino in titulo.lower():
            encontrados.append(titulo)

    return encontrados
