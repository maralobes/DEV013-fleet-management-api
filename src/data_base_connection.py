import psycopg2
import os

#Connect to Database
connection = psycopg2.connect(
print(os.getenv("POSTGRES_DATABASE")),
    dbname=os.getenv("POSTGRES_DATABASE"),
    user= os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    )