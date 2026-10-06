import requests

print("--- Ejecutado por: Edgar Harim ---")

BASE = "https://jsonplaceholder.typicode.com"

# C3. POST, PUT y DELETE
nuevo = {"title": "Prueba de red", "body": "Contenido de ejemplo", "userId": 1}

# Petición POST
r = requests.post(f"{BASE}/posts", json=nuevo, timeout=10)
print("POST:", r.status_code, r.json())

# Petición PUT
r = requests.put(f"{BASE}/posts/1", json={**nuevo, "id": 1}, timeout=10)
print("PUT:", r.status_code, r.json())

# Petición DELETE
r = requests.delete(f"{BASE}/posts/1", timeout=10)
print("DELETE:", r.status_code)