from tkinter import *
import menu
import users
import DB_Commands
import user_db_commands



default_bg='SystemButtonFace'
alcohol_buttons = []
food_buttons = []
soft_drinks_buttons = []
password = 'admin'


def main_menu():
    welcome_text.pack_forget()
    passEntry.place_forget()
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

def check_password(event):
    input_password = passEntry.get()
    if input_password == password:
        buttons_frame.grid(column=0, row=0, columnspan=4)
        back_button.grid(column=0, row=0)
        total_button.grid(column=1, row=0)
        total_label.grid(column=3, row=0)
        main_frame.pack()
        buy_frame.grid(column=0, row=1, sticky="n")
        orders_frame.grid(column=1, row=1, sticky="n")
        main_menu()
    


def remove_item(item_name):
    pass


def add_item(item_name, item_price):
    pass


def open_menu(products):
    pass

def total_today():
    print(user_db_commands.get_total_today())


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
welcome_text.insert(INSERT, 'please enter password:')
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
total_button = Button(buttons_frame, text='Total today', command=total_today)
total_label = Label(buttons_frame, text="Total: ")


create_buttons()

"""
welcome_label = Text(INSERT, "please enter your name to connect to your user:")
welcome_label.tag_configure("center", justify='center')
welcome_label.tag_add("center", "1.0", "end")
welcome_label.pack()
"""
passInput = StringVar()
passEntry = Entry(textvariable = passInput, width = 100)
passEntry.place(x = 200, y = 100)

screen.bind('<Return>', check_password)


screen.mainloop()