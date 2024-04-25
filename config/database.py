import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


#Connect to Database
connection = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DATABASE"),
    user= os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    )

cursor = connection.cursor()
cursor.execute("SELECT * from taxis;")

record = cursor.fetchall()
print("Estás conectado a - ", record)