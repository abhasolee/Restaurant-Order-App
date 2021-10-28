from tkinter import *
from PIL import Image, ImageTk

# Configuring window
w = 500
h = 800
root = Tk()
root.title("Order System App")
root.geometry('{}x{}+500+0'.format(w, h))

# Create dictionaries for prices
drinks_dict = {
    'pepsi': 60,
    'coke': 60,
    'coffee': 30,
    'tea': 20,
    'milkshake': 120,
    'virgin mojito': 250,
    'margarita': 300,
    'fresh juice': 100
}

food_dict = {
    'burger': 130,
    'pizza': 200,
    'momo': 100,
    'pasta': 180,
    'french fries': 75,
    'chowmein': 100,
    'sekuwa': 50,
    'sausage': 40

}


# Function to calculate price
def calculate():
    # Calculate cost for the drinks
    cost_drink = 0
    for drink in drinks_checkbox_list:
        for no in drinks_entry_list:
            if drink.get() != "" and drink.get() != '0':
                print(drink.get())
                cost_drink = cost_drink + \
                    drinks_dict[drink.get()] * int(no.get())
                drinks_entry_list.remove(no)
                break
            else:
                no.insert(0, '0')
                drinks_entry_list.remove(no)
                break

    # Calculate cost for the food
    cost_food = 0
    for food in food_checkbox_list:
        for no in food_entry_list:
            if food.get() != "" and food.get() != '0':
                cost_food = cost_food + \
                    food_dict[food.get()] * int(no.get())
                food_entry_list.remove(no)
                break
            else:
                no.insert(0, '0')
                food_entry_list.remove(no)
                break

    # Calcualte the total cost and inserting in entry box
    cost_total = cost_drink + cost_food
    cost_box.insert(0, cost_total)

    # Calculate service charge
    service_charge = 0.10 * cost_total
    service_charge_box.insert(0, service_charge)

    # Calculate VAT
    vat = 0.13 * (cost_total + service_charge)
    vat_box.insert(0, "%.2f" % vat)

    # Calculate total
    total = cost_total + service_charge + vat
    total_box.insert(0, "%.2f" % total)


# Calculate function to reset the items
def reset():
    # Deleting the contents of entry box
    cost_box.delete(0, END)
    service_charge_box.delete(0, END)
    vat_box.delete(0, END)
    total_box.delete(0, END)

    # Deselecting the items of checkbox
    for drink in drinks_checkbox_list:
        drink.set(0)
    for food in food_checkbox_list:
        food.set(0)

    # Defining the lists again
    drinks_entry_list.extend([pepsi_no, coke_no, coffee_no, tea_no,
                              milkshake_no, virgin_mojito_no, margarita_no, fresh_juice_no])
    for no in drinks_entry_list:
        no.delete(0, END)

    food_entry_list.extend([burger_no, pizza_no, momo_no, pasta_no,
                            french_fries_no, chowmein_no, sekuwa_no, sausage_no])
    for no in food_entry_list:
        no.delete(0, END)



# Create title frame
title_frame = Frame(root, width=w, height=50)
title_frame.grid(row=0, column=0, columnspan=2)

# Create title label
title_label = Label(root, text="ORDER YOUR FOOD!",
                    font=('The Hills PERSONAL USE ONLY', 40), fg="#D65076")
title_label.place(x=w / 2, y=25, anchor=CENTER)

# Add image
# Resizing the image
img = Image.open('images/food.jpg')
resize = img.resize((250, 180), Image.ANTIALIAS)
new_img = ImageTk.PhotoImage(resize)

# Adding the image to screen
img_label = Label(root, image=new_img)
img_label.grid(row=1, column=0, columnspan=2, pady=10)

# Create frames
drink_frame = Frame(root, width=w / 2, height=300, highlightbackground="#C3447A",
                    highlightthickness=2)
drink_frame.grid(row=2, column=0, sticky=E)
drink_frame.grid_propagate(FALSE)

food_frame = Frame(root, width=w / 2, height=300,
                   highlightbackground='#C3447A', highlightthickness=2)
food_frame.grid(row=2, column=1, sticky=W)
food_frame.grid_propagate(FALSE)

