import requests
import json

# query = 'https://jsonplaceholder.typicode.com/posts/1'

# response = requests.get(query)

# print(response)
# print(response.json())

# url = 'https://jsonplaceholder.typicode.com/posts/'
# mtobj = {"title :" "testing api", 
#          "body  :" 'this is a test pose for my social media app',
#          "userId": 209786822812
#           }

# education = 'https://bored-api.appbrewery.com/filter?type=education'

# response = requests.get(education)

# print(response.json())
def pokedex():
   search = input("Would you you like to find a pokemon? ") 
   while search == 'y':
    pokename = input("please enter a pokemone name ")
    url = 'https://pokeapi.co/api/v2/pokemon/'+pokename+"/"

    response = requests.get(url)

    # print(response)
    # print(response.json())

    if response.status_code == 200:
        data= response.json()

        filtered_data = {
            "name" : data["name"],
            "height" : data["height"],
            "weight" : data["weight"],
            "types": data["types"],
            "abilities": [ability["ability"]["name"] for ability in data ["abilities"]],
        }

        print(filtered_data)
        search = input("Would you like to find another pokemon? ")

    else:
        print("data not found")
        print(response.status_code)

pokedex()