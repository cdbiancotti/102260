from persistencia import guardar_post, listar_posts, buscar_posts

guardar_post("Módulos en Python")
guardar_post("Paquetes en Python")
guardar_post("DOM en Javascript")

print("TODOS:")
for titulo in listar_posts():
    print("-", titulo)

print("\nBÚSQUEDA:")
for titulo in buscar_posts("PYTHON"):
    print("-", titulo)

    
