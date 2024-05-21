import psycopg2
import os
from dotenv import load_dotenv
from psycopg2 import DatabaseError
import logging

load_dotenv()

#Setup logging
logging.basicConfig(level=logging.ERROR)

#Connect to Database
def get_connection():
    try:
        connection = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DATABASE"),
        user= os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        )
        return connection
    except DatabaseError as ex:
        logging.error(f"Database connection error: {ex}")
        raise
    #finally:
        #connection.close()
        #print("Connection closed")