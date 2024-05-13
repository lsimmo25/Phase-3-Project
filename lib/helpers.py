# lib/helpers.py
from models.employee import Employee
from models.customer import Customer

def list_all_employee():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)

def find_employee_by_name():
    name = input("Enter a employee's name: ")
    employee = Employee.find_by_name(name)
    print(employee) if employee else print(f"No employee's found for that name")

def find_employee_by_id():
    id_ = input("Enter a employee's ID: ")
    employee = Employee.find_by_id(id_)
    print(employee) if employee else print(f"Employee ID not found")

def create_employee():
    name = input("Enter the employee's name: ")
    title = input("Enter the employee's title: ")
    try:
        employee = Employee.create(name, title)
        print(f"Success: {employee}")
    except Exception as exc:
        print("Error creating employee: ", exc)

def update_employee():
    id_ = input("Enter an employee's ID: ")
    if employee := Employee.find_by_id(id_):
        try:
            name = input("Enter the employees new name: ")
            employee.name = name
            title = input("Enter the employee's new title: ")
            employee.title = title
            employee.update()
            print(f"Success: {employee}")
        except Exception as exc:
            print(f"Error updating employee: ", exc)
    else:
        print(f"Employee {id_} not found")

def delete_employee():
    pass


def exit_program():
    print("Goodbye!")
    exit()