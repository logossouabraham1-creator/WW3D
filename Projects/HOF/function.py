# CUSTOMER ORDERS
menu = {
    "espresso": 2500,
    "latte": 3500,
    "cappuccino": 4000,
    "americano": 3000,
    "mocha": 4500
}
orders = []
def intro():
    print("=" * 30)
    print("\tCOFFEE CART")
    print("=" * 30)
    print("\nMENU\n")
    print(f"1.{'Espresso':<10} ₦2500")
    print(f"2.{'Latte':<10} ₦3500")
    print(f"3.{'Cappuccino':<10} ₦4000")
    print(f"4.{'Americano':<10} ₦3000")
    print(f"5.{'Mocha':<10} ₦4500\n")
    print("=" * 30)
def after_intro():
    print("="*30)
    print("ORDERS COLLECTED")
    print("="*30)
intro()
# Variable scope 
restart = True
# Program start 
while restart :
    while True :
        user_name_entry = input("Enter customer name: ").strip().capitalize()
        if user_name_entry != "" :
            break 
        else :
            print("Customer name cannot be empty.")
    while True:
        user_drink_entry = input("Enter drink:  ").strip().lower()
        if user_drink_entry not in menu :
            print(f"Sorry,{user_drink_entry} is not available.")
            print("Please choose a drink from the menu.")
        else :
            break 
    user_drink_entry_price = menu[user_drink_entry]
    customer_data = (user_name_entry,user_drink_entry,user_drink_entry_price)
    orders.append(customer_data)
    print("Order added successfully.")
    while True :
        user_continues = input("Add another order? (yes/no): ").strip().lower()
        if user_continues == "yes" :
            break
        elif user_continues == "no" :
            restart = False 
            break
        else :
            print("Please enter yes or no.")

after_intro()
print(orders)
def format(usage):
    name , drink , price = usage
    return f"{name} ordered {drink} - ₦{price:,}"
result = list(map(format,orders))
result1 = list(map(lambda usage : f"{usage[0]} ordered {usage[1]} - {usage[2]:,} ",orders))
