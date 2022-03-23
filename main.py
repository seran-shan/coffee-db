from os import system
import sqlite3
from tokenize import String
con = sqlite3.connect("CoffeeDB.db")

cursor = con.cursor()
cursor.execute("SELECT * FROM sqlite_master")


def postNote():
    print("Post New Note to CoffeeDB")
    roastery = input("Roastery: ")
    coffeeName = input("Coffee Name: ")
    points = input("Points Score: ")
    notes = input("Notes: ")

    print(f"New Post posted!\n\n")

def printTopUsers():
    query = """
        SELECT FullName, Count(Distinct CoffeeID) AS DistinctTastings
        FROM User AS U NATURAL JOIN CoffeeTasting AS CT
        WHERE Dato like “%2022”
        GROUP BY U.UserID
        ORDER BY DistinctTastings DESC;
        """
    for row in cursor.execute(query):
        print(row)

def printValueForMoney():
    query = """
        SELECT coffee.roastery AS roasteryName, coffee.name AS CoffeeName, price/kg, (AVERAGE (score)) / price/kg AS AverageScore
        FROM Coffee AS C INNER JOIN CoffeeTasting AS CT USING CoffeeID
        GROUP BY CT.coffee_id
        ORDER BY AverageScore DESC;
        """
    for row in cursor.execute(query):
        print(row)

def printFloralCoffees():
    query = """
        SELECT Coffee.roastery AS roastery, Coffee.name AS Coffeename
        FROM CoffeeTasting AS CT NATURAL JOIN Coffee AS C
        WHERE CT.notes like ‘%floral%’ OR C.description like ‘%floral%’;
        """
    for row in cursor.execute(query):
        print(row)

def printUnwashed():
    query = """
        SELECT Coffee.roastery, Coffee.name
        FROM Coffee AS C
        WHERE CoffeeID NOT IN (
      	Select C.CoffeeID
        FROM Coffee AS C NATURAL JOIN CoffeeBatch AS CB INNER JOIN ProcessingType AS PT ON (CB.ProcessingTypeID=PT.TypeID) INNER JOIN CoffeeFarm AS CF ON (CB.CoffeeFarmID=CF.FarmID)
        WHERE (PT.description LIKE ‘%Vasket%’ OR PT.name LIKE ‘%Vasket%’) AND CF.country LIKE ‘Colombia’	OR CF.country LIKE ‘Rwanda) ;
        """
    for row in cursor.execute(query):
        print(row)

printValueForMoney()

con.close()