reciept_frame = Frame(root, width=w, height=160,
                      highlightbackground='#C3447A', highlightthickness=2)
reciept_frame.grid(row=3, column=0, columnspan=2)
reciept_frame.grid_propagate(FALSE)

# For the drinks frame
# Create title
drink_title_label = Label(drink_frame, text="DRINKS",
                          font=('Beach Society', 30), fg="#FF6F61")
drink_title_label.grid(row=0, column=0, columnspan=2)

# Create checkboxes
pepsi_var = StringVar()
coke_var = StringVar()
coffee_var = StringVar()
tea_var = StringVar()
milkshake_var = StringVar()
virgin_mojito_var = StringVar()
margarita_var = StringVar()
fresh_juice_var = StringVar()


pepsi = Checkbutton(drink_frame, text="Pepsi",
                    variable=pepsi_var, onvalue="pepsi")
pepsi.grid(row=1, column=0, sticky=W)

coke = Checkbutton(drink_frame, text="Coke",
                   variable=coke_var, onvalue="coke")
coke.grid(row=2, column=0, sticky=W)

coffee = Checkbutton(drink_frame, text="Coffee",
                     variable=coffee_var, onvalue="coffee")
coffee.grid(row=3, column=0, sticky=W)

tea = Checkbutton(drink_frame, text="Tea", variable=tea_var, onvalue="tea")
tea.grid(row=4, column=0, sticky=W)

milkshake = Checkbutton(drink_frame, text="Milkshake",
                        variable=milkshake_var, onvalue="milkshake")
milkshake.grid(row=5, column=0, sticky=W)

virgin_mojito = Checkbutton(drink_frame, text="Virgin Mojito",
                            variable=virgin_mojito_var, onvalue="virgin mojito")
virgin_mojito.grid(row=6, column=0, sticky=W)

margarita = Checkbutton(drink_frame, text="Margarita",
                        variable=margarita_var, onvalue="margarita")
margarita.grid(row=7, column=0, sticky=W)

fresh_juice = Checkbutton(drink_frame, text="Fresh Juice",
                          variable=fresh_juice_var, onvalue="fresh juice")
fresh_juice.grid(row=8, column=0, sticky=W)

# Create drinks list of checkboxes variables
drinks_checkbox_list = [pepsi_var, coke_var, coffee_var, tea_var,
                        milkshake_var, virgin_mojito_var, margarita_var, fresh_juice_var]

# Create entry boxes
pepsi_no = Entry(drink_frame, width=8)
pepsi_no.grid(row=1, column=1)

coke_no = Entry(drink_frame, width=8)
coke_no.grid(row=2, column=1)

coffee_no = Entry(drink_frame, width=8)
coffee_no.grid(row=3, column=1)

tea_no = Entry(drink_frame, width=8)
tea_no.grid(row=4, column=1)

milkshake_no = Entry(drink_frame, width=8)
milkshake_no.grid(row=5, column=1)

virgin_mojito_no = Entry(drink_frame, width=8)
virgin_mojito_no.grid(row=6, column=1)

margarita_no = Entry(drink_frame, width=8)
margarita_no.grid(row=7, column=1)

fresh_juice_no = Entry(drink_frame, width=8)
fresh_juice_no.grid(row=8, column=1)

# Create drinks entry boxes list
drinks_entry_list = [pepsi_no, coke_no, coffee_no, tea_no,
                     milkshake_no, virgin_mojito_no, margarita_no, fresh_juice_no]

# For the food frame
# Create title
food_title_label = Label(food_frame, text="SNACKS",
                         font=('Beach Society', 30), fg="#FF6F61")
food_title_label.grid(row=0, column=0, columnspan=2)

# Create checkboxes
burger_var = StringVar()
pizza_var = StringVar()
momo_var = StringVar()
pasta_var = StringVar()
french_fries_var = StringVar()
chowmein_var = StringVar()
sekuwa_var = StringVar()
sausage_var = StringVar()

burger = Checkbutton(food_frame, text="Burger",
                     variable=burger_var, onvalue="burger")
burger.grid(row=1, column=0, sticky=W)

