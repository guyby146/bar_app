import sqlite3
from pathlib import Path
from datetime import date
import os
import time

filename = "users.db"
date_today = str(date.today()).replace("-","_")
table_name = "user"+date_today
counter = 0
modificationTime = time.strftime('%Y_%m_%d', time.localtime(os.path.getmtime(filename)))

def create_db():
    con = sqlite3.connect(filename)
    cur = con.cursor()
    create_commmand = "CREATE TABLE {}(name, order_num, amount, open)".format(table_name)
    cur.execute(create_commmand)
    con.commit()
    con.close()


def add_to_db(name, order_num, amount, open):
    con = sqlite3.connect(filename)
    cur = con.cursor()
    check_exist = "SELECT * FROM {} WHERE order_num = {}".format(table_name, str(counter+order_num))
    result = cur.execute(check_exist)
    exist = len(result.fetchall())>0
    print(open)
    if exist:
        if open==False:
            close_bill(str(counter+order_num))
            print('closing')
        else:
            update_amount(str(counter+order_num), amount)
    else:
        add_user = "INSERT INTO {} VALUES ('{}', {}, {}, {})".format(table_name, name, str(counter+order_num), amount, open)
        cur.execute(add_user)
    con.commit()
    con.close()

def remove_from_db(order_num):
    con = sqlite3.connect(filename)
    cur = con.cursor()
    command = "DELETE FROM {} WHERE order_num={}".format(table_name, str(counter+order_num))
    cur.execute(command)
    con.commit()
    con.close()

def close_bill(order_num):
    con = sqlite3.connect(filename)
    cur = con.cursor()
    command = "UPDATE {} SET open={} WHERE order_num={}".format(table_name, False, order_num)
    cur.execute(command)
    con.commit()
    con.close()

def update_amount(order_num, amount):
    con = sqlite3.connect(filename)
    cur = con.cursor()
    command = "UPDATE {} SET amount={} WHERE order_num={}".format(table_name, amount, order_num)
    cur.execute(command)
    con.commit()
    con.close()

def get_total_today():
    total_today=0
    con = sqlite3.connect(filename)
    cur = con.cursor()
    command = "SELECT * FROM {}".format(table_name)
    orders = cur.execute(command).fetchall()
    counter = len(orders)
    for i in orders:
        total_today+=i[2]
    con.commit()
    con.close()
    return total_today

def total_all_time():
    total_all_time=0
    con = sqlite3.connect(filename)
    cur = con.cursor()
    tables = cur.execute("SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%';")
    for table in tables:
        command = "SELECT * FROM {}".format(table_name)
        orders = cur.execute(command).fetchall()
        for i in orders:
            total_all_time+=i[2]
    con.commit()
    con.close()
    print(total_all_time)
    return total_all_time



db_path = Path(filename)
if not db_path.is_file() or modificationTime != date_today:
    create_db()

con = sqlite3.connect(filename)
cur = con.cursor()
command = "SELECT * FROM {}".format(table_name)
orders = cur.execute(command).fetchall()
counter = len(orders)
con.commit()
con.close()

total_all_time()