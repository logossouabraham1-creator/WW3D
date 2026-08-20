def receipt():
    print("=" * 30)
    print("\tCOFFEE CART")
    print("=" * 30)
    print(
        f"\n\n{'Customer':<10} : {Name}\n"
        f"{'Drink':<10} : {Drink}\n"
        f"{'Drink_ID':<10} : {Drink_tag}\n"
        f"{'Order_ID':<10} : {order_ID}\n"
        f"{'Price':<10} : ₦{Price:,.2f}\n\n"
        f"Thank you, {Name}!\n"
        f"Your {Drink} is being prepared."
    )

user_order = input("Enter your order : ").split("|")
Name = user_order[0].strip().title()
Drink = user_order[1].strip().capitalize()
Price = user_order[2].strip()
Price = float(Price)
Drink_tag = Drink[:3]
Name_tag = Name[:3]
order_ID = "-".join([Name_tag,Drink_tag])
receipt()

