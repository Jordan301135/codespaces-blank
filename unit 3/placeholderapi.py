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

# url = 'https://pokeapi.co/api/v2/ability/'

# response = requests.get(url)


# print(response.json())


if response.status_code == 200:
    data = response.json()

    filtered_data = {
    "name" : data{"name"}
    "height:" data{"height"}
    "weight:"