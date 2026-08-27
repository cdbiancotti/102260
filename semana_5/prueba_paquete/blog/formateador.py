def crear_separador():
    return "-" * 50


def formatear_post(post):
    if len(post["tags"]) == 0:
        tags = "(sin etiquetas)"
    else:
        tags = ", ".join(sorted(post["tags"]))

    return (
        f"ID: {post['id']}\n"
        f"Título: {post['titulo']}\n"
        f"Autor: {post['autor']['nombre']}\n"
        f"Estado: {post['estado']}\n"
        f"Etiquetas: {tags}"
    )


def listar_posts(lista_posts):
    for post in lista_posts:
        print(crear_separador())
        print(formatear_post(post))
