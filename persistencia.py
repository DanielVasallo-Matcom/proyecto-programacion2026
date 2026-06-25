import json

DATA_FILE = "datos.json"

def cargar_datos():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_datos(eventos):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(eventos, f, indent=4, ensure_ascii=False)