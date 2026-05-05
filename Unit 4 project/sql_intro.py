# 1. Bring in the spl lite module to get access to all the sql methods(function) to work with our database.
import sqlite3

# 2. We need to established an actual database file using the connect method.
connect = sqlite3.connect('myDb.db')

# 3. Create a object that will be sent to the new database.
cursor = connect.cursor()

# 4. We need to create a schema (structure) for our data.
cursor.execute('''
    CREATE TABLE IF NOT EXISTS gameSales (
        id INTEGER PRIMARY KEY,
        name TEXT,
        platform TEXT,
        developer TEXT,
        price INTEGER,
        genre TEXT,
        total_price INTEGER
    )
''')
# 5. We can now create or first database object.
# cursor.execute('''
#                INSERT INTO gameSales (name, platform, developer, price, genre, total_price)
#                VALUES ('Crimson Desert', 'Ps5', 'Perals Abyss', 70, 'Action/Adventure', 5000000)
#                ''')

cursor.execute('''
               INSERT INTO gameSales (name, platform, developer, price, genre, total_price)
               VALUES ('Starfield  ', 'PS5', 'bethesda', 50, 'RPG/Sci-Fi', 2000000)
               ''')
               



# cursor.execute('''
#                UPDATE gameSales
#                SET genre = 'adventure/fighting'
#                WHERE name  = 'Naruto X Boruto Ultimate Ninja STROM'
#                ''')


# 6. once we have a new data object, we can commit this to our database.

connect.commit()
connect.close()