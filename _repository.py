import sqlite3
import atexit
import sys
from hats import _hats
from suppliers import _suppliers
from orders import _orders


class _repository:    
    def __init__(self):
        self._conn = sqlite3.connect(sys.argv[4])
        self.hats = _hats(self._conn)
        self.suppilers = _suppliers(self._conn)
        self.orders = _orders(self._conn)
 
    def _close(self):
        self._conn.commit()
        self._conn.close()
 
    def create_tables(self):
        self._conn.executescript("""

        CREATE TABLE hats (
            id                 INT     PRIMARY KEY,
            topping     TEXT    NOT NULL,
            supplier INT,
            quantity      INT     NOT NULL,
            FOREIGN KEY(supplier)     REFERENCES suppliers(id)
           

        );


        CREATE TABLE suppliers (
            id      INT         PRIMARY KEY,
            name    TEXT        NOT NULL
        );
 
       
 
        CREATE TABLE orders (
            id      INT     PRIMARY KEY,
            location  TEXT     NOT NULL,
            hat INT,
            FOREIGN KEY(hat)     REFERENCES hats(id)

        );
    """)
 
# the repository singleton
repo = _repository()
atexit.register(repo._close)
