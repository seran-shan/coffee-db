from datetime import date
from re import U
from sqlite3 import connect

from numpy import void

# Connecting to database
con = connect('CoffeeDB.db')
# Creating a cursor
cursor = con.cursor()

# Function to add new tasting
def new_tasting(notes: str, score: int, coffee_id: int, user_id: int):
    taste_date = date.today()
    
    try:
        cursor.execute(
            '''
                INSERT INTO CoffeeTasting (notes, score, taste_date, coffe_id, user_id)
                VALUES (?, ?, ?, ?, ?)
            ''', (notes, score, taste_date, coffee_id, user_id)
        )
        print('New tasting added!')
    except Exception:
        print('Something went wrong when adding new tase!')

# Function to get a list of user with most unique coffee tastings
def get_unique_tasting():
    return;