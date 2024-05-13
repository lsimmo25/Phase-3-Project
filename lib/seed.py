from models.__init__ import CONN, CURSOR
from models.employee import Employee
from models.customer import Customer

def seed_database():
    Employee.drop_table()
    Customer.drop_table()
    Employee.create_table()
    Customer.create_table()

    jim = Employee.create("Jim Halpert", "Sales Person")
    dwight = Employee.create("Dwight Schrute", "Finance Person")
    michael = Employee.create("Michael Scott", "Sales Manager")

    ron = Customer.create("Ron Swanson", "P001", michael.id)
    april = Customer.create("April Ludgate", "P002", michael.id)
    leslie = Customer.create("Leslie Knope", "P003", jim.id)
    andy = Customer.create("Andy Dwyer", "P004", dwight.id)


seed_database()
print("Seeded database")