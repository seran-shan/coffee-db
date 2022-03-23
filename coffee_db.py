from datetime import date
from sqlite3 import connect
from xxlimited import new


# Get coffee_id by name and roastery

def get_coffee_id(coffee_name: str, roastery: str):
    con = connect('CoffeeDB.db')
    cursor = con.cursor()
    query = '''SELECT coffee_id
               FROM coffee
               WHERE name = ? AND roastery = ?;
            '''

    cursor.execute(query, [coffee_name, roastery])
    res = cursor.fetchone()
    con.close()
    if res is None:
        return None
    else:
        return res



# Function to add new tasting


def new_tasting(notes: str, score: int, coffee_id: int, user_id: int):
    con = connect('CoffeeDB.db')
    cursor = con.cursor()
    taste_date = date.today().strftime("%Y/%m/%d")
    try:
        cursor.execute(
            """INSERT INTO coffee_tasting (notes, score, taste_date, coffee_id, user_id)
               VALUES (?, ?, ?, ?, ?)
            """, (notes, score, taste_date, coffee_id, user_id)
        )
        con.commit()
        print('New tasting added!')
    except Exception:
        print('Something went wrong when adding new taste!')
    con.close()


def get_coffe_by_value():
    con = connect('CoffeeDB.db')
    cursor = con.cursor()
    query = """SELECT roastery AS roastery_name, 
                name AS coffee_name, price_per_kg_nok, 
                (AVG(score) / price_per_kg_nok) AS AverageScore
               FROM coffee AS C NATURAL JOIN coffee_tasting AS CT
               GROUP BY CT.coffee_id
               ORDER BY AverageScore DESC;
            """

    query_result = []

    cursor.execute(query)
    tuples = cursor.fetchall()

    for tuple in tuples:
        roastery_name, name, price_per_kg_nok, score = tuple

        query_result.append({
            "roastery_name": roastery_name,
            "name": name,
            "price/kg": price_per_kg_nok,
            "score": score
        })

    con.commit()
    con.close()
    return query_result

# Function to get a list of user with most unique coffee tastings


def get_unique_tasting():
    con = connect('CoffeeDB.db')
    cursor = con.cursor()
    query = '''SELECT U.full_name, Count(DISTINCT CT.coffee_id) AS DistinctTastings
               FROM coffee_tasting AS CT INNER JOIN user AS U
               WHERE CT.taste_date like ?
               GROUP BY CT.user_id
               ORDER BY DistinctTastings DESC;
            '''

    query_result = []

    cursor.execute(query, ["2022%"])
    tuples = cursor.fetchall()

    for tuple in tuples:
        full_name, count = tuple

        query_result.append({
            'full_name': full_name,
            'count': count
        })

    con.commit()
    con.close()
    return query_result

# Gets all coffees described (both user and roastery) by the given search word


def get_coffee_by_description(search: str):
    con = connect('CoffeeDB.db')
    cursor = con.cursor()
    query = '''SELECT C.roastery AS roastery, C.name AS Coffeename
               FROM coffee_tasting AS CT NATURAL JOIN coffee AS C
               WHERE CT.notes like ? OR C.description like ?;
            '''

    query_result = []

    cursor.execute(query, [search, search])
    tuples = cursor.fetchall()

    for tuple in tuples:
        roastery, coffee_name = tuple

        query_result.append({
            "roastery_name": roastery,
            "coffee_name": coffee_name
        })

    con.commit()
    con.close()
    return query_result

# Getting the user id of the pre-logged in user


def get_user_id():
    return 1

# Gets coffee from Rwanda or Colombia that are unwashed


def get_coffee_by_country_and_processing():
    con = connect('CoffeeDB.db')
    cursor = con.cursor()
    query = """SELECT C.roastery, C.name
               FROM ((coffee AS C INNER JOIN coffee_batch AS CB ON (C.coffee_batch_id = CB.batch_id)) 
               INNER JOIN processing_type AS PT ON (CB.processing_type_id = PT.type_id))
               INNER JOIN coffee_farm AS CF ON (CB.coffee_farm_id = CF.farm_id)
               WHERE CF.country = ? OR CF.country = ? AND PT.name <> ?;
            """

    query_result = []

    cursor.execute(query, ['Rwanda', 'Colombia', 'washed'])
    tuples = cursor.fetchall()

    for tuple in tuples:
        roastery, coffee_name = tuple

        query_result.append({
            "roastery": roastery,
            "coffee_name": coffee_name
        })

    con.commit()
    con.close()
    return query_result
