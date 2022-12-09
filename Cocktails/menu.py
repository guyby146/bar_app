import sqlite3
from pathlib import Path
import DB_Commands
"""
def create_db():
    con = sqlite3.connect("menu.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE alcohol(name, description, price, percentage, size)")
    con.commit()
    con.close()

db_path = Path("menu.db")
if not db_path.is_file():
    create_db()
"""
class product():
    def __init__(self, name="unknown", description="unknown", price=0) -> None:
        self._name = name
        self._desc = description
        self._price = price
    
    def get_name(self):
        return self._name
    
    def get_desc(self):
        return self._desc
    
    def get_price(self):
        return self._price

    def change_name(self, name=""):
        if name == "":
            print("invalid name")
        else:
            self._name = name
    def change_desc(self, desc=""):
        if desc == "":
            print("invalid description")
        else:
            self._desc = desc
    def change_price(self, price=-1):
        if price < 0:
            print("invalid price")
        else:
            self._price = price

class alcohol(product):
    def __init__(self, name="unknown", description="unknown", price=0, percentage=0, size = "regular") -> None:
        super().__init__(name, description, price)
        self._perc = percentage
        self._size = size
    
    def get_perc(self):
        return self._perc
    
    def get_size(self):
        return self._size
    
    def change_perc(self, new_percentage = "0"):
        self._perc = new_percentage
    
    def change_size(self, new_size = "regular"):
        self._size = new_size



"""
exec("Goldstar" + ' = alcohol("Goldstar", "Fine Israeli beer", 30, 5, "Third")')
exec("Shikma" + ' = alcohol("Shikma", "Fine Israeli beer", 30, 5, "Third")')
print(globals()['Goldstar'].get_name())
"""

alcohol_list = []
food_list = []
soft_drinks_list = []

def load_menu():
    db_path = Path("menu.db")
    if db_path.is_file():
        con = sqlite3.connect("menu.db")
        cur = con.cursor()
        for drink in cur.execute("SELECT * FROM alcohol"):
            command = 'global {}; {} = alcohol("{}", "{}", {}, {}, "{}")'.format(drink[4]+drink[0],drink[4]+drink[0], drink[0], drink[1],drink[2],drink[3],drink[4])
            exec(command)
            alcohol_list.append(globals()[drink[4]+drink[0]])
            #print(globals()[drink[4]+drink[0]].get_name())
        for plate in cur.execute("SELECT * FROM food"):
            command = 'global {}; {} = product("{}", "{}", {})'.format(plate[0],plate[0], plate[0], plate[1], plate[2])
            exec(command)
            food_list.append(globals()[plate[0]])

        for drink in cur.execute("SELECT * FROM soft_drink"):
            command = 'global {}; {} = product("{}", "{}", {})'.format(drink[0],drink[0], drink[0], drink[1], drink[2])
            exec(command)
            soft_drinks_list.append(globals()[drink[0]])
            #print(globals()[plate[0]].get_name())
        con.commit()
        con.close()

load_menu()
print(alcohol_list)
print(food_list)
print(soft_drinks_list)
#print (ThirdShikma.get_price())
#print (HalfShikma.get_price())
#print (Adamame.get_price())


