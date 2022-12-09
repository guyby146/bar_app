import menu
import user_db_commands

users = []
total_day = 0
counter = 0

class user():
    def __init__(self, name) -> None:
        self._name = name
        self._order_num = counter
        self._items = []
        self._total_price = 0
        self._open = True
        users.append(self)

    def add_item(self, item):
        item_price = getattr(menu, item).get_price()
        self._items.append((item, item_price))
        self._total_price += item_price

    def remove_item(self, item):
        item_price = getattr(menu, item).get_price()
        self._items.remove((item, item_price))
        self._total_price -= item_price

    def get_bill(self):
        bill = self._name + "\n"
        for item in self._items:
            bill += item[0] + " " + str(item[1]) +"\n"
        bill += "Total: " + str(self._total_price)
        print(self._name, self._order_num, self._total_price, self._open)
        user_db_commands.add_to_db(self._name, self._order_num, self._total_price, self._open)
        print(bill)
        return bill

    def get_name(self):
        return self._name

    def get_total(self):
        return self._total_price

    def pay(self):
        self._open = False
        global total_day
        total_day += self._total_price
        user_db_commands.add_to_db(self._name, self._order_num, self._total_price, self._open)
        print("Bill closed")


"""
Guy = user("Guy")
Guy.add_item("ThirdGoldstar")
Guy.add_item("Adamame")
Guy.add_item("ThirdGoldstar")
Guy.add_item("HalfShikma")
Guy.get_bill()
Guy.remove_item("HalfShikma")
Guy.get_bill()
Guy.pay()
"""
for customer in users:
    print(customer.get_name())
    
print(total_day, "from", str(len(users)), "transactions")
#goldstar = getattr(menu, "Goldstar")
#print (goldstar.get_name())