import requests

print("--- Ejecutado por: Edgar Harim ---")

BASE = "https://jsonplaceholder.typicode.com"

# C1. Primer GET
respuesta = requests.get(f"{BASE}/posts/1", timeout=10)
print("Código de estado:", respuesta.status_code)
print("Tipo de contenido:", respuesta.headers["Content-Type"])

publicacion = respuesta.json()  # Convierte el JSON en un diccionario de Python
print("Título:", publicacion["title"])