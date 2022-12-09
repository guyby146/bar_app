from tkinter import *
import menu
import users

counter = 0
alcohol_buttons = []
food_buttons = []
soft_drinks_buttons = []
default_bg='SystemButtonFace'
ordered_items = []
ordered_buttons = []


def main_menu():
    welcome_text.pack_forget()
    wordEntry.place_forget()
    for button in alcohol_buttons:
        button.grid_forget()
    for button in food_buttons:
        button.grid_forget()
    for button in soft_drinks_buttons:
        button.grid_forget()
    #back_button.pack_forget()
    back_button.config(borderwidth=0, fg=default_bg)
    food_button.grid(column=1,row=0)
    alcohol_button.grid(column=1,row=1)
    soft_drinks_button.grid(column=1,row=2)

    """
    for button in alcohol_buttons:
        button.pack_forget()
    for button in food_buttons:
        button.pack_forget()
    for button in soft_drinks_buttons:
        button.pack_forget()
    back_button.pack_forget()
    food_button.grid(column=1,row=0)
    alcohol_button.grid(column=1,row=1)
    soft_drinks_button.grid(column=1,row=2)
    
    food_button.place(x=100, y=100)
    alcohol_button.place(x=400, y=100)
    soft_drinks_button.place(x=700, y=100)
"""
current_user = ""

def create_user(event):
    name = wordEntry.get()
    global counter
    if name.isalpha():
        command = 'global {}; {} = users.user("{}")'.format(name+str(counter), name+str(counter), name)
        exec(command)
        global current_user
        current_user = globals()[wordEntry.get()+str(counter)]
        print(globals()[wordEntry.get()+str(counter)].get_name())
        counter += 1
    else:
        welcome_text.delete(1.0, END)
        welcome_text.insert(1.0, 'please enter letters only:') 
        welcome_text.tag_add("center", "1.0", "end")
    name_label.config(text="Hi {}, on the left side you can add items to your order and on the right side remove from the order:".format(name))
    name_label.pack()
    #back_button.pack()
    buttons_frame.grid(column=0, row=0, columnspan=4)
    back_button.grid(column=0, row=0)
    get_bill_button.grid(column=1, row=0)
    total_label.grid(column=3, row=0)
    main_frame.pack()
    buy_frame.grid(column=0, row=1, sticky="n")
    orders_frame.grid(column=1, row=1, sticky="n")
    #buy_frame.pack(side='top', anchor='nw')
    #orders_frame.pack(anchor='ne')
    main_menu()

def remove_item(item_name):
    current_user.remove_item(item_name)
    print(current_user.get_total())
    print(current_user.get_name())
    for item in current_user._items:
        print(item)
    current = ordered_buttons[ordered_items.index(item_name)]
    current.grid_forget()
    ordered_buttons.remove(current)
    ordered_items.remove(item_name)
    for button, i in zip(ordered_buttons, range(len(ordered_buttons))):
        button.grid(row=i)
    total_label.config(text="Total: {}".format(current_user._total_price))
    print(ordered_items)
    print(ordered_buttons)
    print(len(ordered_buttons))
    print(len(ordered_items))


def add_item(item_name, item_price):
    current_user.add_item(item_name)
    print(current_user.get_total())
    print(current_user.get_name())
    for item in current_user._items:
        print(item)
    create_button = "global {}; {} = Button(orders_frame, text='{}'+' - '+'{}', padx=5, pady=5, width=15, command=lambda:remove_item('{}')); ordered_buttons.append({})".format(item_name, item_name, item_name, item_price, item_name, item_name)
    exec(create_button)
    ordered_items.append(item_name)
    ordered_buttons[-1].grid(column=0,row=len(ordered_buttons))
    total_label.config(text="Total: {}".format(current_user._total_price))
    print(ordered_buttons)
    print(ordered_items)
    print(len(ordered_buttons))
    print(len(ordered_items))


def open_menu(products):
    print(current_user)
    #items_list = []
    #items_list = getattr(menu, category)
    """
    food_button.place_forget()
    alcohol_button.place_forget()
    soft_drinks_button.place_forget()
    """
    food_button.grid_forget()
    alcohol_button.grid_forget()
    soft_drinks_button.grid_forget()
    #back_button.pack()
    back_button.config(fg='black', borderwidth=2)

    #for item in products:
    #    item.pack(side='left')
    for item, i in zip(products, range(5)):
        for l in range(10):
            item.grid(column=l,row=i)
    
    """
    if category == 'alcohol_list':
        for item in items_list:
            print(item.get_name())
            create_button = "global {}; {} = Button(screen, text='{}', padx=35, pady=5, width=5, command=lambda:add_item('{}'))".format(item.get_size()+item.get_name(), item.get_size()+item.get_name(), item.get_size()+" "+item.get_name(), item.get_size()+item.get_name())
            exec(create_button)
            #add_button = "{}.grid(row=1,column={})".format(item.get_size()+item.get_name(), i)
            #add_button = "{}.place(relx=0.01, rely=0.01)".format(item.get_size()+item.get_name())
            add_button = "{}.pack(side='left')".format(item.get_size()+item.get_name())
            exec(add_button)
    else:
        for item in items_list:
            print(item.get_name())
            create_button = "global {}; {} = Button(screen, text='{}', padx=35, pady=5, width=5, command=lambda:add_item('{}'))".format(item.get_name(), item.get_name(), item.get_name(), item.get_name())
            exec(create_button)
            #add_button = "{}.grid(row=1,column={})".format(item.get_size()+item.get_name(), i)
            #add_button = "{}.place(relx=0.01, rely=0.01)".format(item.get_size()+item.get_name())
            add_button = "{}.pack(side='left')".format(item.get_name())
            exec(add_button)"""

