import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get the database connection details from environment variables
HOST = os.getenv('DB_HOST')
DATABASE = os.getenv('DB_DATABASE')
USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')

def create_connection():
    """Establish a connection to the MySQL database and return the connection object."""
    try:
        connection = mysql.connector.connect(
            host=HOST,
            database=DATABASE,
            user=USER,
            password=PASSWORD
        )
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None
