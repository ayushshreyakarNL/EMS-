import re
from datetime import datetime, timedelta

# Validate mobile number
def validate_mobile_number(mobile_number):
    if re.match(r'^[0-9]{10}$', mobile_number):
        return True
    else:
        return False

# Validate age
def validate_age(age):
    try:
        age = int(age)
        if age >= 18 and age <= 100:  # Assuming reasonable age limits
            return True
        else:
            return False
    except ValueError:
        return False

# Validate salary
def validate_salary(salary):
    try:
        salary = float(salary)
        if salary >= 0:  # Assuming salary cannot be negative
            return True
        else:
            return False
    except ValueError:
        return False

# Validate employee ID
def validate_employee_id(employee_id):
    try:
        employee_id = int(employee_id)
        if employee_id > 0:  # Assuming employee IDs start from 1
            return True
        else:
            return False
    except ValueError:
        return False

# Validate gender
def validate_gender(gender):
    return gender.lower() in ['male', 'female', 'other']