import tkinter as tk
from tkinter import messagebox, simpledialog
import mysql.connector
from datetime import datetime, timedelta

# Connect to MySQL server
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ayush@12345",
    database="emsg"
)

# Create a cursor object
cursor = db_connection.cursor()


# Function to add a new employee
def add_employee():
    name = name_entry.get()
    age = age_entry.get()
    address = address_entry.get()
    gender = gender_var.get()
    education_details = education_entry.get()
    doj = doj_entry.get()
    department = department_entry.get()
    position = position_entry.get()
    annual_salary = annual_salary_entry.get()
    project = project_entry.get()
    manager = manager_entry.get()
    tech_stack = tech_stack_entry.get()
    mobile_number = mobile_number_entry.get()

    try:
        doj = datetime.strptime(doj, "%Y-%m-%d").date()
        annual_salary = float(annual_salary)
    except ValueError:
        messagebox.showerror("Error", "Invalid input")
        return

    insert_query = """
    INSERT INTO employees (name, age, address, mobile_number, gender, education_details, doj, department, position, annual_salary, project, manager, tech_stack)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    data = (
        name, age, address, mobile_number, gender, education_details, doj, department, position, annual_salary,
        project,
        manager, tech_stack)
    cursor.execute(insert_query, data)
    db_connection.commit()
    messagebox.showinfo("Success", "Employee added successfully!")


# Function to view a particular employee’s details
# Function to view a particular employee’s details
def view_employee_details():
    while True:
        try:
            employee_id = simpledialog.askinteger("Employee ID", "Enter employee ID:")
            select_query = "SELECT * FROM employees WHERE id = %s"
            cursor.execute(select_query, (employee_id,))
            employee = cursor.fetchone()
            if employee:
                details = (
                    f"ID: {employee[0]}\n"
                    f"Name: {employee[1]}\n"
                    f"Age: {employee[2]}\n"
                    f"Address: {employee[3]}\n"
                    f"Mobile Number: {employee[4]}\n"
                    f"Gender: {employee[5]}\n"
                    f"Education Details: {employee[6]}\n"
                    f"Date of Joining: {employee[7]}\n"
                    f"Department: {employee[8]}\n"
                    f"Position: {employee[9]}\n"
                    f"Annual Salary: {employee[10]}\n"
                    f"Project: {employee[11]}\n"
                    f"Manager: {employee[12]}\n"
                    f"Tech Stack: {employee[13]}"
                )
                messagebox.showinfo("Employee Details", details)
                break
            else:
                messagebox.showerror("Error", "Employee not found. Please enter a valid Employee ID.")
        except ValueError:
            messagebox.showerror("Error", "Invalid Employee ID. Please enter a valid ID.")

def update_employee_info():
    employee_id = int(employee_id_update_entry.get())
    select_query = "SELECT * FROM employees WHERE id = %s"
    cursor.execute(select_query, (employee_id,))
    employee = cursor.fetchone()
    if employee:
        update_window = tk.Toplevel()
        update_window.title("Update Employee Information")

        # Labels
        tk.Label(update_window, text="Age:").grid(row=0, column=0, sticky="e")
        tk.Label(update_window, text="Address:").grid(row=1, column=0, sticky="e")
        tk.Label(update_window, text="Gender:").grid(row=2, column=0, sticky="e")
        tk.Label(update_window, text="Education Details:").grid(row=3, column=0, sticky="e")
        tk.Label(update_window, text="Date of Joining (YYYY-MM-DD):").grid(row=4, column=0, sticky="e")
        tk.Label(update_window, text="Department:").grid(row=5, column=0, sticky="e")
        tk.Label(update_window, text="Position:").grid(row=6, column=0, sticky="e")
        tk.Label(update_window, text="Annual Salary:").grid(row=7, column=0, sticky="e")
        tk.Label(update_window, text="Project:").grid(row=8, column=0, sticky="e")
        tk.Label(update_window, text="Manager:").grid(row=9, column=0, sticky="e")
        tk.Label(update_window, text="Tech Stack:").grid(row=10, column=0, sticky="e")
        tk.Label(update_window, text="Mobile Number:").grid(row=11, column=0, sticky="e")

        # Entries
        age_entry = tk.Entry(update_window)
        age_entry.grid(row=0, column=1)
        address_entry = tk.Entry(update_window)
        address_entry.grid(row=1, column=1)
        gender_var = tk.StringVar(update_window)
        gender_var.set(employee[5])
        gender_menu = tk.OptionMenu(update_window, gender_var, "Male", "Female", "Other")
        gender_menu.grid(row=2, column=1)
        education_entry = tk.Entry(update_window)
        education_entry.grid(row=3, column=1)
        doj_entry = tk.Entry(update_window)
        doj_entry.grid(row=4, column=1)
        department_entry = tk.Entry(update_window)
        department_entry.grid(row=5, column=1)
        position_entry = tk.Entry(update_window)
        position_entry.grid(row=6, column=1)
        annual_salary_entry = tk.Entry(update_window)
        annual_salary_entry.grid(row=7, column=1)
        project_entry = tk.Entry(update_window)
        project_entry.grid(row=8, column=1)
        manager_entry = tk.Entry(update_window)
        manager_entry.grid(row=9, column=1)
        tech_stack_entry = tk.Entry(update_window)
        tech_stack_entry.grid(row=10, column=1)
        mobile_number_entry = tk.Entry(update_window)
        mobile_number_entry.grid(row=11, column=1)

        # Populate existing data
        age_entry.insert(0, employee[2])
        address_entry.insert(0, employee[3])
        education_entry.insert(0, employee[6])
        doj_entry.insert(0, employee[7])
        department_entry.insert(0, employee[8])
        position_entry.insert(0, employee[9])
        annual_salary_entry.insert(0, employee[10])
        project_entry.insert(0, employee[11])
        manager_entry.insert(0, employee[12])
        tech_stack_entry.insert(0, employee[13])

        def submit_update():
            age = age_entry.get()
            address = address_entry.get()
            gender = gender_var.get()
            education_details = education_entry.get()
            doj = doj_entry.get()
            department = department_entry.get()
            position = position_entry.get()
            annual_salary = annual_salary_entry.get()
            project = project_entry.get()
            manager = manager_entry.get()
            tech_stack = tech_stack_entry.get()
            mobile_number = mobile_number_entry.get()

            try:
                doj = datetime.strptime(doj, "%Y-%m-%d").date()
                annual_salary = float(annual_salary)
            except ValueError:
                messagebox.showerror("Error", "Invalid input")
                return

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
            messagebox.showinfo("Success", "Employee information updated successfully!")
            update_window.destroy()

        # Submit button
        submit_button = tk.Button(update_window, text="Submit", command=submit_update)
        submit_button.grid(row=12, column=0, columnspan=2)

    else:
        messagebox.showerror("Error", "Employee not found. Please enter a valid Employee ID.")


# Function to delete an employee record
# Function to delete an employee record
# Function to delete an employee record
def delete_employee_record():
    while True:
        try:
            employee_id = simpledialog.askinteger("Employee ID", "Enter employee ID:")
            select_query = "SELECT doj FROM employees WHERE id = %s"
            cursor.execute(select_query, (employee_id,))
            date_of_joining = cursor.fetchone()
            if date_of_joining:
                date_of_joining = date_of_joining[0]
                today = datetime.now().date()
                if today - date_of_joining > timedelta(days=30):
                    delete_query = "DELETE FROM employees WHERE id = %s"
                    cursor.execute(delete_query, (employee_id,))
                    db_connection.commit()
                    messagebox.showinfo("Success", "Employee record deleted successfully!")
                    break
                else:
                    messagebox.showerror("Error", "Employee has worked for less than 1 month. Cannot delete record.")
                    break
            else:
                messagebox.showerror("Error", "Employee not found. Please enter a valid Employee ID.")
        except ValueError:
            messagebox.showerror("Error", "Invalid Employee ID. Please enter a valid ID.")

def calculate_total_salary():
    select_query = "SELECT id, annual_salary FROM employees"
    cursor.execute(select_query)
    employees = cursor.fetchall()
    if employees:
        salary_details = "Monthly Total Salary:\n"
        for employee in employees:
            monthly_salary = employee[1] / 12
            salary_details += f"Employee ID {employee[0]}: {monthly_salary}\n"
        messagebox.showinfo("Total Salary", salary_details)
    else:
        messagebox.showinfo("Total Salary", "No employees found!")


def list_all_employees():
    select_query = "SELECT name, department, position, gender FROM employees"
    cursor.execute(select_query)
    employees = cursor.fetchall()
    if employees:
        employee_details = "All Employees:\n"
        for employee in employees:
            employee_details += f"Name: {employee[0]}\nDepartment: {employee[1]}\nPosition: {employee[2]}\nGender: {employee[3]}\n-------------------------\n"
        messagebox.showinfo("All Employees", employee_details)
    else:
        messagebox.showinfo("All Employees", "No employees found!")


def view_employee_projects():
    while True:
        try:
            employee_id = int(simpledialog.askinteger("Employee ID", "Enter employee ID: "))
            select_query = "SELECT project FROM employees WHERE id = %s"
            cursor.execute(select_query, (employee_id,))
            result = cursor.fetchone()
            if result:
                projects = result[0]
                if projects:
                    messagebox.showinfo("Employee Projects", f"Projects assigned to Employee ID {employee_id}:\n{projects}")
                else:
                    messagebox.showinfo("Employee Projects", f"No projects assigned to Employee ID {employee_id}")
                break
            else:
                messagebox.showerror("Error", "Employee not found or has no projects assigned.")
        except ValueError:
            messagebox.showerror("Error", "Invalid Employee ID. Please enter a valid ID.")


def assign_project():
    while True:
        try:
            employee_id = int(simpledialog.askinteger("Employee ID", "Enter employee ID: "))
            select_query = "SELECT name FROM employees WHERE id = %s"
            cursor.execute(select_query, (employee_id,))
            if cursor.fetchone():
                new_project = simpledialog.askstring("New Project", "Enter new project: ")

                update_query = "UPDATE employees SET project = CONCAT(project, ', ', %s) WHERE id = %s"
                cursor.execute(update_query, (new_project, employee_id))
                db_connection.commit()
                messagebox.showinfo("Success", "Project assigned successfully!")
                break
            else:
                messagebox.showerror("Error", "Employee ID not found. Please enter a valid ID.")
        except ValueError:
            messagebox.showerror("Error", "Invalid Employee ID. Please enter a valid ID.")


def assign_manager():
    while True:
        try:
            employee_id = int(simpledialog.askinteger("Employee ID", "Enter employee ID: "))
            select_query = "SELECT name FROM employees WHERE id = %s"
            cursor.execute(select_query, (employee_id,))
            if cursor.fetchone():
                manager_name = simpledialog.askstring("Manager's Name", "Enter manager's name: ")

                update_query = "UPDATE employees SET manager = %s WHERE id = %s"
                cursor.execute(update_query, (manager_name, employee_id))
                db_connection.commit()
                messagebox.showinfo("Success", "Manager assigned successfully!")
                break
            else:
                messagebox.showerror("Error", "Employee ID not found. Please enter a valid ID.")
        except ValueError:
            messagebox.showerror("Error", "Invalid Employee ID. Please enter a valid ID.")

def view_manager_details():
    while True:
        try:
            manager_name = simpledialog.askstring("Manager's Name", "Enter manager's name: ")
            select_query = "SELECT name FROM employees WHERE manager = %s"
            cursor.execute(select_query, (manager_name,))
            mentees = cursor.fetchall()
            if mentees:
                mentees_list = "\n".join([mentee[0] for mentee in mentees])
                messagebox.showinfo("Manager Details", f"Manager: {manager_name}\nMentees:\n{mentees_list}")
                break
            else:
                messagebox.showinfo("No Mentees", "No employees are mentored by this manager.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

def add_tech_stack():
    while True:
        try:
            employee_id = simpledialog.askinteger("Employee ID", "Enter employee ID:")
            select_query = "SELECT name, education_details, tech_stack FROM employees WHERE id = %s"
            cursor.execute(select_query, (employee_id,))
            employee = cursor.fetchone()
            if employee:
                name, education_details, current_tech_stack = employee
                if "B.Tech" in education_details or "M.Tech" in education_details:
                    new_tech_stack = simpledialog.askstring("Tech Stack", "Enter tech stack to add:")
                    if current_tech_stack:
                        updated_tech_stack = current_tech_stack + ', ' + new_tech_stack
                    else:
                        updated_tech_stack = new_tech_stack

                    update_query = "UPDATE employees SET tech_stack = %s WHERE id = %s"
                    cursor.execute(update_query, (updated_tech_stack, employee_id))
                    db_connection.commit()
                    messagebox.showinfo("Success", "Tech stack added successfully!")
                else:
                    messagebox.showerror("Error", f"{name} is not an engineer. Tech stack cannot be added.")
                break
            else:
                messagebox.showerror("Error", "Employee ID not found. Please enter a valid ID.")
        except ValueError:
            messagebox.showerror("Error", "Invalid Employee ID. Please enter a valid ID.")

def view_employee_tech_stack():
    while True:
        try:
            employee_id = simpledialog.askinteger("Employee ID", "Enter employee ID:")
            select_query = "SELECT name, education_details, tech_stack FROM employees WHERE id = %s"
            cursor.execute(select_query, (employee_id,))
            employee = cursor.fetchone()
            if employee:
                name, education_details, tech_stack = employee
                if "B.Tech" in education_details or "M.Tech" in education_details:
                    messagebox.showinfo("Tech Stack", f"Tech Stack for {name}: {tech_stack}")
                else:
                    messagebox.showerror("Error", f"{name} is not an engineer.")
                break
            else:
                messagebox.showerror("Error", "Employee ID not found. Please enter a valid ID.")
        except ValueError:
            messagebox.showerror("Error", "Invalid Employee ID. Please enter a valid ID.")

def search_employee_by_name():
    while True:
        try:
            employee_name = simpledialog.askstring("Employee Name", "Enter employee name:")
            select_query = "SELECT * FROM employees WHERE name LIKE %s"
            cursor.execute(select_query, ('%' + employee_name + '%',))
            employees = cursor.fetchall()
            if employees:
                info = ""
                for employee in employees:
                    info += f"ID: {employee[0]}\nName: {employee[1]}\nDepartment: {employee[8]}\nPosition: {employee[9]}\nGender: {employee[5]}\n-------------------------\n"
                messagebox.showinfo("Matching Employees", info)
                break
            else:
                messagebox.showinfo("No Matching Employees", "No matching employees found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Function to search employee by tech stack
def search_employee_by_tech_stack():
    while True:
        try:
            tech_stack = simpledialog.askstring("Tech Stack", "Enter tech stack:")
            select_query = "SELECT * FROM employees WHERE tech_stack LIKE %s"
            cursor.execute(select_query, ('%' + tech_stack + '%',))
            employees = cursor.fetchall()
            if employees:
                info = ""
                for employee in employees:
                    info += f"ID: {employee[0]}\nName: {employee[1]}\nDepartment: {employee[8]}\nPosition: {employee[9]}\nGender: {employee[5]}\n-------------------------\n"
                messagebox.showinfo("Employees with Tech Stack", info)
                break
            else:
                messagebox.showinfo("No Matching Employees", "No employees found with the specified tech stack.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Function to search employee by project
def search_employee_by_project():
    while True:
        try:
            project_name = simpledialog.askstring("Project Name", "Enter project name:")
            select_query = "SELECT * FROM employees WHERE project LIKE %s"
            cursor.execute(select_query, ('%' + project_name + '%',))
            employees = cursor.fetchall()
            if employees:
                info = ""
                for employee in employees:
                    info += f"ID: {employee[0]}\nName: {employee[1]}\nDepartment: {employee[8]}\nPosition: {employee[9]}\nGender: {employee[5]}\n-------------------------\n"
                messagebox.showinfo("Employees Assigned to Project", info)
                break
            else:
                messagebox.showinfo("No Employees Found", f"No employees found assigned to the specified project: {project_name}.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

def sort_employees_by_salary():
    try:
        select_query = "SELECT * FROM employees ORDER BY annual_salary DESC"
        cursor.execute(select_query)
        employees = cursor.fetchall()
        if employees:
            info = ""
            for employee in employees:
                info += f"ID: {employee[0]}\nName: {employee[1]}\nDepartment: {employee[8]}\nPosition: {employee[9]}\nSalary: {employee[10]}\n-------------------------\n"
            messagebox.showinfo("Employees Sorted by Salary (Descending)", info)
        else:
            messagebox.showinfo("No Employees Found", "No employees found!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI
root = tk.Tk()
root.title("Employee Management System")

# Labels and Entries for adding new employee
tk.Label(root, text="Name:").grid(row=0, column=0, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)
tk.Label(root, text="Age:").grid(row=1, column=0, sticky="e")
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1)
tk.Label(root, text="Address:").grid(row=2, column=0, sticky="e")
address_entry = tk.Entry(root)
address_entry.grid(row=2, column=1)
tk.Label(root, text="Gender:").grid(row=3, column=0, sticky="e")
gender_var = tk.StringVar(root)
gender_var.set("Male")
gender_menu = tk.OptionMenu(root, gender_var, "Male", "Female", "Other")
gender_menu.grid(row=3, column=1)
tk.Label(root, text="Education Details:").grid(row=4, column=0, sticky="e")
education_entry = tk.Entry(root)
education_entry.grid(row=4, column=1)
tk.Label(root, text="Date of Joining (YYYY-MM-DD):").grid(row=5, column=0, sticky="e")
doj_entry = tk.Entry(root)
doj_entry.grid(row=5, column=1)
tk.Label(root, text="Department:").grid(row=6, column=0, sticky="e")
department_entry = tk.Entry(root)
department_entry.grid(row=6, column=1)
tk.Label(root, text="Position:").grid(row=7, column=0, sticky="e")
position_entry = tk.Entry(root)
position_entry.grid(row=7, column=1)
tk.Label(root, text="Annual Salary:").grid(row=8, column=0, sticky="e")
annual_salary_entry = tk.Entry(root)
annual_salary_entry.grid(row=8, column=1)
tk.Label(root, text="Project:").grid(row=9, column=0, sticky="e")
project_entry = tk.Entry(root)
project_entry.grid(row=9, column=1)
tk.Label(root, text="Manager:").grid(row=10, column=0, sticky="e")
manager_entry = tk.Entry(root)
manager_entry.grid(row=10, column=1)
tk.Label(root, text="Tech Stack:").grid(row=11, column=0, sticky="e")
tech_stack_entry = tk.Entry(root)
tech_stack_entry.grid(row=11, column=1)
tk.Label(root, text="Mobile Number:").grid(row=12, column=0, sticky="e")
mobile_number_entry = tk.Entry(root)
mobile_number_entry.grid(row=12, column=1)

# Submit button
submit_button = tk.Button(root, text="Submit", command=add_employee)
submit_button.grid(row=13, column=0, columnspan=4)

# View Employee Details
view_details_button = tk.Button(root, text="View Details", command=view_employee_details)
view_details_button.grid(row=16, column=0, columnspan=2)

# Update Employee Information
tk.Label(root, text="Enter Employee ID to Update Info:").grid(row=15, column=0, sticky="e")
employee_id_update_entry = tk.Entry(root)
employee_id_update_entry.grid(row=15, column=1)
update_info_button = tk.Button(root, text="Update Info", command=update_employee_info)
update_info_button.grid(row=15, column=2)

# Button to delete employee record
delete_button = tk.Button(root, text="Delete Record", command=delete_employee_record)
delete_button.grid(row=16, column=2, columnspan=2)


# Calculate Total Salary
total_salary_button = tk.Button(root, text="Calculate Total Salary", command=calculate_total_salary)
total_salary_button.grid(row=17, column=0, columnspan=2)

# List All Employees
list_employees_button = tk.Button(root, text="List All Employees", command=list_all_employees)
list_employees_button.grid(row=17, column=2)

# View Employee Projects
view_projects_button = tk.Button(root, text="View Employee Projects", command=view_employee_projects)
view_projects_button.grid(row=18, column=0, columnspan=2)

# Assign Project
assign_project_button = tk.Button(root, text="Assign Project", command=assign_project)
assign_project_button.grid(row=18, column=2)
assign_manager_button = tk.Button(root, text="Assign Manager", command=assign_manager)
assign_manager_button.grid(row=19, column=0, columnspan=2)
view_manager_button = tk.Button(root, text="View Manager Details", command=view_manager_details)
view_manager_button.grid(row=19, column=2, columnspan=2)
add_tech_stack_button = tk.Button(root, text="Add Tech Stack", command=add_tech_stack)
add_tech_stack_button.grid(row=20, column=0, columnspan=2)
view_tech_stack_button = tk.Button(root, text="View Tech Stack", command=view_employee_tech_stack)
view_tech_stack_button.grid(row=20, column=2, columnspan=2)
search_by_name_button = tk.Button(root, text="Search by Name", command=search_employee_by_name)
search_by_name_button.grid(row=21, column=0, columnspan=2)
search_by_tech_stack_button = tk.Button(root, text="Search by Tech Stack", command=search_employee_by_tech_stack)
search_by_tech_stack_button.grid(row=21, column=2, columnspan=2)
search_by_project_button = tk.Button(root, text="Search by Project", command=search_employee_by_project)
search_by_project_button.grid(row=22, column=0, columnspan=2)
sort_by_salary_button = tk.Button(root, text="Sort by Salary", command=sort_employees_by_salary)
sort_by_salary_button.grid(row=22, column=2, columnspan=2)
root.mainloop()


# Close cursor and connection
cursor.close()
db_connection.close()
