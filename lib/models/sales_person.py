from models.__init__ import CURSOR, CONN   

class Sales_person:
    
    all = {}

    approved_titles = ["sales_person", "sales_manager", "finance_manager"]

    def __init__(self, name, title, id=None):
        self.name = name
        self.id = id
        self.title = title
    
    def __repr__(self):
        return f"<SalesPerson {self.id}: {self.name}, {self.title}"
    
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
        if isinstance(value, str) and value in Sales_person.approved_titles:
            self._name = value
        else:
            raise ValueError("Name must be a string in list of approved titles")
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS sales_people
            (
            id INTEGER PRIMARY KEY,
            name TEXT
            title TEXT
            )    
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS sales_people
        """
        CONN.execute(sql)
        CONN.commit()
    
    def save(self):
        sql = """
            INSERT INTO sales_people (name, title)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.title))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls, name, title):
        sales_person = cls(name, title)
        sales_person.save()
        return sales_person
    
    def update(self):
        sql = """
            UPDATE sales_people
            SET name = ?, title = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.title, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM sales_people
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        
        del type(self).all[self.id]
        self.id = None
    
    @classmethod
    def instance_from_db(cls, row):
        sales_person = cls.all.get(row[0])
        if sales_person:
            sales_person.name = row[1]
            sales_person.title = row[2]
        else:
            sales_person = cls(row[1], row[2])
            sales_person.id = row[0]
            cls.all[sales_person.id] = sales_person
        return sales_person
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM sales_people
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM sales_people
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
