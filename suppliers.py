class suppliers:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class _suppliers:
    def __init__(self, conn):
        self._conn = conn
        
    def insert(self, suppliers):
        self._conn.execute("""
               INSERT INTO suppliers (id, name) VALUES (?, ?)
           """, [suppliers.id, suppliers.name])
 
    def find(self, suppliers_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, name FROM suppliers WHERE id = ?
        """, [suppliers_id])
 
        return suppliers(*c.fetchone())
