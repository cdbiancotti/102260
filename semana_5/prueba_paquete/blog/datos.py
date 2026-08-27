perfil_autor = {
    "nombre": "Ana Pérez",
    "bio": "Desarrolladora Python y creadora de contenido.",
    "especialidad": "Django",
    "redes_sociales": ["@ana_dev", "@python_ana"],
}

estados_post = ("borrador", "publicado", "archivado")

posts = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "autor": perfil_autor,
        "estado": "publicado",
        "tags": {"Python", "Programación"},
        "contenido": "En este post aprendemos los conceptos básicos.",
    },
    {
        "id": 2,
        "titulo": "",
        "autor": perfil_autor,
        "estado": "borrador",
        "tags": set(),
        "contenido": "",
    },
]
