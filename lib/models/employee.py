from models.__init__ import CURSOR, CONN   

class Employee:
    
    all = {}

    approved_titles = ["Sales Person", "Sales Manager", "Finance Manager"]

    def __init__(self, name, title, id=None):
        self.name = name
        self.id = id
        self.title = title
    
    def __repr__(self):
        return f"<Employee {self.id}: {self.name}, {self.title}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a string with length greater than 0")
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if isinstance(value, str) and value in Employee.approved_titles:
            self._title = value
        else:
            raise ValueError("Name must be a string in list of approved titles")
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS employees
            (
            id INTEGER PRIMARY KEY,
            name TEXT,
            title TEXT
            )    
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS employees
        """
        CONN.execute(sql)
        CONN.commit()
    
    def save(self):
        sql = """
            INSERT INTO employees (name, title)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.title))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls, name, title):
        employee = cls(name, title)
        employee.save()
        return employee
    
    def update(self):
        sql = """
            UPDATE employees
            SET name = ?, title = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.title, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM employees
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        
        del type(self).all[self.id]
        self.id = None
    
    @classmethod
    def instance_from_db(cls, row):
        employee = cls.all.get(row[0])
        if employee:
            employee.name = row[1]
            employee.title = row[2]
        else:
            employee = cls(row[1], row[2])
            employee.id = row[0]
            cls.all[employee.id] = employee
        return employee
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM employees
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM employees
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM employees
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def customers(self):
        from models.customer import Customer
        sql = """
            SELECT * FROM employees
            WHERE department_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Customer.instance_from_db(row) for row in rows
        ]       
