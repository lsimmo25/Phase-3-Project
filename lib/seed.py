from models.__init__ import CONN, CURSOR
from models.sales_person import Sales_person
from models.customer import Customer

def seed_database():
    Sales_person.drop_table()
    Sales_person.create_table()

    jim = Sales_person.create("Jim Halpert", "Sales Person")


seed_database()
print("Seeded database")