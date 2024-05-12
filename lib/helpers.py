# lib/helpers.py
from models.sales_person import Sales_person
from models.customer import Customer

def list_all_sales_people():
    sales_people = Sales_person.get_all()
    for sales_person in sales_people:
        print(sales_person)

def find_sales_person_by_name():
    name = input("Enter a sales person's name: ")
    sales_person = Sales_person.find_by_name(name)
    print(sales_person) if sales_person else print(f"No sales people found for that name")

def find_sales_person_by_id():
    id_ = input("Enter a sales person's ID: ")
    sales_person = Sales_person.find_by_id(id_)
    print(sales_person) if sales_person else print(f"Sales Person ID not found")

def create_sales_person():
    name = input("Enter the sales person's name: ")
    title = input("Enter the sales person's title: ")
    try:
        sales_person = Sales_person.create(name, title)
        print(f"Success: {sales_person}")
    except Exception as exc:
        print("Error creating sales person: ", exc)

def update_sales_person():
    pass

def delete_sales_person():
    pass


def exit_program():
    print("Goodbye!")
    exit()