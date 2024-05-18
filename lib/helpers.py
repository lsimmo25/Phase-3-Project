# lib/helpers.py

from models.employee import Employee

def list_all_employees():
    employees = Employee.get_all()
    print("\nEmployees:")
    print("-" * 40)
    for employee in employees:
        print(f"Name: {employee.name}, Title: {employee.title}")
    print("-" * 40)

def select_employee():
    employees = Employee.get_all()
    print("\nSelect an Employee:")
    print("-" * 40)
    for idx, employee in enumerate(employees, start=1):
        print(f"{idx}. *{employee.name}*, Title: {employee.title}")
    print("-" * 40)
    
    choice = input("Enter the number of the employee: ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(employees):
            employee = employees[choice - 1]
            employee_menu(employee)
        else:
            print("Invalid employee number")
    except ValueError:
        print("Invalid input. Please enter a number")

def employee_menu(employee):
    while True:
        print(f"\nEmployee: *{employee.name}*")
        print("-" * 40)
        print("Employee Menu:")
        print("0. Back to Main Menu")
        print("1. View Employee Details")
        print("2. View Employee's Customers")
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            view_employee_details(employee)
        elif choice == "2":
            view_employee_customers(employee)
        else:
            print("Invalid choice")

def view_employee_details(employee):
    print("\nEmployee Details:")
    print("-" * 40)
    print(f"Name: {employee.name}")
    print(f"Title: {employee.title}")
    print("-" * 40)

def view_employee_customers(employee):
    customers = employee.customers()
    if customers:
        print(f"\nCustomers of {employee.name}:")
        print("-" * 40)
        for customer in customers:
            print(f"Name: {customer.name}, Stock Number: {customer.stock_number}")
        print("-" * 40)
    else:
        print(f"{employee.name} has no active customers")


def exit_program():
    print("Goodbye!")
    exit()