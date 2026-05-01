# import all the methods we will need to send/ receieve data from DB
import sqlite3

# just function
def getALLDATA():
    # setting up the connection to our dd (the road)
    connect = sqlite3.connect('myDb.db')

    #setting up or vehicle to send/ receive data
    # to / from the DB (the vehicle)
    cursor = connect.cursor()

    # the data we want to get
    # SELECT = ouyr selection
    query = "SELECT genre FROM gameSales"

    # turns the vehicle on to the data
    cursor.execute(query)

    # tells cursor to fetch/ get ALL data
    results = cursor.fetchall()

    # show our results in terminal
    print(results)

# call function
getALLDATA()


def get1data():
    connect = sqlite3.connect('myDb.db')

    cursor = connect.cursor()

    query = "SELECT genre FROM gameSales WHERE developer = 'Bandai'"

    cursor.execute(query)

    results = cursor.fetchone()

    print(results)

get1data()