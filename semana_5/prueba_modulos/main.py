# leer_json.py

import datos
import formateador
from validaciones import validar_post

print("AUTOR")
print(datos.perfil_autor["nombre"])

print("\nLISTADO DE POSTS")
formateador.listar_posts(datos.posts)

print("\nVALIDACIÓN")
for post in datos.posts:
    errores = validar_post(post)

    if len(errores) == 0:
        print(f"El post '{post['titulo']}' es válido.")
    else:
        print(f"El post con ID {post['id']} tiene errores:")
        for error in errores:
            print(f"- {error}")
