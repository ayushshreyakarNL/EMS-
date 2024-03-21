from functionality import *
from validation import *
import sys
import os


# Define exit key
EXIT_KEY = '\x04'  # Ctrl + D


# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Main function
def main():
    while True:
        clear_screen()
        print("____________________________________________________________")
        # Your menu options here...
        print("Options:")
        print("1. Add employee")
        print("2. View employee details")
        print("3. Update employee information")
        print("4. Delete employee record")
        print("5. List all employees")
        print("6. Calculate total salary at monthly level")
        print("7. Update employee project")
        print("8. View employee's project details")
        print("9. Assign manager to employee")
        print("10. View manager details of any employee")
        print("11. Add tech stack for employees")
        print("12. View employee's known tech stack")
        print("13. Search employees by name")
        print("14. Search employees by tech stack")
        print("15. Search employees by project name")
        print("16. Sort employees by salary")
        print("17. Export data to csv")
        print("18. Import data from csv")
        print("19. Exit")
        try:
            choice = input("Enter your choice : ")

            if choice == "":
                print("Invalid input. Please enter a choice.")
                continue

            if choice == EXIT_KEY:
                print("Exiting...")
                break

            choice = int(choice)

            if choice < 1 or choice > 19:
                print("Invalid choice. Please enter a number between 1 and 19.")
                continue

            if choice == 1:
                add_employee()
            elif choice == 2:
                view_employee_details()
            elif choice == 3:
                update_employee_info()
            elif choice == 4:
                delete_employee_record()
            elif choice == 5:
                list_all_employees()
            elif choice == 6:
                calculate_total_salary()
            elif choice == 7:
                update_employee_project()
            elif choice == 8:
                view_employee_projects()
            elif choice == 9:
                assign_manager()
            elif choice == 10:
                view_manager_details()
            elif choice == 11:
                add_tech_stack()
            elif choice == 12:
                view_employee_tech_stack()
            elif choice == 13:
                search_employee_by_name()
            elif choice == 14:
                search_employee_by_tech_stack()
            elif choice == 15:
                search_employee_by_project()
            elif choice == 16:
                sort_employees_by_salary()
            elif choice == 17:
                export_data_to_csv()
            elif choice == 18:
                add_employees_from_csv()
            elif choice == 19:
                print("Exiting...")
                break
        except EOFError:
            print("Exiting...")
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

        # Wait for the user to press Enter before displaying the menu again
        input("Press Enter to continue...")


if __name__ == "__main__":
    main()
