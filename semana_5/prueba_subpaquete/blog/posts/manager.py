# blog/posts/manager.py

from .validaciones import titulo_valido


def crear_post(titulo):
    if not titulo_valido(titulo):
        return None

    return {
        "titulo": titulo.strip(),
        "estado": "borrador",
    }
