import requests

query = ('https://v1.american-football.api-sports.io/players')

response = requests.get(query)

print(response.json())
