BEGIN;

-- Create model User
CREATE TABLE "user" (
    "user_id" INTEGER NOT NULL UNIQUE, 
    "full_name" TEXT NOT NULL,
    "email" TEXT NOT NULL, 
    "password" TEXT NOT NULL,
    PRIMARY KEY("user_id" AUTOINCREMENT) 
);

-- Create model Coffee
CREATE TABLE "coffee" (
    "coffee_id" INTEGER NOT NULL UNIQUE,
    "roastery" TEXT NOT NULL,
    "roast_degree" TEXT NOT NULL,
    "roast_date" DATE NOT NULL,
    "description" TEXT NOT NULL, 
    "price_per_kg_nok" INTEGER NOT NULL,
    "coffee_batch_id" INTEGER NOT NULL,
    PRIMARY KEY("coffee_id" AUTOINCREMENT),
    FOREIGN KEY ("coffee_batch_id") REFERENCES "coffee_batch" ("batch_id")   
);

-- Create model CoffeeTasting
/** 
    Notes, score and taste_date can be null, if user don't want to review the coffee 
*/
CREATE TABLE "coffee_tasting" (
    "notes" TEXT, 
    "score" INTEGER, 
    "taste_date" DATE,
    "coffee_id" INTEGER NOT NULL, 
    "user_id" INTEGER NOT NULL,
    PRIMARY KEY("coffee_id", "user_id"),
    FOREIGN KEY ("coffee_id") REFERENCES "coffee" ("coffee_id"),
    FOREIGN KEY ("user_id") REFERENCES "user" ("user_id") 
);

-- Create model CoffeeBatch
CREATE TABLE "coffee_batch" (
    "batch_id" INTEGER NOT NULL UNIQUE, 
    "harvest_year" DATE NOT NULL, 
    "price_pr_kg_usd" INTEGER NOT NULL,
    "processing_type_id" INTEGER NOT NULL, 
    "coffee_farm_id" INTEGER NOT NULL,
    PRIMARY KEY ("batch_id" AUTOINCREMENT),
    FOREIGN KEY ("processing_type_id") REFERENCES "processing_type" ("type_id"),
    FOREIGN KEY ("coffee_farm_id") REFERENCES "coffee_farm" ("farmID") 
);

-- Create model CoffeeFarm
CREATE TABLE "coffee_farm" (
    "farm_id" INTEGER NOT NULL UNIQUE, 
    "name" TEXT NOT NULL, 
    "meters_above_sea" INTEGER NOT NULL, 
    "region" TEXT NOT NULL, 
    "country" TEXT NOT NULL,
    PRIMARY KEY ("farm_id" AUTOINCREMENT)
);

-- Create model ProcessingType
CREATE TABLE "processing_type" (
    "type_id" INTEGER NOT NULL UNIQUE, 
    "name" TEXT NOT NULL, 
    "description" TEXT NOT NULL,
    PRIMARY KEY ("type_id" AUTOINCREMENT)
);

-- Create model UnprocessedBean
CREATE TABLE "coffee_bean" (
    "bean_id" INTEGER NOT NULL, 
    "species" TEXT NOT NULL,
    PRIMARY KEY ("bean_id" AUTOINCREMENT)
);

-- Create model for the relation beansInBatch
CREATE TABLE "beans_in_batch" (
    "coffee_batch_id" INTEGER NOT NULL, 
    "coffee_bean_id" INTEGER NOT NULL,
    PRIMARY KEY("coffee_batch_id", "coffee_bean_id"),
    FOREIGN KEY ("coffee_batch_id") REFERENCES "coffee" ("batch_id"),
    FOREIGN KEY ("coffee_bean_id") REFERENCES "user" ("bean_id") 
);

-- Create model for the relation beansInBatch
CREATE TABLE "has_bean" (
    "coffee_farm_id" INTEGER NOT NULL, 
    "coffee_bean_id" INTEGER NOT NULL,
    PRIMARY KEY("coffee_farm_id", "coffee_bean_id"),
    FOREIGN KEY ("coffee_farm_id") REFERENCES "coffee" ("farm_id"),
    FOREIGN KEY ("coffee_bean_id") REFERENCES "user" ("bean_id")
);

COMMIT;