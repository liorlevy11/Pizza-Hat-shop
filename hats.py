class hats:
    def __init__(self, id, topping,supplier,quantity):
        self.id = id
        self.topping = topping
        self.supplier = supplier
        self.quantity = quantity   


class _hats:
    def __init__(self,conn):
        self._conn = conn 

    def insert(self, hats):
        self._conn.execute("""
               INSERT INTO hats (id,topping,supplier,quantity) VALUES (?,?,?,?)
           """, [hats.id, hats.topping,hats.supplier,hats.quantity])
 
    def find(self, hats_topping):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, topping,supplier,quantity
            FROM hats
            WHERE topping = ?
            ORDER BY supplier ASC
            LIMIT 1
        """, [hats_topping])
        return hats(*c.fetchone())


    def update(self, hats):
        self._conn.execute("""
               UPDATE hats SET quantity=(?) WHERE id=(?)
           """, [hats.quantity-1, hats.id]) 


    def delete(self,hats):
        self._conn.execute("""
               DELETE FROM hats WHERE id=?     
        """, [hats.id])             
