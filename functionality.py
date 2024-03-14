from datetime import datetime, timedelta
import mysql.connector
from db_connection import *
from validation import *

# Connect to MySQL server



# Add a new employee
def add_employee():
    name = input("Enter name: ")

    # Validate age
    age = None
    while age is None or not validate_age(age):
        age = input("Enter age: ")
        if not validate_age(age):
            print("Age must be a number between 18 and 100.")

    address = input("Enter address: ")
    gender = input("Enter gender (male/female/other): ")
    while not validate_gender(gender):
        print("Invalid gender. Please enter 'male', 'female', or 'other'.")
        gender = input("Enter gender (male/female/other): ")
    education_details = input("Enter education details: ")

    doj = None
    while doj is None:
        try:
            doj = datetime.strptime(input("Enter date of joining (YYYY-MM-DD): "), "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    department = input("Enter department: ")
    position = input("Enter position: ")

    # Validate salary
    while True:
        annual_salary = input("Enter annual salary: ")
        if validate_salary(annual_salary):
            annual_salary = float(annual_salary)
            break
        else:
            print("Salary must be entered as a positive number.")

    project = input("Enter project: ")
    manager = input("Enter manager: ")
    tech_stack = input("Enter tech stack: ")

    # Validate mobile number
    while True:
        mobile_number = input("Enter mobile number: ")
        if validate_mobile_number(mobile_number):
            break
        else:
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
            select_query = "SELECT * FROM employees WHERE id = %s"
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
            select_query = "SELECT * FROM employees WHERE id = %s"
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

                # Prompt for updated employee details
                age = None
                while age is None or not validate_age(age):
                    age = input("Enter age: ")
                    if not validate_age(age):
                        print("Age must be a number between 18 and 100.")

                address = input("Enter address: ")
                gender = input("Enter gender (male/female/other): ")
                while not validate_gender(gender):
                    print("Invalid gender. Please enter 'male', 'female', or 'other'.")
                    gender = input("Enter gender (male/female/other): ")
                education_details = input("Enter education details: ")

                doj = None
                while doj is None:
                    try:
                        doj = datetime.strptime(input("Enter date of joining (YYYY-MM-DD): "), "%Y-%m-%d").date()
                    except ValueError:
                        print("Invalid date format. Please use YYYY-MM-DD.")

                department = input("Enter department: ")
                position = input("Enter position: ")

                # Validate salary
                while True:
                    annual_salary = input("Enter annual salary: ")
                    if validate_salary(annual_salary):
                        annual_salary = float(annual_salary)
                        break
                    else:
                        print("Salary must be entered as a positive number.")

                project = input("Enter project: ")
                manager = input("Enter manager: ")
                tech_stack = input("Enter tech stack: ")

                # Validate mobile number
                while True:
                    mobile_number = input("Enter mobile number: ")
                    if validate_mobile_number(mobile_number):
                        break
                    else:
                        print("Mobile number must be exactly 10 digits and contain only numbers.")

                # Update the employee record in the database
                update_query = """
                UPDATE employees 
                SET age=%s, address=%s, gender=%s, education_details=%s, doj=%s, department=%s, position=%s, annual_salary=%s, project=%s, manager=%s, tech_stack=%s, mobile_number=%s
                WHERE id=%s
                """
                data = (
                    age, address, gender, education_details, doj, department, position, annual_salary, project, manager,
                    tech_stack, mobile_number, employee_id)
                cursor.execute(update_query, data)
                db_connection.commit()
                print("Employee information updated successfully!")
                break
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
                    delete_query = "DELETE FROM employees WHERE id = %s"
                    cursor.execute(delete_query, (employee_id,))
                    db_connection.commit()
                    print("Employee record deleted successfully!")
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
    select_query = "SELECT name, department, position, gender FROM employees"
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
    select_query = "SELECT id, annual_salary FROM employees"
    cursor.execute(select_query)
    employees = cursor.fetchall()
    if employees:
        print("Monthly Total Salary:")
        for employee in employees:
            monthly_salary = employee[1] / 12
            print(f"Employee ID {employee[0]}: {monthly_salary}")
    else:
        print("No employees found!")


# View employee's project details (past and present projects)
def view_employee_projects():
    while True:
        try:
            employee_id = input("Enter employee ID: ")
            if not validate_employee_id(employee_id):
                print("Invalid Employee ID. Please enter a valid ID.")
                continue
            select_query = "SELECT project FROM employees WHERE id = %s"
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


# Assign project to employee
def assign_project():
    while True:
        try:
            employee_id = input("Enter employee ID: ")
            if not validate_employee_id(employee_id):
                print("Invalid Employee ID. Please enter a valid ID.")
                continue
            select_query = "SELECT name FROM employees WHERE id = %s"
            cursor.execute(select_query, (employee_id,))
            if cursor.fetchone():
                new_project = input("Enter new project: ")

                update_query = "UPDATE employees SET project = CONCAT(project, ', ', %s) WHERE id = %s"
                cursor.execute(update_query, (new_project, employee_id))
                db_connection.commit()
                print("Project assigned successfully!")
                break
            else:
                print("Employee ID not found. Please enter a valid ID.")
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
            select_query = "SELECT name FROM employees WHERE id = %s"
            cursor.execute(select_query, (employee_id,))
            if cursor.fetchone():
                new_project = input("Enter new project: ")

                update_query = "UPDATE employees SET project = CONCAT(project, ', ', %s) WHERE id = %s"
                cursor.execute(update_query, (new_project, employee_id))
                db_connection.commit()
                print("Project updated successfully!")
                break
            else:
                print("Employee ID not found. Please enter a valid ID.")
        except ValueError:
            print("Invalid Employee ID. Please enter a valid ID.")


# Assign a manager to an employee
def assign_manager():
    while True:
        try:
            employee_id = input("Enter employee ID: ")
            if not validate_employee_id(employee_id):
                print("Invalid Employee ID. Please enter a valid ID.")
                continue
            select_query = "SELECT name FROM employees WHERE id = %s"
            cursor.execute(select_query, (employee_id,))
            if cursor.fetchone():
                new_manager = input("Enter new manager: ")

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
        select_query = "SELECT name FROM employees WHERE manager = %s"
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
            select_query = "SELECT name, education_details, tech_stack FROM employees WHERE id = %s"
            cursor.execute(select_query, (employee_id,))
            employee = cursor.fetchone()
            if employee:
                name, education_details, current_tech_stack = employee
                if "B.Tech" in education_details or "M.Tech" in education_details:
                    new_tech_stack = input("Enter tech stack to add: ")

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
            select_query = "SELECT name, education_details, tech_stack FROM employees WHERE id = %s"
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
            employee_name = input("Enter employee name: ")
            select_query = "SELECT * FROM employees WHERE name LIKE %s"
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
            tech_stack = input("Enter tech stack: ")
            select_query = "SELECT * FROM employees WHERE tech_stack LIKE %s"
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
            project_name = input("Enter project name: ")
            select_query = "SELECT * FROM employees WHERE project LIKE %s"
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
    try:
        select_query = "SELECT * FROM employees ORDER BY annual_salary DESC"
        cursor.execute(select_query)
        employees = cursor.fetchall()
        if employees:
            print("Employees Sorted by Salary (Descending):")
            for employee in employees:
                print("ID:", employee[0])
                print("Name:", employee[1])
                print("Department:", employee[8])
                print("Position:", employee[9])
                print("Salary:", employee[10])
                print("-------------------------")
        else:
            print("No employees found!")
    except Exception as e:
        print("Error:", e)