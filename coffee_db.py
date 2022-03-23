from datetime import date
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
            """INSERT INTO CoffeeTasting (notes, score, taste_date, coffe_id, user_id)
               VALUES (?, ?, ?, ?, ?)
            """, (notes, score, taste_date, coffee_id, user_id)
        )
        print('New tasting added!')
    except Exception:
        print('Something went wrong when adding new tase!')

def get_coffe_by_value():
        query = """SELECT roastery AS roastery_name, name AS coffee_name, price_per_kg_nok, (AVERAGE (score) / price_per_kg_nok) AS AverageScore
                   FROM coffee AS C INNER JOIN coffee_tasting AS coffee_tasting USING coffee_id
                   GROUP BY coffee_tasting.coffee_id
                   ORDER BY AverageScore DESC;
                """

        query_result = []

        for i in cursor.execute(query):
            roastery_name, name, price_per_kg_nok, score = i

            query_result.append({
                "roastery_name": roastery_name,
                "name": name,
                "price/kg": price_per_kg_nok,
                "score": score
            })

        con.commit()
        return query_result

# Function to get a list of user with most unique coffee tastings
def get_unique_tasting():
    query = '''SELECT full_name, Count(DISTINCT coffee_id) AS DistinctTastings
               FROM user AS U NATURAL JOIN coffee_tasting AS CT
               WHERE taste_date like "?"
               GROUP BY U.user_id
               ORDER BY DistinctTastings DESC;
            '''
    
    query_result = []

    for tupel in cursor.execute(query, [2022]):
        full_name, count = tupel

        query_result.append({
            'full_name': full_name,
            'count': count
        })

    con.commit()
    return query_result

# Gets all coffees described (both user and roastery) by the given search word
def getCoffeeByDescription(search: str):
    query = '''SELECT coffee.roastery AS roastery, coffee.name AS Coffeename
               FROM coffee_tasting AS CT NATURAL JOIN coffee AS C
               WHERE CT.notes like "?" OR C.description like "?";
            '''

    query_result = []

    for tupel in cursor.execute(query, [search, search]):
        roastery, coffee_name = tupel

        query_result.append({
            "roastery_name": roastery,
            "coffee_name": coffee_name
        })

    con.commit()
    return query_result

# Gets coffee from Rwanda or Colombia that are unwashed
def get_coffee_by_country_and_processing():
    query = """SELECT coffee.roastery, coffee.name
               FROM coffee AS C
               WHERE coffee_id NOT IN (
                    SELECT C.coffee_id
                    FROM coffee AS C NATURAL JOIN coffee_batch AS CB INNER JOIN processing_type AS PT ON (CB.processing_type_id=PT.type_id) INNER JOIN coffee_farm AS CF ON (CB.coffee_farm_id=CF.farm_id)
                    WHERE (PT.description LIKE "?" OR PT.name LIKE ‘%Vasket%’) AND CF.country LIKE "?"	OR CF.country LIKE "?"
               );
            """

    query_result = []

    for tupel in cursor.execute(query, ['vasket', 'Colombia', 'Rwanda']):
        roastery, coffee_name = tupel

        query_result.append({
            "roastery": roastery,
            "coffee_name": coffee_name
        })

    con.commit()
    return query_result