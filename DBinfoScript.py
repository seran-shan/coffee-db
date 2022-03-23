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
    VALUES ('species1');
    """
)
cursor.execute(
    """
    INSERT INTO coffee_bean (species)
    VALUES ('species2')
    """
)
cursor.execute(
    """
    INSERT INTO coffee_bean (species)
    VALUES ('species3')
    """
)

cursor.execute(
    """
    INSERT INTO coffee_farm (farm_id, name, meters_above_sea, region, country)
    VALUES (1, 'name1', 1, 'region1', 'country1')
    """
)
cursor.execute(
    """
    INSERT INTO coffee_farm (farm_id, name, meters_above_sea, region,country)
    VALUES (2, 'name2', 2, 'region2', 'country2')
    """
)
cursor.execute(
    """
    INSERT INTO coffee_farm (farm_id, name, meters_above_sea, region, country)
    VALUES (3, 'name3', 3, 'region3', 'country3')
    """
)

cursor.execute(
    """
    INSERT INTO processing_type (type_id, name, description)
    VALUES (1, 'name1', 'description1')
    """
)
cursor.execute(
    """
    INSERT INTO processing_type (type_id, name, description)
    VALUES (2, 'name2', 'description2')
    """
)
cursor.execute(
    """
    INSERT INTO processing_type (type_id, name, description)
    VALUES (3, 'name3', 'description3')
    """
)

cursor.execute(
    """
    INSERT INTO coffee_batch (batch_id, harvest_year, price_pr_kg_usd, processing_type_id, coffee_farm_id)
    VALUES (1, 0001-01-01, 1, 1, 1)
    """
)
cursor.execute(
    """
    INSERT INTO coffee_batch (batch_id, harvest_year, price_pr_kg_usd, processing_type_id, coffee_farm_id)
    VALUES (2, 0002-02-02, 2, 2, 2)
    """
)
cursor.execute(
    """
    INSERT INTO coffee_batch (batch_id, harvest_year, price_pr_kg_usd, processing_type_id, coffee_farm_id)
    VALUES (3, 0003-03-03,3 , 3, 3)
    """
)

cursor.execute(
    """
    INSERT INTO coffee (coffee_id, roastery, roast_degree,roast_date, name, description, price_per_kg_nok, coffee_batch_id)
    VALUES (1, 'roastery1', 'degree1', 0001-01-01, 'name1', 'description1', 1, 1)
    """
)
cursor.execute(
    """
    INSERT INTO coffee (coffee_id, roastery, roast_degree, roast_date, name, description, price_per_kg_nok, coffee_batch_id)
    VALUES (2, 'roastery2', 'degree2', 0002-02-02, 'name2', 'description2', 2, 2)
    """
)
cursor.execute(
    """
    INSERT INTO coffee (coffee_id, roastery, roast_degree, roast_date, name, description, price_per_kg_nok, coffee_batch_id)
    VALUES (3, 'roastery3', 'degree3', 0003-03-03, 'name3', 'description3', 3, 3)
    """
)
cursor.execute(
    """
    INSERT INTO coffee_tasting (notes, score, taste_date, coffee_id, user_id)
    VALUES ('note1', 1, 0001-01-01, 1, 1)
    """
)
cursor.execute(
    """
    INSERT INTO coffee_tasting (notes, score, taste_date, coffee_id, user_id)
    VALUES ('note2', 2, 0002-02-02, 2, 2)
    """
)
cursor.execute(
    """
    INSERT INTO coffee_tasting (notes, score, taste_date, coffee_id, user_id)
    VALUES ('note3', 3, 0003-03-03, 3, 3)
    """
)
con.commit()
con.close()