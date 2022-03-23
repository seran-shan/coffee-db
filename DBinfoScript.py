import sqlite3
con = sqlite3.connect("CoffeeDB.db")

cursor = con.cursor()

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
    INSERT INTO processing_type (type, description)
    VALUES ('unwashed', 'raw coffe beans')
    """
)
cursor.execute(
    """
    INSERT INTO processing_type (type, description)
    VALUES ('unwashed', 'raw ecological coffee')
    """
)
cursor.execute(
    """
    INSERT INTO processing_type (type, description)
    VALUES ('washed', 'washed, processed, finest quality')
    """
)

cursor.execute(
    """
    INSERT INTO coffee_batch (harvest_year, price_pr_kg_usd, processing_type_id, coffee_farm_id)
    VALUES (2020-01-02, 9, 1, 1)
    """
)
cursor.execute(
    """
    INSERT INTO coffee_batch (harvest_year, price_pr_kg_usd, processing_type_id, coffee_farm_id)
    VALUES (2021-02-02, 8, 2, 2)
    """
)
cursor.execute(
    """
    INSERT INTO coffee_batch (harvest_year, price_pr_kg_usd, processing_type_id, coffee_farm_id)
    VALUES (2022-03-03, 7, 3, 3)
    """
)

cursor.execute(
    """
    INSERT INTO coffee (roastery, roast_degree,roast_date, name, description, price_per_kg_nok, coffee_batch_id)
    VALUES ('Coffee Roaster', 'degree1', 2021-01-01, 'Golden Coffee', 'fine roasted beans', 10, 1)
    """
)
cursor.execute(
    """
    INSERT INTO coffee (roastery, roast_degree, roast_date, name, description, price_per_kg_nok, coffee_batch_id)
    VALUES ('Roasted Bean', 'degree2', 2022-02-02, 'Finest Coffee', 'high quality beans', 11, 2)
    """
)
cursor.execute(
    """
    INSERT INTO coffee (roastery, roast_degree, roast_date, name, description, price_per_kg_nok, coffee_batch_id)
    VALUES ('Golden Roast', 'degree3', 2020-03-03, 'Lux Coffee', 'supreme coffee beans', 14, 3)
    """
)
cursor.execute(
    """
    INSERT INTO coffee_tasting (notes, score, taste_date, coffee_id, user_id)
    VALUES ('round taste', 7, 2022-01-01, 1, 1)
    """
)
cursor.execute(
    """
    INSERT INTO coffee_tasting (notes, score, taste_date, coffee_id, user_id)
    VALUES ('strong but tasty', 8, 2022-02-02, 2, 2)
    """
)
cursor.execute(
    """
    INSERT INTO coffee_tasting (notes, score, taste_date, coffee_id, user_id)
    VALUES ('delicious flavour, fine scent', 10, 2022-03-03, 3, 3)
    """
)

con.commit()
con.close()