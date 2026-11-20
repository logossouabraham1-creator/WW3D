def welcome():
    print("=== ATM Login ===")
made = True
while made :
    try :
        welcome()
        user_pin = int(input("Enter your Pin(4-digit) : "))
        if user_pin == 1234 :
            print("Login Successful")
            made = False 
        else :
            print("Incorrect PIN")
    except ValueError :
        print("Enter a valid whole number.")
print("Thank you ")
