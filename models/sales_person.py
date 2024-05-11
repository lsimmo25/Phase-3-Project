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