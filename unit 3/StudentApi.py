import requests

query = 'https://rickandmortyapi.com/api/character/1'

response = requests.get(query)

# print(response)
# print(response.json())


def RickandMorty():
   search = input("Would you you like to find a Rick and Morty? ") 
   while search == 'y':
    rickandmortycharacter = input("please enter a Rick and Morty name ")
    url = 'https://rickandmortyapi.com/api/character/1,2,4'+rickandmortycharacter+"/"

    response = requests.get(url)

    # print(response)
    # print(response.json())

    if response.status_code == 200:
        data= response.json()

        filtered_data = {
           "id": data[1,2,4],
            "name" : data["name"],
        }

        print(filtered_data)
        search = input("Would you like to find another pokemon? ")

    else:
        print("data not found")
        print(response.status_code)

RickandMorty()