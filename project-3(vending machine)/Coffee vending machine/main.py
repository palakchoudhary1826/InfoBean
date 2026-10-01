import os
import customtkinter as ctk
from tkinter import messagebox, simpledialog
from PIL import Image
from bill import generate_bill
coffees = [
    { "name": "Espresso",
        "price": 80,
        "image": "espresso.png" },
    { "name": "Cappuccino",
        "price": 120,
        "image": "cappuccino.png" },
    {"name": "Latte",
        "price": 110,
        "image": "latte.png"},
    { "name": "Mocha",
        "price": 130,
        "image": "mocha.png" }

]

BG_COLOR = "#FFF8F0"
DARK_BROWN = "#4B2E20"
BROWN = "#795548"
LIGHT_BROWN = "#F5E6D3"
CREAM = "#FFFDF9"
GOLD = "#C89B3C"
WHITE = "#FFFFFF"


ctk.set_appearance_mode("Dark")
app = ctk.CTk()
app.title("Coffee Vending Machine")
app.geometry("900x700")
app.resizable(True, True)
app.configure(fg_color=BG_COLOR)

cart = []
BASE_DIR = os.path.dirname( os.path.abspath(__file__))
IMAGES_DIR = os.path.join( BASE_DIR,"images")



def calculate_total():
    total = 0
    for item in cart:
        amount = ( item["price"]* item["quantity"])
        total = total + amount
    return total

def add_to_cart(coffee):
    for item in cart:
        if item["name"] == coffee["name"]:
            item["quantity"] += 1
            update_cart()
            return

    cart.append({ "name": coffee["name"], "price": coffee["price"], "quantity": 1})
    update_cart()


def remove_from_cart(name):
    for item in cart:
        if item["name"] == name:
            if item["quantity"] > 1:
                item["quantity"] -= 1
            else:
                cart.remove(item)
            break
    update_cart()

def update_cart():
    for widget in cart_frame.winfo_children():
        widget.destroy()

    if len(cart) == 0:
        empty_label = ctk.CTkLabel(cart_frame,text="Your cart is empty ☕",font=("Arial", 15),text_color=BROWN)
        empty_label.pack(pady=25)


    else:
        for item in cart:
            amount = (item["price"] * item["quantity"])
            item_frame = ctk.CTkFrame( cart_frame, fg_color=LIGHT_BROWN, corner_radius=10 )

            item_frame.pack(fill="x",padx=5,pady=5 )


            # Coffee name
            name_label = ctk.CTkLabel(item_frame,text=item["name"],
            font=("Arial", 14, "bold"), text_color=DARK_BROWN )
            name_label.pack( side="left",padx=10)

            quantity_label = ctk.CTkLabel(item_frame,text="x" + str(item["quantity"]),
            font=("Arial", 13),text_color=BROWN)

            quantity_label.pack(side="left",padx=10 )


            # Amount
            price_label = ctk.CTkLabel(item_frame,text="Rs. " + str(amount),font=("Arial", 13, "bold"),
            text_color=DARK_BROWN)
            price_label.pack( side="left", padx=10)

            remove_button = ctk.CTkButton(item_frame,text="-",width=35,height=30,fg_color=BROWN,hover_color=DARK_BROWN,
            text_color=WHITE,corner_radius=8,command=lambda name=item["name"]:
                remove_from_cart(name))

            remove_button.pack( side="right", padx=10 )

    total = calculate_total()
    total_label.configure(
        text="Total: Rs. " + str(total) )

def make_payment():
    if len(cart) == 0:
        messagebox.showwarning("Empty Cart","Please add a coffee first." )
        return
    total = calculate_total()
    amount = simpledialog.askinteger("Payment","Total Amount: Rs. "+ str(total)+ "\n\nEnter payment amount:" )

    if amount is None:
        return
    if amount < total:
        remaining = total - amount

        messagebox.showerror("Insufficient Payment", "Please pay Rs. " + str(remaining) + " more.")
        return
    change = amount - total
    # Generate PDF
    file_name = generate_bill(cart,total,amount,change )

    messagebox.showinfo("Payment Successful","Payment successful!\n\n""Total: Rs. "+ str(total)+ "\nPaid: Rs. "+ str(amount)+ "\nChange: Rs. "+ str(change)  + "\n\nPDF Bill Generated!")
    cart.clear()
    update_cart()

    # Open PDF
    os.startfile(
        os.path.abspath(file_name))

