import requests

print("--- Ejecutado por: Edgar Harim ---")

BASE = "https://jsonplaceholder.typicode.com"

# C2. Recorrer una lista y usar parámetros
respuesta = requests.get(f"{BASE}/posts", params={"userId": 3}, timeout=10)
publicaciones = respuesta.json()  # Lista de diccionarios

print("Total:", len(publicaciones))
for p in publicaciones:
    print(f"{p['id']:>3} | {p['title']}")