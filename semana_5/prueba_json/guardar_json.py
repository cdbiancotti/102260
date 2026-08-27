import json
from pathlib import Path

ARCHIVO = Path(__file__).resolve().parent / "posts_generados.json"

posts = [
    {"id": 1, "titulo": "Python desde cero", "autor": "Ana Pérez", "estado": "publicado"},
    {"id": 2, "titulo": "Archivos JSON", "autor": "Carlos Gómez", "estado": "borrador"}
]

with open(ARCHIVO, "w", encoding="utf-8") as archivo:
    json.dump(posts, archivo, ensure_ascii=False, indent=2)

print("Archivo creado en:", ARCHIVO)
