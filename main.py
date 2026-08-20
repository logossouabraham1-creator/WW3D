def intro():
    print("=" * 40)
    print("\tSTUDENT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Students")
    print("4. Enter Scores")
    print("5. Calculate Grades")
    print("6. Class Statistics")
    print("7. Save Students")
    print("8. Load Students")
    print("9. Exit")
def entry():
    while True:
        try:
            user_choice = int(input("Enter your option(1-9): "))
            if user_choice >= 1 :
                break
            else :
                print("Option cannot be negative.")

            continue
        except ValueError:
            print("Please enter a valid number")
    return user_choice
intro()
user_choice = None
user_choice = entry()
if user_choice == 1 :
    print("Hello")