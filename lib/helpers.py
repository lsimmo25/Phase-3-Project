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
    id_ = input("Enter an employee's ID: ")
    if employee := Employee.find_by_id(id_):
        employee.delete()
        print(f'Employee {id_} deleted')
    else:
        print(f'Employee {id_} not found')

def list_all_customers():
    customers = Customer.get_all()
    for customer in customers:
        print(customer)

def find_customer_by_name():
    name = input("Enter a Customer's name: ")
    customer = Customer.find_by_name(name)
    print(customer) if customer else print(f"No customer's found for that name")

def find_customer_by_id():
    id_ = input("Enter a customer's ID: ")
    customer = Customer.find_by_id(id_)
    print(customer) if customer else print(f"Customer ID not found")

def create_customer():
    name = input("Enter the customer's name: ")
    stock_number = input("Enter the customer's stock number: ")
    try:
        customer = Customer.create(name, stock_number)
        print(f'Success: {customer}')
    except Exception as exc:
        print("Error creating customer: ", exc)  

def update_customer():
    id_ = input("Enter the customer's id: ")
    if customer := Customer.find_by_id(id_):
        try:
            name = input("Enter the customer's new name: ")
            customer.name = name
            stock_number = input("Enter the customer's new stock number: ")
            customer.stock_number = stock_number

            customer.update()
            print(f'Success: {customer}')
        except Exception as exc:
            print("Error updating customer: ", exc)
    else:
        print(f'customer {id_} not found')

def delete_customer():
    id_ = input("Enter the customer's id: ")
    if customer := Customer.find_by_id(id_):
        customer.delete()
        print(f'Customer {id_} deleted')
    else:
        print(f'Customer {id_} not found')

def all_customers_belonging_to_an_employee():
    pass

def exit_program():
    print("Goodbye!")
    exit()