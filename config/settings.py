from config.database import get_connection

connection = get_connection()
cursor = connection.cursor()
