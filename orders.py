class orders:
    def __init__(self, id, location,hat):
        self.id = id
        self.location = location
        self.hat = hat
        
class _orders:
    def __init__(self, conn):
        self._conn = conn
 
    def insert(self, orders):
        self._conn.execute("""
               INSERT INTO orders (id,location,hat) VALUES (?,?,?)
           """, [orders.id, orders.location,orders.hat])
 
    def find(self, orders_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, location,hat FROM orders WHERE id = ?
        """, [orders_id])
 
        return orders(*c.fetchone())    
