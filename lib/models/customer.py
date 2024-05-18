from models.__init__ import CURSOR, CONN
from models.employee import Employee

class Customer:
    all = {}

    def __init__(self, name, stock_number, employee_id, id = None):
        self.id = id
        self.name = name
        self.stock_number = stock_number
        self.employee_id = employee_id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and len(value):
            self._name = value
        else:
            raise ValueError("Name must be a string with length greater than 0")
    
    @property
    def stock_number(self):
        return self._stock_number
    
    @stock_number.setter
    def stock_number(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._stock_number = value
        else:
            raise ValueError("Stock Number must be a string with length greater than 0")

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id: int):
        if type(employee_id) is int and Employee.find_by_id(employee_id):
            self._employee_id = employee_id
        else:
            raise ValueError("employee_id must reference an employee in the database")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                name TEXT,
                stock_number TEXT,
                employee_id INTEGER,
                FOREIGN KEY (employee_id) REFERENCES employees(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS customers;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        sql = """
            INSERT INTO customers (name, stock_number, employee_id)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.stock_number, self.employee_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    def update(self):
        sql = """
            UPDATE customers
            SET name = ?, stock_number = ?, employee_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.stock_number, self.employee_id, self.id))
        CONN.commit()


    def delete(self):
        sql = """
            DELETE FROM customers
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
    
    @classmethod
    def create(cls, name: str, stock_number: str, employee_id: int):
        customer = cls(name, stock_number, employee_id)
        customer.save()
        return customer
    
    @classmethod
    def instance_from_db(cls, row):
        customer = cls.all.get(row[0])
        if customer:
            customer.name = row[1]
            customer.stock_number = row[2]
            customer.employee_id = row [3]
        else:
            customer = cls(row[1], row[2], row[3])
            customer.id = row[0]
            cls.all[customer.id] = customer
        return customer
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM customers
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM customers
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name: str):
        sql = """
            SELECT *
            FROM customers
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None