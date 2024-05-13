import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

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
    except Exception as ex:
        raise ex
    #finally:
        #connection.close()
        #print("Connection closed")