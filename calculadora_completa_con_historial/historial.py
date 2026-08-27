import json
from pathlib import Path
from datetime import datetime

# ruta_historial = Path('')
# print(ruta_historial)
ruta_historial = Path().resolve() / 'data.json'
print(ruta_historial)

def agregar_a_historial(*valores, operacion, resultado):
    # print(valores)
    # print(operacion)
    # print(resultado)
    
    info = {
        'valores': valores,
        'operacion': operacion,
        'resultado': resultado,
    }

    try:
        with open(ruta_historial, 'r', encoding='utf-8') as archivo:
            data = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist, is empty, or contains invalid JSON,
        # start with an empty history dictionary.
        data = {}

    fecha = datetime.now().isoformat()

    data[fecha] = info
    print(data)

    with open(ruta_historial, 'w') as archivo:
        json.dump(data, archivo, ensure_ascii=False, indent=4)

def listar_operaciones():
    
    try:
        with open(ruta_historial, 'r', encoding='utf-8') as archivo:
            data = json.load(archivo)
            # print(data)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist, is empty, or contains invalid JSON,
        # start with an empty history dictionary.
        print('No existen datos hasta ahora...')
    else:
        print(data)
