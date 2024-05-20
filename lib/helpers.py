from models.employee import Employee
from models.customer import Customer

def list_all_employees():
    employees = Employee.get_all()
    print("\nEmployees:")
    print("-" * 40)
    for idx, employee in enumerate(employees, start=1):
        print(f"{idx}. Name: {employee.name}, Title: {employee.title}")
    print("-" * 40)

def select_employee():
    employees = Employee.get_all()
    print("\nSelect an Employee:")
    print("-" * 40)
    for idx, employee in enumerate(employees, start=1):
        print(f"{idx}. {employee.name}, Title: {employee.title}")
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
        print(f"\nEmployee: {employee.name}")
        print("-" * 40)
        print("Employee Menu:")
        print("0. Back to Main Menu")
        print("1. View Employee Details")
        print("2. View Employee's Customers")
        print("3. Create Customer for Employee")
        print("4. Update Employee Details")
        print("5. Delete Employee")
        print("6. Update Customer")
        print("7. Delete Customer")
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            view_employee_details(employee)
        elif choice == "2":
            view_employee_customers(employee)
        elif choice == "3":
            create_customer(employee)
        elif choice == "4":
            update_employee(employee)
        elif choice == "5":
            delete_employee(employee)
            break  # Return to main menu after deleting employee
        elif choice == "6":
            update_customer(employee)
        elif choice == "7":
            delete_customer(employee)
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

def create_customer(employee):
    name = input("Enter the customer's name: ")
    stock_number = input("Enter the customer's stock number: ")
    try:
        customer = Customer.create(name, stock_number, employee.id)
        print(f"Success: Customer {customer.name} created and assigned to {employee.name}.")
    except Exception as exc:
        print("Error creating customer: ", exc)

def update_customer(employee):
    customers = employee.customers()
    if not customers:
        print(f"{employee.name} has no active customers to update.")
        return

    print("\nSelect a Customer to Update:")
    print("-" * 40)
    for idx, customer in enumerate(customers, start=1):
        print(f"{idx}. {customer.name}, Stock Number: {customer.stock_number}")
    print("-" * 40)

    choice = input("Enter the number of the customer: ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(customers):
            customer = customers[choice - 1]
            new_name = input(f"Enter the customer's new name (current: {customer.name}): ")
            new_stock_number = input(f"Enter the customer's new stock number (current: {customer.stock_number}): ")
            customer.name = new_name
            customer.stock_number = new_stock_number
            customer.update()
            print(f"Success: Customer {customer.name} updated.")
        else:
            print("Invalid customer number")
    except ValueError:
        print("Invalid input. Please enter a number")

def delete_customer(employee):
    customers = employee.customers()
    if not customers:
        print(f"{employee.name} has no active customers to delete.")
        return

    print("\nSelect a Customer to Delete:")
    print("-" * 40)
    for idx, customer in enumerate(customers, start=1):
        print(f"{idx}. {customer.name}, Stock Number: {customer.stock_number}")
    print("-" * 40)

    choice = input("Enter the number of the customer: ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(customers):
            customer = customers[choice - 1]
            customer.delete()
            print(f"Success: Customer {customer.name} deleted.")
        else:
            print("Invalid customer number")
    except ValueError:
        print("Invalid input. Please enter a number")

def create_employee():
    name = input("Enter the employee's name: ")
    title = input("Enter the employee's title: ")
    try:
        employee = Employee.create(name, title)
        print(f"Success: Employee {employee.name} created.")
    except Exception as exc:
        print("Error creating employee: ", exc)

def update_employee(employee):
    try:
        new_name = input(f"Enter the employee's new name (current: {employee.name}): ")
        new_title = input(f"Enter the employee's new title (current: {employee.title}): ")
        employee.update(new_name, new_title)
        print(f"Success: Employee {employee.name} updated.")
    except Exception as exc:
        print("Error updating employee: ", exc)

def delete_employee(employee):
    customers = employee.customers()

    if customers:
        for customer in customers:
            customer.delete()

    employee.delete()
    print(f'Employee {employee.name} deleted')

def exit_program():
    print("Goodbye!")
    exit()