pizza = Checkbutton(food_frame, text="Pizaa",
                    variable=pizza_var, onvalue="pizza")
pizza.grid(row=2, column=0, sticky=W)

momo = Checkbutton(food_frame, text="Momo",
                   variable=momo_var, onvalue="momo")
momo.grid(row=3, column=0, sticky=W)

pasta = Checkbutton(food_frame, text="Pasta",
                    variable=pasta_var, onvalue="pasta")
pasta.grid(row=4, column=0, sticky=W)

french_fries = Checkbutton(food_frame, text="French Fries",
                           variable=french_fries_var, onvalue="french fries")
french_fries.grid(row=5, column=0, sticky=W)

chowmein = Checkbutton(food_frame, text="Chowmein",
                       variable=chowmein_var, onvalue="chowmein")
chowmein.grid(row=6, column=0, sticky=W)

sekuwa = Checkbutton(food_frame, text="Sekuwa",
                     variable=sekuwa_var, onvalue="sekuwa")
sekuwa.grid(row=7, column=0, sticky=W)

sausage = Checkbutton(food_frame, text="Sausage",
                      variable=sausage_var, onvalue="sausage")
sausage.grid(row=8, column=0, sticky=W)

# Create food checkboxes list
food_checkbox_list = [burger_var, pizza_var, momo_var, pasta_var,
                      french_fries_var, chowmein_var, sekuwa_var, sausage_var]

# Create entry boxes
burger_no = Entry(food_frame, width=8)
burger_no.grid(row=1, column=1)

pizza_no = Entry(food_frame, width=8)
pizza_no.grid(row=2, column=1)

momo_no = Entry(food_frame, width=8)
momo_no.grid(row=3, column=1)

pasta_no = Entry(food_frame, width=8)
pasta_no.grid(row=4, column=1)

french_fries_no = Entry(food_frame, width=8)
french_fries_no.grid(row=5, column=1)

chowmein_no = Entry(food_frame, width=8)
chowmein_no.grid(row=6, column=1)

sekuwa_no = Entry(food_frame, width=8)
sekuwa_no.grid(row=7, column=1)

sausage_no = Entry(food_frame, width=8)
sausage_no.grid(row=8, column=1)

# Create list for the food entry boxes
food_entry_list = [burger_no, pizza_no, momo_no, pasta_no,
                   french_fries_no, chowmein_no, sekuwa_no, sausage_no]


# For the reciept frame
# Create title
reciept_title_label = Label(reciept_frame, text="RECIEPT",
                            font=('Beach Society', 30), fg="#FF6F61")
reciept_title_label.grid(row=0, column=0, columnspan=2)

# Create labels
cost_label = Label(reciept_frame, text="Cost")
cost_label.grid(row=1, column=0)

service_charge_label = Label(reciept_frame, text=" 10% Service Charge")
service_charge_label.grid(row=2, column=0)

vat_label = Label(reciept_frame, text="13% VAT")
vat_label.grid(row=3, column=0)

total_label = Label(reciept_frame, text="Total")
total_label.grid(row=4, column=0)

# Create entry boxes
cost_box = Entry(reciept_frame, width=20)
cost_box.grid(row=1, column=1)

service_charge_box = Entry(reciept_frame, width=20)
service_charge_box.grid(row=2, column=1)

vat_box = Entry(reciept_frame, width=20)
vat_box.grid(row=3, column=1)

total_box = Entry(reciept_frame, width=20)
total_box.grid(row=4, column=1)

# Create buttons
button_frame = Frame(root, width=w, height=30)
button_frame.grid(row=4, column=0, pady=10, columnspan=2)

calculate_button = Button(
    button_frame, text="Calculate Price", font=('Coves', 18), fg="#DD4124", command=calculate)
calculate_button.grid(row=4, column=0)

reset_button = Button(button_frame, text="Reset",
                      font=('Coves', 18), fg="#DD4124", command=reset)
reset_button.grid(row=4, column=1, padx=30)

exit_button = Button(button_frame, text="Exit", font=(
    'Coves', 18), fg="#DD4124", command=root.quit)
exit_button.grid(row=4, column=2, padx=20)


root.mainloop()
