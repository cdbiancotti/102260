# Ruta relativa
# rutas/main.py

# Ejemplos de rutas absolutas
# C:\Users\Ana\proyecto\data\posts.txt
# /home/ana/proyecto/data/posts.txt


#from pathlib import Path

#carpeta_data = Path("data")
#archivo_posts = carpeta_data / "posts.txt"

#print(f"{archivo_posts}\n")



from pathlib import Path

data_dir = Path("data")
#Quiero trabajar con una ruta llamada data.
data_dir.mkdir(parents=True, exist_ok=True)
#make directory

Path("curso/python/data")
curso
└── python
    └── data

exist_ok=True
Si la carpeta ya existe, no generes un error.

archivo = data_dir / "posts.txt"

print("Existe:", archivo.exists()) # ¿Existe algo físicamente en esta ruta?
print("Es archivo:", archivo.is_file()) #¿Esta ruta existe y corresponde a un archivo?
print("Es carpeta:", archivo.is_dir()) #¿Esta ruta representa una carpeta que realmente existe?
print("Nombre:", archivo.name) #name es una propiedad del objeto Path.
print("Extensión:", archivo.suffix) #devuelve el sufijo del archivo, que normalmente interpretamos como su extensión.
print("Padre:", archivo.parent)#devuelve el directorio inmediatamente superior a la ruta.




