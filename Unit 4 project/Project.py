# import requests

# url = 'https://dragonball-api.com/api/characters/65'

# response = requests.get(url)

# print(response)
# print(response.json())

import sqlite3

connect = sqlite3.connect('myDb.db')

cursor = connect.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS DragonBall (
        id INTEGER PRIMARY KEY,
        name TEXT,
        powerlvl INTERGER,
        transformation TEXT,
        price INTEGER,
        genre TEXT,
        total_price INTEGER
    )
''')