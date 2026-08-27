with open("posts_campos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        titulo, autor, estado = linea.strip().split("|")
        print("Título:", titulo)
        print("Autor:", autor)
        print("Estado:", estado)
        print("-" * 40)
