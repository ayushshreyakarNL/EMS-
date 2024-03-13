import mysql.connector
import random
from datetime import datetime, timedelta




# Function to generate random education details
def generate_education():
   return random.choice(['B.tech', 'MBA', 'M.tech'])




# Function to generate random project
def generate_project():
   return random.choice(['Inventory Management', 'EMS', 'SMM'])


# Function to generate random position
def generate_position():
   return random.choice(['Web Developer', 'Data Analyst', 'Project Manager'])




# Function to generate random salary above 300000
def generate_salary():
   return random.randint(300000, 1500000)




# List of real-life names
names = [
   "John Smith", "Mary Johnson", "James Williams", "Patricia Jones", "Robert Brown",
   "Linda Davis", "Michael Miller", "Barbara Wilson", "William Moore", "Elizabeth Taylor",
   "David Martinez", "Jennifer Anderson", "Joseph Thompson", "Susan Garcia", "Charles Robinson",
   "Jessica Hernandez", "Thomas Lewis", "Sarah Walker", "Christopher Perez", "Karen Hill",
   "Daniel King", "Nancy Wright", "Matthew Scott", "Lisa Adams", "Donald Green",
   "Ashley Baker", "Paul Hall", "Kimberly Young", "Mark Turner", "Emily White"
]


# Additional addresses from Bangalore, India
addresses = [
   "123, MG Road, Bangalore",
   "456, Brigade Road, Bangalore",
   "789, Indiranagar, Bangalore",
   "101, Koramangala, Bangalore",
   "234, Jayanagar, Bangalore",
   "567, Whitefield, Bangalore",
   "890, Electronic City, Bangalore",
   "123, Bannerghatta Road, Bangalore",
   "456, Marathahalli, Bangalore",
   "789, Hebbal, Bangalore",
   "910, Yelahanka, Bangalore",
   "111, BTM Layout, Bangalore",
   "222, HSR Layout, Bangalore",
   "333, J.P. Nagar, Bangalore",
   "444, Rajajinagar, Bangalore",
   "555, Malleshwaram, Bangalore",
   "666, Basavanagudi, Bangalore",
   "777, Cox Town, Bangalore",
   "888, Banashankari, Bangalore",
   "999, Vijayanagar, Bangalore"
]


# Updated list of departments
departments = ['Engineering', 'Management', 'Finance', 'Sales', 'Board of Directors']


# List of tech stacks
tech_stacks = ['Python', 'SQL', 'Java']


# Additional unique names
additional_names = [
   "Adam Johnson", "Eva Martinez", "Ryan Davis", "Olivia Wilson", "Lucas Moore",
   "Sophia Thompson", "Aiden Garcia", "Isabella Robinson", "Noah Lewis", "Mia Walker",
   "Ethan Perez", "Ava Hill", "Liam Wright", "Emma Scott", "Jacob Adams",
   "Charlotte Green", "Alexander Hall", "Amelia Young", "William Turner", "Sofia White"
]


# Combine the existing names and additional unique names
names += additional_names


try:
   # Connect to MySQL server
   db_connection = mysql.connector.connect(
       host="localhost",
       user="root",
       password="Ayush@12345",
       database="ems3"
   )


   # Create a cursor object
   cursor = db_connection.cursor()


   # Generate and insert 100 random records
   for i in range(100):
       name = random.choice(names)
       age = random.randint(22, 60)
       address = random.choice(addresses)
       mobile_number = "98765" + str(random.randint(10000, 99999))
       gender = random.choice(['Male', 'Female'])
       education_details = generate_education()


       # Generate random date of joining in the year 2021
       doj = datetime(2021, 1, 1) + timedelta(days=random.randint(0, 364))


       department = random.choice(departments)
       position = generate_position()
       annual_salary = generate_salary()
       project = generate_project()
       manager = random.choice(names)  # Randomly assign manager from names list
       tech_stack = random.choice(tech_stacks)  # Randomly assign tech stack


       # Create an insert query
       insert_query = """
       INSERT INTO employees (name, age, address, mobile_number, gender, education_details, doj, department, position, annual_salary, project, manager, tech_stack)
       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
       """


       # Insert data into the table
       data = (
       name, age, address, mobile_number, gender, education_details, doj, department, position, annual_salary, project,
       manager, tech_stack)
       cursor.execute(insert_query, data)


   # Commit changes
   db_connection.commit()


   print("Data inserted successfully!")


finally:
   # Close cursor and connection
   cursor.close()
   db_connection.close()
