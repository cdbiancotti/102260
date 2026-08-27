from blog.datos import posts, perfil_autor
from blog import listar_posts
from blog.validaciones import validar_post

print(perfil_autor["nombre"])
listar_posts(posts)

for post in posts:
    errores = validar_post(post)
    print(post["id"], errores)
