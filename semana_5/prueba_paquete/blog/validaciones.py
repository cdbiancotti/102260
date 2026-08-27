# validaciones.py

def validar_post(post):
    errores = []

    if post["titulo"].strip() == "":
        errores.append("El título no puede estar vacío.")

    if post["contenido"].strip() == "":
        errores.append("El contenido no puede estar vacío.")

    if len(post["tags"]) == 0:
        errores.append("El post debe tener al menos una etiqueta.")

    if post["estado"] not in ("borrador", "publicado", "archivado"):
        errores.append("El estado del post no es válido.")

    return errores
