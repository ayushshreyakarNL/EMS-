from datetime import datetime, timedelta
import mysql.connector
from db_connection import *
from validation import *
import csv
import sys


# Add a new employee
def add_employee():
    name = None
    while not name:
        name = input("Enter name: ").strip()
        if not name or not validate_name(name):
            print("Invalid name. Please enter a valid name with at least one alphabet.")
            name = None

    age = None
    while age is None or not validate_age(age):
        age_input = input("Enter age: ").strip()
        if age_input and validate_age(age_input):
            age = int(age_input)
        else:
            print("Age must be a number between 18 and 100.")

    address = None
    while not address:
        address = input("Enter address: ").strip()
        if not address:
            print("Address cannot be blank.")

    gender = None
    while not gender or not validate_gender(gender):
        gender = input("Enter gender (male/female/other): ").strip().lower()
        if not validate_gender(gender):
            print("Invalid gender. Please enter 'male', 'female', or 'other'.")

    education_details = None
    while not education_details:
        education_details = input("Enter education details: ").strip()
        if not education_details:
            print("Education details cannot be blank.")

    doj = None
    while not doj:
        try:
            doj_input = input("Enter date of joining (YYYY-MM-DD): ").strip()
            doj = datetime.strptime(doj_input, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    department = None
    while not department:
        department = input("Enter department: ").strip()
        if not department:
            print("Department cannot be blank.")

    position = None
    while not position:
        position = input("Enter position: ").strip()
        if not position:
            print("Position cannot be blank.")

    annual_salary = None
    while not annual_salary or not validate_salary(annual_salary):
        annual_salary_input = input("Enter annual salary: ").strip()
        if annual_salary_input and validate_salary(annual_salary_input):
            annual_salary = float(annual_salary_input)
        else:
            print("Salary must be entered as a positive number with a minimum of 10000.")

    project = None
    while not project:
        project = input("Enter project: ").strip()
        if not project:
            print("Project cannot be blank.")

    manager = None
    while not manager or not validate_name(manager):
        manager = input("Enter manager: ").strip()
        if not manager or not validate_name(manager):
            print("Invalid manager name. Please enter a valid name with at least one alphabet.")

    tech_stack = None
    while not tech_stack:
        tech_stack = input("Enter tech stack: ").strip()
        if not tech_stack:
            print("Tech stack cannot be blank.")

    mobile_number = None
    while not mobile_number or not validate_mobile_number(mobile_number):
        mobile_number = input("Enter mobile number: ").strip()
        if not validate_mobile_number(mobile_number):
            print("Mobile number must be exactly 10 digits and contain only numbers.")

    insert_query = """
    INSERT INTO employees (name, age, address, mobile_number, gender, education_details, doj, department, position, annual_salary, project, manager, tech_stack)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    data = (
        name, age, address, mobile_number, gender, education_details, doj, department, position, annual_salary, project,
        manager, tech_stack)
    cursor.execute(insert_query, data)
    db_connection.commit()
    print("Employee added successfully!")


# View a particular employee’s details
def view_employee_details():
    while True:
        try:
            employee_id = input("Enter employee ID: ")
            if not validate_employee_id(employee_id):
                print("Invalid Employee ID. Please enter a valid ID.")
                continue
            select_query = "SELECT * FROM employees WHERE id = %s AND deleted = 0"
            cursor.execute(select_query, (employee_id,))
            employee = cursor.fetchone()
            if employee:
                print("Employee Details:")
                print("ID:", employee[0])
                print("Name:", employee[1])
                print("Age:", employee[2])
                print("Address:", employee[3])
                print("Mobile Number:", employee[4])
                print("Gender:", employee[5])
                print("Education Details:", employee[6])
                print("Date of Joining:", employee[7])
                print("Department:", employee[8])
                print("Position:", employee[9])
                print("Annual Salary:", employee[10])
                print("Project:", employee[11])
                print("Manager:", employee[12])
                print("Tech Stack:", employee[13])
                break
            else:
                print("Employee not found. Please enter a valid Employee ID.")
        except ValueError:
            print("Invalid Employee ID. Please enter a valid ID.")


# Update employee information (name can’t be updated)
def update_employee_info():
    while True:
        try:
            employee_id = input("Enter employee ID: ")
            if not validate_employee_id(employee_id):
                print("Invalid Employee ID. Please enter a valid ID.")
                continue
            select_query = "SELECT * FROM employees WHERE id = %s AND deleted = 0"
            cursor.execute(select_query, (employee_id,))
            employee = cursor.fetchone()
            if employee:
                print("Current Employee Details:")
                print("ID:", employee[0])
                print("Name:", employee[1])
                print("Age:", employee[2])
                print("Address:", employee[3])
                print("Mobile Number:", employee[4])
                print("Gender:", employee[5])
                print("Education Details:", employee[6])
                print("Date of Joining:", employee[7])
                print("Department:", employee[8])
                print("Position:", employee[9])
                print("Annual Salary:", employee[10])
                print("Project:", employee[11])
                print("Manager:", employee[12])
                print("Tech Stack:", employee[13])

                # Menu for selecting information to update
                print("\nSelect the information you want to update:")
                print("1. Age")
                print("2. Address")
                print("3. Gender")
                print("4. Education Details")
                print("5. Date of Joining")
                print("6. Department")
                print("7. Position")
                print("8. Annual Salary")
                print("9. Project")
                print("10. Manager")
                print("11. Tech Stack")
                print("12. Mobile Number")
                print("0. Exit")

                choice = input("Enter your choice (0-12): ")

                if choice == '0':
                    break

                if choice == '1':
                    # Update age
                    age = None
                    while age is None or not validate_age(age):
                        age = input("Enter new age: ").strip()
                        if not validate_age(age):
                            print("Age must be a number between 18 and 100.")
                    update_query = "UPDATE employees SET age=%s WHERE id=%s"
                    cursor.execute(update_query, (age, employee_id))
                    db_connection.commit()
                    print("Age updated successfully!")

                elif choice == '2':
                    # Update address
                    address = None
                    while not address:
                        address = input("Enter new address: ").strip()
                        if not address:
                            print("Address cannot be blank.")
                    update_query = "UPDATE employees SET address=%s WHERE id=%s"
                    cursor.execute(update_query, (address, employee_id))
                    db_connection.commit()
                    print("Address updated successfully!")

                elif choice == '3':
                    # Update gender
                    gender = None
                    while not gender or not validate_gender(gender):
                        gender = input("Enter new gender (male/female/other): ").strip().lower()
                        if not validate_gender(gender):
                            print("Invalid gender. Please enter 'male', 'female', or 'other'.")
                    update_query = "UPDATE employees SET gender=%s WHERE id=%s"
                    cursor.execute(update_query, (gender, employee_id))
                    db_connection.commit()
                    print("Gender updated successfully!")

                elif choice == '4':
                    # Update education details
                    education_details = None
                    while not education_details:
                        education_details = input("Enter new education details: ").strip()
                        if not education_details:
                            print("Education details cannot be blank.")
                    update_query = "UPDATE employees SET education_details=%s WHERE id=%s"
                    cursor.execute(update_query, (education_details, employee_id))
                    db_connection.commit()
                    print("Education details updated successfully!")

                elif choice == '5':
                    # Update date of joining
                    doj = None
                    while not doj:
                        try:
                            doj_input = input("Enter new date of joining (YYYY-MM-DD): ").strip()
                            doj = datetime.strptime(doj_input, "%Y-%m-%d").date()
                        except ValueError:
                            print("Invalid date format. Please use YYYY-MM-DD.")
                    update_query = "UPDATE employees SET doj=%s WHERE id=%s"
                    cursor.execute(update_query, (doj, employee_id))
                    db_connection.commit()
                    print("Date of Joining updated successfully!")

                elif choice == '6':
                    # Update department
                    department = None
                    while not department:
                        department = input("Enter new department: ").strip()
                        if not department:
                            print("Department cannot be blank.")
                    update_query = "UPDATE employees SET department=%s WHERE id=%s"
                    cursor.execute(update_query, (department, employee_id))
                    db_connection.commit()
                    print("Department updated successfully!")

                elif choice == '7':
                    # Update position
                    position = None
                    while not position:
                        position = input("Enter new position: ").strip()
                        if not position:
                            print("Position cannot be blank.")
                    update_query = "UPDATE employees SET position=%s WHERE id=%s"
                    cursor.execute(update_query, (position, employee_id))
                    db_connection.commit()
                    print("Position updated successfully!")

                elif choice == '8':
                    # Update annual salary
                    annual_salary = None
                    while not annual_salary or not validate_salary(annual_salary):
                        annual_salary_input = input("Enter new annual salary: ").strip()
                        if annual_salary_input and validate_salary(annual_salary_input):
                            annual_salary = float(annual_salary_input)
                        else:
                            print("Salary must be entered as a positive number with a minimum of 10000.")
                    update_query = "UPDATE employees SET annual_salary=%s WHERE id=%s"
                    cursor.execute(update_query, (annual_salary, employee_id))
                    db_connection.commit()
                    print("Annual Salary updated successfully!")

                elif choice == '9':
                    # Update project
                    project = None
                    while not project:
                        project = input("Enter new project: ").strip()
                        if not project:
                            print("Project cannot be blank.")
                    update_query = "UPDATE employees SET project=%s WHERE id=%s"
                    cursor.execute(update_query, (project, employee_id))
                    db_connection.commit()
                    print("Project updated successfully!")

                elif choice == '10':
                    # Update manager
                    manager = None
                    while not manager or not validate_name(manager):
                        manager = input("Enter new manager: ").strip()
                        if not manager or not validate_name(manager):
                            print("Invalid manager name. Please enter a valid name with at least one alphabet.")
                    update_query = "UPDATE employees SET manager=%s WHERE id=%s"
                    cursor.execute(update_query, (manager, employee_id))
                    db_connection.commit()
                    print("Manager updated successfully!")

                elif choice == '11':
                    # Update tech stack
                    tech_stack = None
                    while not tech_stack:
                        tech_stack = input("Enter new tech stack: ").strip()
                        if not tech_stack:
                            print("Tech stack cannot be blank.")
                    update_query = "UPDATE employees SET tech_stack=%s WHERE id=%s"
                    cursor.execute(update_query, (tech_stack, employee_id))
                    db_connection.commit()
                    print("Tech Stack updated successfully!")

                elif choice == '12':
                    # Update mobile number
                    mobile_number = None
                    while not mobile_number or not validate_mobile_number(mobile_number):
                        mobile_number = input("Enter new mobile number: ").strip()
                        if not validate_mobile_number(mobile_number):
                            print("Mobile number must be exactly 10 digits and contain only numbers.")
                    update_query = "UPDATE employees SET mobile_number=%s WHERE id=%s"
                    cursor.execute(update_query, (mobile_number, employee_id))
                    db_connection.commit()
                    print("Mobile Number updated successfully!")

                else:
                    print("Invalid choice. Please enter a number between 0 and 12.")

            else:
                print("Employee not found. Please enter a valid Employee ID.")
        except ValueError:
            print("Invalid Employee ID. Please enter a valid ID.")


# Delete employee record (to check only if she/he has worked more than 1 Month) (Soft delete)
def delete_employee_record():
    while True:
        try:
            employee_id = input("Enter employee ID: ")
            if not validate_employee_id(employee_id):
                print("Invalid Employee ID. Please enter a valid ID.")
                continue
            select_query = "SELECT doj FROM employees WHERE id = %s"
            cursor.execute(select_query, (employee_id,))
            date_of_joining = cursor.fetchone()[0]
            if date_of_joining:
                today = datetime.now().date()
                if today - date_of_joining > timedelta(days=30):
                    update_query = "UPDATE employees SET deleted = 1 WHERE id = %s"
                    cursor.execute(update_query, (employee_id,))
                    db_connection.commit()
                    print("Employee record soft deleted successfully!")
                    break
                else:
                    print("Employee has worked for less than 1 month. Cannot delete record.")
                    break
            else:
                print("Employee not found. Please enter a valid Employee ID.")
        except ValueError:
            print("Invalid Employee ID. Please enter a valid ID.")


# List all employees in the organization (department, position, gender)
def list_all_employees():
    select_query = "SELECT name, department, position, gender FROM employees WHERE deleted = 0"
    cursor.execute(select_query)
    employees = cursor.fetchall()
    if employees:
        print("All Employees:")
        for employee in employees:
            print("Name:", employee[0])
            print("Department:", employee[1])
            print("Position:", employee[2])
            print("Gender:", employee[3])
            print("-------------------------")
    else:
        print("No employees found!")


# Calculate total salary at monthly level of each employee
def calculate_total_salary():
    while True:
        try:
            limit = int(input("Enter the number of employees you want to display (0 for all): "))
            if limit < 0:
                print("Limit must be a non-negative integer.")
            else:
                select_query = "SELECT id, annual_salary FROM employees WHERE deleted = 0"
                if limit:
                    select_query += " ORDER BY annual_salary DESC LIMIT %s" % limit
                cursor.execute(select_query)
                employees = cursor.fetchall()
                if employees:
                    print("Monthly Total Salary:")
                    for employee in employees:
                        monthly_salary = employee[1] / 12
                        print(f"Employee ID {employee[0]}: {monthly_salary}")
                else:
                    print("No employees found!")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")



# View employee's project details (past and present projects)
def view_employee_projects():
    while True:
        try:
            employee_id = input("Enter employee ID: ")
            if not validate_employee_id(employee_id):
                print("Invalid Employee ID. Please enter a valid ID.")
                continue
            select_query = "SELECT project FROM employees WHERE id = %s AND deleted = 0"
            cursor.execute(select_query, (employee_id,))
            result = cursor.fetchone()
            if result:
                projects = result[0]
                if projects:
                    print("Projects assigned to Employee ID", employee_id, ":")
                    print(projects)
                else:
                    print("No projects assigned to Employee ID", employee_id)
                break
            else:
                print("Employee not found or has no projects assigned.")
        except ValueError:
            print("Invalid Employee ID. Please enter a valid ID.")

# Update employee's project details (past project details should remain)
def update_employee_project():
    while True:
        try:
            employee_id = input("Enter employee ID: ")
            if not validate_employee_id(employee_id):
                print("Invalid Employee ID. Please enter a valid ID.")
                continue
            select_query = "SELECT name FROM employees WHERE id = %s AND deleted = 0"
            cursor.execute(select_query, (employee_id,))
            if cursor.fetchone():
                new_project = input("Enter new project: ").strip()
                if not new_project:
                    print("Project cannot be blank.")
                    continue

                update_query = "UPDATE employees SET project = CONCAT(project, ', ', %s) WHERE id = %s"
                cursor.execute(update_query, (new_project, employee_id))
                db_connection.commit()
                print("Project updated successfully!")
                break
            else:
                print("Employee ID not found. Please enter a valid ID.")
        except ValueError:
            print("Invalid Employee ID. Please enter a valid ID.")

def assign_manager():
    while True:
        try:
            employee_id = input("Enter employee ID: ")
            if not validate_employee_id(employee_id):
                print("Invalid Employee ID. Please enter a valid ID.")
                continue
            select_query = "SELECT name FROM employees WHERE id = %s AND deleted = 0"
            cursor.execute(select_query, (employee_id,))
            if cursor.fetchone():
                new_manager = input("Enter new manager: ").strip()
                if not new_manager:
                    print("Manager name cannot be blank.")
                    continue

                update_query = "UPDATE employees SET manager = %s WHERE id = %s"
                cursor.execute(update_query, (new_manager, employee_id))
                db_connection.commit()
                print("Manager assigned successfully!")
                break
            else:
                print("Employee ID not found. Please enter a valid ID.")
        except ValueError:
            print("Invalid Employee ID. Please enter a valid ID.")


# View manager details (employee under the manager)
def view_manager_details():
    while True:
        manager_name = input("Enter manager name: ")
        if not manager_name:
            print("Manager name cannot be empty.")
            continue
        select_query = "SELECT name FROM employees WHERE manager = %s AND deleted = 0"
        cursor.execute(select_query, (manager_name,))
        employees = cursor.fetchall()
        if employees:
            print(f"Employees under Manager {manager_name}:")
            for employee in employees:
                print(employee[0])
            break
        else:
            print("No employees found under this manager.")

def add_tech_stack():
    while True:
        try:
            employee_id = int(input("Enter employee ID: "))
            select_query = "SELECT name, education_details, tech_stack FROM employees WHERE id = %s AND deleted = 0"
            cursor.execute(select_query, (employee_id,))
            employee = cursor.fetchone()
            if employee:
                name, education_details, current_tech_stack = employee
                if "B.Tech" in education_details or "M.Tech" in education_details:
                    new_tech_stack = input("Enter tech stack to add: ").strip()
                    if not new_tech_stack:
                        print("Tech stack cannot be blank.")
                        continue

                    if current_tech_stack:
                        updated_tech_stack = current_tech_stack + ', ' + new_tech_stack
                    else:
                        updated_tech_stack = new_tech_stack

                    update_query = "UPDATE employees SET tech_stack = %s WHERE id = %s"
                    cursor.execute(update_query, (updated_tech_stack, employee_id))
                    db_connection.commit()
                    print("Tech stack added successfully!")
                else:
                    print(f"{name} is not an engineer. Tech stack cannot be added.")
                break
            else:
                print("Employee ID not found. Please enter a valid ID.")
        except ValueError:
            print("Invalid Employee ID. Please enter a valid ID.")




# View employee's known tech stack (applicable only for engineering employees)
def view_employee_tech_stack():
    while True:
        try:
            employee_id = int(input("Enter employee ID: "))
            select_query = "SELECT name, education_details, tech_stack FROM employees WHERE id = %s AND deleted = 0"
            cursor.execute(select_query, (employee_id,))
            employee = cursor.fetchone()
            if employee:
                name, education_details, tech_stack = employee
                if "B.Tech" in education_details or "M.Tech" in education_details:
                    print(f"Tech Stack for {name}: {tech_stack}")
                else:
                    print(f"{name} is not an engineer.")
                break
            else:
                print("Employee ID not found. Please enter a valid ID.")
        except ValueError:
            print("Invalid Employee ID. Please enter a valid ID.")




# Search employees by name
def search_employee_by_name():
    while True:
        try:
            employee_name = input("Enter employee name: ").strip()  # Remove leading/trailing whitespace
            if not employee_name:
                print("Employee name cannot be empty. Please enter a valid name.")
                continue

            select_query = "SELECT * FROM employees WHERE name LIKE %s AND deleted = 0"
            cursor.execute(select_query, ('%' + employee_name + '%',))
            employees = cursor.fetchall()
            if employees:
                print("Matching Employees:")
                for employee in employees:
                    print("ID:", employee[0])
                    print("Name:", employee[1])
                    print("Department:", employee[8])
                    print("Position:", employee[9])
                    print("Gender:", employee[5])
                    print("-------------------------")
                break
            else:
                print("No matching employees found.")
        except Exception as e:
            print("Error:", e)


# Search employees by tech stack
def search_employee_by_tech_stack():
    while True:
        try:
            tech_stack = input("Enter tech stack: ").strip()  # Remove leading/trailing whitespace
            if not tech_stack:
                print("Tech stack cannot be empty. Please enter a valid tech stack.")
                continue

            select_query = "SELECT * FROM employees WHERE tech_stack LIKE %s AND deleted = 0"
            cursor.execute(select_query, ('%' + tech_stack + '%',))
            employees = cursor.fetchall()
            if employees:
                print("Employees with Tech Stack:", tech_stack)
                for employee in employees:
                    print("ID:", employee[0])
                    print("Name:", employee[1])
                    print("Department:", employee[8])
                    print("Position:", employee[9])
                    print("Gender:", employee[5])
                    print("-------------------------")
                break
            else:
                print("No employees found with the specified tech stack.")
        except Exception as e:
            print("Error:", e)


# Search employees by project name
def search_employee_by_project():
    while True:
        try:
            project_name = input("Enter project name: ").strip()  # Remove leading/trailing whitespace
            if not project_name:
                print("Project name cannot be empty. Please enter a valid project name.")
                continue

            select_query = "SELECT * FROM employees WHERE project LIKE %s AND deleted = 0"
            cursor.execute(select_query, ('%' + project_name + '%',))
            employees = cursor.fetchall()
            if employees:
                print("Employees Assigned to Project:", project_name)
                for employee in employees:
                    print("ID:", employee[0])
                    print("Name:", employee[1])
                    print("Department:", employee[8])
                    print("Position:", employee[9])
                    print("Gender:", employee[5])
                    print("-------------------------")
                break
            else:
                print("No employees found assigned to the specified project.")
        except Exception as e:
            print("Error:", e)


# Sort employees by salary
def sort_employees_by_salary():
    while True:
        try:
            limit = input("Enter 'top' for top earners, 'least' for least earners, or 'all' for all employees: ").strip().lower()
            if limit not in ['top', 'least', 'all']:
                print("Invalid input. Please enter 'top', 'least', or 'all'.")
            else:
                select_query = "SELECT * FROM employees WHERE deleted = 0"
                if limit == 'top':
                    select_query += " ORDER BY annual_salary DESC LIMIT 10"
                elif limit == 'least':
                    select_query += " ORDER BY annual_salary ASC LIMIT 10"

                cursor.execute(select_query)
                employees = cursor.fetchall()
                if employees:
                    if limit == 'top':
                        print("Top 10 Earners Sorted by Salary (Descending):")
                    elif limit == 'least':
                        print("Least 10 Earners Sorted by Salary (Ascending):")
                    else:
                        print("Employees Sorted by Salary:")
                    for employee in employees:
                        print("ID:", employee[0])
                        print("Name:", employee[1])
                        print("Department:", employee[8])
                        print("Position:", employee[9])
                        print("Salary:", employee[10])
                        print("-------------------------")
                else:
                    print("No employees found!")
                break
        except Exception as e:
            print("Error:", e)


def export_data_to_csv():
    try:
        # Fetch all employee data from the database
        select_query = "SELECT * FROM employees"
        cursor.execute(select_query)
        employees = cursor.fetchall()

        if employees:
            # Define the CSV file name
            csv_file = "/home/nineleaps/Downloads/Employee Export - Sheet1.csv"

            # Write data to CSV file
            with open(csv_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                # Write header
                writer.writerow(
                    ["ID", "Name", "Age", "Address", "Mobile Number", "Gender", "Education Details", "Date of Joining",
                     "Department", "Position", "Annual Salary", "Project", "Manager", "Tech Stack"])
                # Write rows
                for employee in employees:
                    writer.writerow(employee)

            print(f"Data exported to {csv_file} successfully!")
        else:
            print("No employees found to export.")
    except Exception as e:
        print("Error:", e)

def add_employees_from_csv():
    file_path = input("Enter the path to the CSV file: ")
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                insert_query = "INSERT INTO employees (name, age, address, mobile_number, gender, education_details, doj, department, position, annual_salary, project, manager, tech_stack, deleted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                values = (row['name'], row['age'], row['address'], row['mobile_number'], row['gender'], row['education_details'], row['doj'], row['department'], row['position'], row['annual_salary'], row['project'], row['manager'], row['tech_stack'], 0)  # assuming 'deleted' is set to 0 for new entries
                cursor.execute(insert_query, values)
                db_connection.commit()
        print("Data from CSV file inserted successfully!")
    except Exception as e:
        print("Error:", e)




