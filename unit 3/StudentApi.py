import requests

query = 'https://rickandmortyapi.com/api/character/1'

res = requests.get(query)

# print(res.status_code)
# print(res.json())
data = res.json()


url ='https://rickandmortyapi.com/api/character/1'
res = requests.get(url)
status = res.status_code
#print(res.status_code)
#print(res.json())

if status == 200:
    data = res.json()

    filterData = {
        "name": data["name"],
        "status":data["status"],
        "image":data["image"],
    }

    print(filterData)
else:
    print("Something went wrong")
    print(res.status_code)

url ='https://rickandmortyapi.com/api/character/2'
res = requests.get(url)
status = res.status_code
#print(res.status_code)
#print(res.json())

if status == 200:
    data = res.json()

    filterData = {
        "name": data["name"],
        "status":data["status"],
        "image":data["image"],
    }

    print(filterData)
else:
    print("Something went wrong")
    print(res.status_code)

url ='https://rickandmortyapi.com/api/character/83'
res = requests.get(url)
status = res.status_code
#print(res.status_code)
#print(res.json())

if status == 200:
    data = res.json()

    filterData = {
        "name": data["name"],
        "status":data["status"],
        "image":data["image"],
    }

    print(filterData)
else:
    print("Something went wrong")
    print(res.status_code)