menu = ["espresso","latte","cappuccino","americano"]
def welcome():
    print("=" * 40)
    print("\tCOFFEE CART SYSTEM")
    print("=" * 40)

def display_menu():
    print("Coffee Menu\n")
    print("1. Espresso\t₦2500")
    print("2. Latte\t₦3500")
    print("3. Cappuccino\t₦4000")
    print("4. Americano\t₦3000")

def get_customer_name():
    while True:
        user_entry = input("Enter your name : ").strip().title()
        if len(user_entry) == 0:
            print("Please Enter a valid name.")
        else :
            return user_entry

def get_drink():
    while True :
        user_drink = input("Enter your beverage order : ").strip().lower()
        if user_drink in menu :
            return user_drink
        
def get_price(drink):
    if drink =="espresso":
        return 2500
    elif drink == "latte":
        return 3500
    elif drink == "cappuccino":
        return 4000
    elif drink == "americano":
        return 3000
    else :
        return "Drink not found"

def create_order_id(name,drink):
    joined = "-".join([name[:3],drink[:3]])
    return joined
def print_receipt(name, drink, price, order_id):
    # joined = "-"join.([nam[:3],drink[:3]])
    print("=" * 30)
    print("\tRECEIPT")
    print("=" * 30)
    print(f"\n{'Customer':<10} : {name}\n")
    print(f"{'Drink':<10} : {drink}\n")
    print(f"{'Price':<10} : {price:.2f}\n")
    print(f"{'Order ID':<10} : {order_id}\n")
    print("Thank you for your order!")

welcome()
display_menu()

name = get_customer_name()
drink = get_drink()
price = get_price(drink)
order_id = create_order_id(name, drink)

print_receipt(name,drink,price, order_id)