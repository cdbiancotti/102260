import json
from pathlib import Path

ARCHIVO = Path(__file__).resolve().parent / "posts.json"

print(ARCHIVO)

with open(ARCHIVO, "r", encoding="utf-8") as archivo:
    posts = json.load(archivo)

for post in posts:
    print("ID:", post["id"])
    print("Título:", post["titulo"])
    print("Autor:", post["autor"])
    print("Estado:", post["estado"])
    print("Tags:", ", ".join(post["tags"]))
    print("-" * 40)
