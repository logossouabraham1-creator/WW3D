def welcome():
    print("=" * 40)
    print("\t COFFEE CART ORDER SYSTEM ")
    print("=" * 40)
    print("Welcome")
    print("Please enter your order in the format below: \n")
    print("Name | Drink | Price")
    print("Example:")
    print("Daniel John | Espresso | 2500")
    print("-" * 40)
welcome()
user_order = input("Enter your order : ")
user_order = user_order.split("|")
user_name = user_order[0]
user_drink = user_order[1]
user_price = user_order[2]
user_name = user_name.strip()
user_drink = user_drink.strip()
user_price = user_price.strip()
user_price = float(user_price)
user_drink_cap = user_drink.capitalize()
user_drink_tag = user_drink[:3]
user_name_tag = user_name[:3]
order_ID = "-".join([user_name_tag,user_drink_tag])
print(f"{'Customer':<10} : {user_name}"
    f"\n{'Drink':<10} : {user_drink}"
    f"\n{'Drink Id':<10} : {user_drink_tag}"
    f"\n{'Order ID':<10} : {order_ID}"
    f"\n{'Price':<10} : {user_price:.2f}"
    f"\n\nThank you,{user_name}!"
    f"\nYour {user_drink_cap} is being prepared.")
print("\nDrink Analysis")
print("-" * 20)
print(f"First Letter : {user_drink[0]}")
print(f"Last Letter  : {user_drink[-1]}")
print(f"Last 3 Letters : {user_drink[-3:]}")
print(f"Reverse Drink : {user_drink[::-1]}")

  # abraham logossou   |   SOFTWARE ENGINEER   |   OPENAI   |   abraham.LOGO@GMAIL.com
