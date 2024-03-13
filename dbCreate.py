import mysql.connector

# Connect to MySQL server
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ayush@12345",
    database="ems3"
)

# Create a cursor object
cursor = db_connection.cursor()

# Create a table query
create_table_query = """
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    address VARCHAR(255),
    mobile_number VARCHAR(15),
    gender VARCHAR(10),
    education_details VARCHAR(255),
    doj DATE,
    department VARCHAR(50),
    position VARCHAR(50),
    annual_salary DECIMAL(10, 2),
    project VARCHAR(100),
    manager VARCHAR(255),
    tech_stack VARCHAR(255)
)
"""

# Execute the create table query
cursor.execute(create_table_query)

# Commit changes
db_connection.commit()

# Close cursor and connection
cursor.close()
db_connection.close()

print("Table 'employees' created successfully!")
