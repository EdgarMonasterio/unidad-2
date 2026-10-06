import requests

print("--- Ejecutado por: Edgar Harim --")

BASE = "https://jsonplaceholder.typicode.com"

# C4. Manejo de errores
try:
    r = requests.get(f"{BASE}/posts/9999", timeout=10)
    r.raise_for_status()  # Lanza excepción si el código es 4xx o 5xx
    print(r.json())
except requests.exceptions.HTTPError as e:
    print("Error HTTP:", e)
except requests.exceptions.RequestException as e:
    print("Error de conexión:", e)