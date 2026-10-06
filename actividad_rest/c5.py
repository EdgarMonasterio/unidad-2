import requests

print("--- Ejecutado por: Edgar Harim ---")


# C5. Consumir otra API (clima)
def obtener_clima(latitud, longitud):
    url = "https://api.open-meteo.com/v1/forecast"
    parametros = {
        "latitude": latitud,
        "longitude": longitud,
        "current": "temperature_2m,wind_speed_10m",
    }
    r = requests.get(url, params=parametros, timeout=10)
    r.raise_for_status()
    return r.json()["current"]


# Prueba con tres ciudades
ciudades = [
    {"nombre": "Querétaro", "lat": 20.59, "lon": -100.39},
    {"nombre": "Dolores Hidalgo", "lat": 21.15, "lon": -100.93},
    {"nombre": "Guanajuato", "lat": 21.01, "lon": -101.25},
]

print(f"{'Ciudad':<18} | {'Temp (°C)':<10} | {'Viento (km/h)':<14}")
print("-" * 50)

for c in ciudades:
    try:
        clima = obtener_clima(c["lat"], c["lon"])
        temp = clima["temperature_2m"]
        viento = clima["wind_speed_10m"]
        print(f"{c['nombre']:<18} | {temp:<10} | {viento:<14}")
    except requests.exceptions.RequestException as e:
        print(f"Error con {c['nombre']}: {e}")