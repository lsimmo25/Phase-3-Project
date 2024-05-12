# lib/helpers.py
from models.sales_person import Sales_person
from models.customer import Customer

def list_all_sales_people():
    sales_people = Sales_person.get_all()
    for sales_person in sales_people:
        print(sales_person)


def exit_program():
    print("Goodbye!")
    exit()