from models.__init__ import CONN, CURSOR
from models.employee import Employee
from models.customer import Customer

def seed_database():
    Employee.drop_table()
    Employee.create_table()

    jim = Employee.create("Jim Halpert", "Sales Person")


seed_database()
print("Seeded database")