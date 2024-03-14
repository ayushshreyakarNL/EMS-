import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ayush@12345",
    database="ems5"
)

# Create a cursor object
cursor = db_connection.cursor()