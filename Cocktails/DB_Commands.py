import sqlite3
from pathlib import Path


def create_db():
    con = sqlite3.connect("menu.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE alcohol(name, description, price, percentage, size)")
    cur.execute("CREATE TABLE food(name, description, price)")
    cur.execute("CREATE TABLE soft_drink(name, description, price)")
    con.commit()
    con.close()

def add_to_db(category, name, desc, price, perc=0, size=""):
    con = sqlite3.connect("menu.db")
    cur = con.cursor()
    #attr = getattr(menu, item)
    #data = (attr.get_name(), attr.get_desc(), attr.get_perc(), attr.get_price(), attr.get_size())
    if category == "alcohol":
        check_exist = "SELECT * FROM {} WHERE name = '{}' AND size = '{}'".format(category, name, size)
        add_drink = "INSERT INTO {} VALUES ('{}', '{}', {}, {}, '{}')".format(category, name, desc, price, perc, size)
        o = cur.execute(check_exist)
        if len(o.fetchall())>0:
            print("Value already exist if you wish to change go to change value function")
        else:
            cur.execute(add_drink)
    else:
        check_exist = "SELECT * FROM {} WHERE name = '{}'".format(category, name)
        add_product = "INSERT INTO {} VALUES ('{}', '{}', {})".format(category, name, desc, price)
        o = cur.execute(check_exist)
        if len(o.fetchall())>0:
            print("Value already exist if you wish to change go to change value function")
        else:
            cur.execute(add_product)
    con.commit()
    con.close()

def remove_from_db(category, name):
    con = sqlite3.connect("menu.db")
    cur = con.cursor()
    command = "DELETE FROM {} WHERE name='{}'".format(category, name)
    cur.execute(command)
    con.commit()
    con.close()

def update_price(category, name, new_price, size=""):
    con = sqlite3.connect("menu.db")
    cur = con.cursor()
    command = "UPDATE {} SET price={} WHERE name='{}' AND size='{}'".format(category, new_price, name, size)
    cur.execute(command)
    #data = (new_price, name, size)
    #cur.execute("UPDATE alcohol SET price=? WHERE name=?AND size=?",data)
    con.commit()
    con.close()
    


db_path = Path("menu.db")
if not db_path.is_file():
    create_db()

#add_to_db("alcohol", "Shikma", "Fine Israeli beer", 20, 5, "Third")
#add_to_db("alcohol", "Shikma", "Fine Israeli beer", 33, 5, "Half")
#add_to_db("alcohol", "Goldstar", "Fine Israeli beer", 30, 5, "Third")
#add_to_db("food", "Adamame", "idk", 30)
#add_to_db("food", "Chips", "idk", 30)
#add_to_db("soft_drink", "Cola", "Not realy tasty", 9)
#add_to_db("soft_drink", "Fuzetea", "nice", 9)
#remove_from_db("soft_drink", "Fuze tea")
#remove_from_db("alcohol", "Goldstar")
#update_price("alcohol", "Shikma", 20, "Third")