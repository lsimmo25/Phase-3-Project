from models.__init__ import CURSOR, CONN   

class Sales_person:
    
    all = {}

    def __init__(self, name, id=None):
        self.name = name
        self.id = id
    
    def __repr__(self):
        return f"<SalesPerson {self.id}: {self.name}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a string with length greater than 0")
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS sales_people
            (
            id INTEGER PRIMARY KEY,
            name TEXT
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
            INSERT INTO sales_people (name)
            VALUES (?, )
        """
        CURSOR.execute(sql, (self.name, ))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls, name):
        sales_person = cls(name)
        sales_person.save()
        return sales_person
    
    def update(self):
        sql = """
            UPDATE sales_people
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM sales_people
            WHERE id = ?
        """

        del type(self).all[self.id]
        self.id = None