def order():
    current_user.get_bill()
    buy_frame.grid_forget()
    orders_frame.grid_forget()
    back_button.grid_forget()
    get_bill_button.grid_forget()
    pay_button.grid(column=0, row=0)

def pay():
    current_user.pay()
    main_frame.pack_forget()
    name_label.config(text="Thank you for ordering, your order will arrive shortly to your table.")

def create_buttons():
    for item in getattr(menu, 'alcohol_list'):
        create_button = "global {}; {} = Button(buy_frame, text='{}'+' - '+'{}', padx=5, pady=5, width=15, command=lambda:add_item('{}', '{}')); alcohol_buttons.append({})".format(item.get_size()+item.get_name(), item.get_size()+item.get_name(), item.get_size()+" "+item.get_name(), item.get_price(), item.get_size()+item.get_name(), item.get_price(), item.get_size()+item.get_name())
        exec(create_button)
    for item in getattr(menu, 'food_list'):
        create_button = "global {}; {} = Button(buy_frame, text='{}'+' - '+'{}', padx=5, pady=5, width=15, command=lambda:add_item('{}', '{}')); food_buttons.append({})".format(item.get_name(), item.get_name(), item.get_name(), item.get_price(), item.get_name(), item.get_price(), item.get_name())
        exec(create_button)
    for item in getattr(menu, 'soft_drinks_list'):
        create_button = "global {}; {} = Button(buy_frame, text='{}'+' - '+'{}', padx=5, pady=5, width=15, command=lambda:add_item('{}', '{}')); soft_drinks_buttons.append({})".format(item.get_name(), item.get_name(), item.get_name(), item.get_price(), item.get_name(), item.get_price(), item.get_name())
        exec(create_button)


screen = Tk()
screen.geometry("1000x500")
screen.title("Guy's cocktails")
screen.iconbitmap("cocktail.ico")
heading = Label(text = "Welcome to Guy's cocktails - the BEST bar in town", bg = "blue", fg = "white", width = 1000, height = 3)
heading.pack()

welcome_text = Text(screen, width=1000, height=2)
welcome_text.insert(INSERT, 'please enter your name:')
welcome_text.tag_configure("center", justify='center')
welcome_text.tag_add("center", "1.0", "end")
welcome_text.pack()

name_label = Label()

main_frame = Frame(screen, width=1000)
buy_frame = LabelFrame(main_frame, text="Click any item you would like to order", padx=5, pady=5, width=50)
orders_frame = LabelFrame(main_frame, text="Click any item you would like to remove", padx=5, pady=5, width=50)
buttons_frame = Frame(main_frame)
"""
alcohol_button = Button(screen, text='Alcohol menu', command=lambda:open_menu(alcohol_buttons))
food_button = Button(screen, text='Food menu', command=lambda:open_menu(food_buttons))
soft_drinks_button = Button(screen, text='Soft drinks menu', command=lambda:open_menu(soft_drinks_buttons))
"""

alcohol_button = Button(buy_frame, text='Alcohol menu', padx=5, pady=5, width=15, command=lambda:open_menu(alcohol_buttons))
food_button = Button(buy_frame, text='Food menu', padx=5, pady=5, width=15, command=lambda:open_menu(food_buttons))
soft_drinks_button = Button(buy_frame, text='Soft drinks menu', padx=5, pady=5, width=15, command=lambda:open_menu(soft_drinks_buttons))

back_button = Button(buttons_frame, text='Back', command=main_menu)
get_bill_button = Button(buttons_frame, text='Order', command=order)
pay_button = Button(buttons_frame, text='Pay', command=pay)
total_label = Label(buttons_frame, text="Total: ")


create_buttons()

"""
welcome_label = Text(INSERT, "please enter your name to connect to your user:")
welcome_label.tag_configure("center", justify='center')
welcome_label.tag_add("center", "1.0", "end")
welcome_label.pack()
"""
wordInput = StringVar()
wordEntry = Entry(textvariable = wordInput, width = 100)
wordEntry.place(x = 200, y = 100)

screen.bind('<Return>', create_user)


screen.mainloop()