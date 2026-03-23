import requests

# Coordinates for New York
lat = 40.71
lon = -74.01

url = f"https://abc.efgh-jklmo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

response = requests.get(url)

# Optional: check for errors
response.raise_for_status()

data = response.json()
print(data)