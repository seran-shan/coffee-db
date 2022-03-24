import sqlite3

con = sqlite3.connect("CoffeeDB.db")

cursor = con.cursor()

cursor.execute(
    """
    INSERT INTO user (full_name, email, password)
    VALUES ('Sensor Sensorsen', 'Bruker@email.no', 'BrukerPassord')
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
    INSERT INTO coffee_farm (name, meters_above_sea, region, country)
    VALUES ('Lola', 93, 'South America', 'Colombia')
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
    VALUES ('plain', 'raw ecological coffee, floral')
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
    INSERT INTO processing_type (name, description)
    VALUES ('honey', 'honey processed, for a sweet coffee')
    """
)

cursor.execute(
    """
    INSERT INTO coffee_batch (harvest_year, price_pr_kg_usd, processing_type_id, coffee_farm_id)
    VALUES ('2018', 1, 1, 1)
    """
)
cursor.execute(
    """
    INSERT INTO coffee_batch (harvest_year, price_pr_kg_usd, processing_type_id, coffee_farm_id)
    VALUES ('2020', 2, 2, 2)
    """
)
cursor.execute(
    """
    INSERT INTO coffee_batch (harvest_year, price_pr_kg_usd, processing_type_id, coffee_farm_id)
    VALUES ('2022', 3, 3, 3)
    """
)

cursor.execute(
    """
    INSERT INTO coffee_batch (harvest_year, price_pr_kg_usd, processing_type_id, coffee_farm_id)
    VALUES ('2022', 3, 4, 4)
    """
)

cursor.execute(
    """
    INSERT INTO coffee (roastery, roast_degree,roast_date, name, description, price_per_kg_nok, coffee_batch_id)
    VALUES ('Tromso-brenneri', 'Light', '2018-01-01', 'TromsoKaffen', 'Floral', 40, 1)
    """
)
cursor.execute(
    """
    INSERT INTO coffee (roastery, roast_degree, roast_date, name, description, price_per_kg_nok, coffee_batch_id)
    VALUES ('Trondheims-brenneri', 'Cinnamon', '2020-02-02', 'TrondheimsKaffen', 'Setter seg fast i barten', 30, 2)
    """
)
cursor.execute(
    """
    INSERT INTO coffee (roastery, roast_degree, roast_date, name, description, price_per_kg_nok, coffee_batch_id)
    VALUES ('Oslo-brenneri', 'Dark', '2022-03-03', 'OsloKaffen', 'Alle har meninger om den', 23, 3)
    """
)
cursor.execute(
    """
    INSERT INTO coffee (roastery, roast_degree, roast_date, name, description, price_per_kg_nok, coffee_batch_id)
    VALUES ('Nidaros-brenneri', 'Medium', '2022-02-03', 'NidarosCoffee', 'Sweet, but sour', 20, 4)
    """
)
cursor.execute(
    """
    INSERT INTO coffee_tasting (notes, score, taste_date, coffee_id, user_id)
    VALUES ('Dette er kaffe1', 1, '2022-01-01', 1, 1)
    """
)
cursor.execute(
    """
    INSERT INTO coffee_tasting (notes, score, taste_date, coffee_id, user_id)
    VALUES ('Dette er kaffe2', 1, '2022-03-01', 2, 1)
    """
)
cursor.execute(
    """
    INSERT INTO coffee_tasting (notes, score, taste_date, coffee_id, user_id)
    VALUES ('Dette er kaffe2', 2, '2022-02-02', 2, 2)
    """
)
cursor.execute(
    """
    INSERT INTO coffee_tasting (notes, score, taste_date, coffee_id, user_id)
    VALUES ('Dette er kaffe 3', 3, '2020-03-03', 3, 3)
    """
)

con.commit()
con.close()