title_frame = ctk.CTkFrame(app,fg_color=DARK_BROWN,corner_radius=0)
title_frame.pack(  fill="x")


title_label = ctk.CTkLabel( title_frame, text="☕  COFFEE VENDING MACHINE  ☕",
font=("Arial", 28, "bold"), text_color=WHITE)
title_label.pack(pady=18)

main_frame = ctk.CTkFrame(app,fg_color=BG_COLOR)
main_frame.pack(fill="both",expand=True,padx=20,pady=15)

 #LEFT cofee frme
coffee_frame = ctk.CTkFrame(main_frame,fg_color=CREAM,corner_radius=15,
border_width=2,border_color=LIGHT_BROWN)
coffee_frame.pack( side="left", fill="both", expand=True, padx=8, pady=5)

coffee_title = ctk.CTkLabel(coffee_frame,text="Choose Your Coffee",
font=("Arial", 20, "bold"),text_color=DARK_BROWN)
coffee_title.pack(pady=15)

for coffee in coffees:
    card = ctk.CTkFrame(coffee_frame,fg_color=LIGHT_BROWN,corner_radius=12)
    card.pack( fill="x", padx=15, pady=7)
    
    image_path = os.path.join( IMAGES_DIR, coffee["image"])
    if os.path.exists(image_path):
        image = Image.open(image_path)

        coffee_image = ctk.CTkImage(light_image=image,dark_image=image,size=(70, 70))
        image_label = ctk.CTkLabel( card, text="", image=coffee_image)
        image_label.pack(side="left", padx=10, pady=8)

    else:
        image_label = ctk.CTkLabel( card, text="Image not found", text_color=BROWN )
        image_label.pack( side="left", padx=10, pady=8 )

    details = ctk.CTkFrame( card,fg_color="transparent")
    details.pack(side="left",padx=10 )

    name_label = ctk.CTkLabel(details,text=coffee["name"],
    font=("Arial", 16, "bold"),text_color=DARK_BROWN )

    name_label.pack(anchor="w")
    price_label = ctk.CTkLabel(details,text="Rs. " + str(coffee["price"]),
    font=("Arial", 14),text_color=BROWN)
    price_label.pack( anchor="w" )


    add_button = ctk.CTkButton( card, text="Add to Cart", width=110, height=35, 
    fg_color=DARK_BROWN, hover_color=BROWN, text_color=WHITE, corner_radius=8,
        command=lambda c=coffee:
        add_to_cart(c))
    add_button.pack( side="right",padx=12)

right_frame = ctk.CTkFrame(main_frame,fg_color=CREAM,corner_radius=15,border_width=2,border_color=LIGHT_BROWN)
right_frame.pack(side="right", fill="both", expand=True, padx=8, pady=5)

cart_title = ctk.CTkLabel(right_frame,text="🛒 Your Cart",
font=("Arial", 20, "bold"),text_color=DARK_BROWN)
cart_title.pack( pady=15)

cart_frame = ctk.CTkFrame( right_frame, fg_color="transparent")
cart_frame.pack(fill="both",expand=True,padx=10)

total_label = ctk.CTkLabel(right_frame,text="Total: Rs. 0",font=("Arial", 20, "bold"),text_color=DARK_BROWN)
total_label.pack(pady=10)

payment_button = ctk.CTkButton( right_frame, text="💳  Pay Now", width=200, height=45,
font=("Arial", 16, "bold"), fg_color=GOLD, hover_color=BROWN, text_color=WHITE,corner_radius=10,command=make_payment)
payment_button.pack(pady=15)

update_cart()
app.mainloop()