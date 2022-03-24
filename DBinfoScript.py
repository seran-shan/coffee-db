import sqlite3

con = sqlite3.connect("CoffeeDB.db")

cursor = con.cursor()

cursor.execute(
    """
    INSERT INTO user (full_name, email, password)
    VALUES ('Bruker', 'Bruker@email.no', 'BrukerPassord')
    """
)
cursor.execute(
    """
    INSERT INTO user (full_name, email, password)
    VALUES ('Julius', 'julius@email.no', 'passord1')
    """
)
cursor.execute(
    """
    INSERT INTO user (full_name, email, password)
    VALUES ('Seran', 'Seran@email.no', 'passord2') 
    """
)
cursor.execute(
    """
    INSERT INTO user (full_name, email, password)
    VALUES ('Hammad', 'Hammad@email.no', 'passord3') 
    """
)

cursor.execute(
    """
    INSERT INTO coffee_bean (species)
    VALUES ('Arabica');
    """
)
cursor.execute(
    """
    INSERT INTO coffee_bean (species)
    VALUES ('Robusta')
    """
)
cursor.execute(
    """
    INSERT INTO coffee_bean (species)
    VALUES ('Liberica')
    """
)

cursor.execute(
    """
    INSERT INTO coffee_farm (name, meters_above_sea, region, country)
    VALUES ('hermano', 177, 'South America', 'Colombia')
    """
)
cursor.execute(
    """
    INSERT INTO coffee_farm (name, meters_above_sea, region,country)
    VALUES ('golden coffee', 27, 'Africa', 'Rwanda')
    """
)
cursor.execute(
    """
    INSERT INTO coffee_farm (name, meters_above_sea, region, country)
    VALUES ('cafe de abuela', 88, 'South America', 'Argentina')
    """
)

cursor.execute(
    """
    INSERT INTO processing_type (name, description)
    VALUES ('aged', 'raw coffe beans')
    """
)
cursor.execute(
    """
    INSERT INTO processing_type (name, description)
    VALUES ('plain', 'raw ecological coffee')
    """
)
cursor.execute(
    """
    INSERT INTO processing_type (name, description)
    VALUES ('washed', 'washed, processed, finest quality')
    """
)

cursor.execute(
    """
    INSERT INTO coffee_batch (harvest_year, price_pr_kg_usd, processing_type_id, coffee_farm_id)
    VALUES ('2018-01-01', 1, 1, 1)
    """
)
cursor.execute(
    """
    INSERT INTO coffee_batch (harvest_year, price_pr_kg_usd, processing_type_id, coffee_farm_id)
    VALUES ('2020-02-02', 2, 2, 2)
    """
)
cursor.execute(
    """
    INSERT INTO coffee_batch (harvest_year, price_pr_kg_usd, processing_type_id, coffee_farm_id)
    VALUES ('2022-03-03',3 , 3, 3)
    """
)

cursor.execute(
    """
    INSERT INTO coffee (roastery, roast_degree,roast_date, name, description, price_per_kg_nok, coffee_batch_id)
    VALUES ('Tromso-roastery', 'degree-1', '2018-01-01', 'TromsoCoffee', 'Best served cold', 1, 1)
    """
)
cursor.execute(
    """
    INSERT INTO coffee (roastery, roast_degree, roast_date, name, description, price_per_kg_nok, coffee_batch_id)
    VALUES ('Trondheim-roastery', 'degree-2', '2020-02-02', 'TrondheimCoffee', 'Sticks to the moustache', 1, 2)
    """
)
cursor.execute(
    """
    INSERT INTO coffee (roastery, roast_degree, roast_date, name, description, price_per_kg_nok, coffee_batch_id)
    VALUES ('Oslo-roastery', 'degree-3', '2022-03-03', 'OsloCoffee', 'Everyone has got an opinion', 1, 3)
    """
)
cursor.execute(
    """
    INSERT INTO coffee_tasting (notes, score, taste_date, coffee_id, user_id)
    VALUES ('This is coffee 1', 1, '2018-01-01', 1, 1)
    """
)
cursor.execute(
    """
    INSERT INTO coffee_tasting (notes, score, taste_date, coffee_id, user_id)
    VALUES ('This is coffee 2', 2, '2020-02-02', 2, 2)
    """
)
cursor.execute(
    """
    INSERT INTO coffee_tasting (notes, score, taste_date, coffee_id, user_id)
    VALUES ('This is coffee 3', 3, '2022-03-03', 3, 3)
    """
)

con.commit()
con.close()