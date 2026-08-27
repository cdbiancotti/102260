from blog.posts.manager import crear_post

post_correcto = crear_post("Mi primer post con paquetes")
post_incorrecto = crear_post(" ")

print(post_correcto)
print(post_incorrecto)
