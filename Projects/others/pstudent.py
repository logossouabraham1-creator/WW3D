def menu():
    print("=" * 40)
    print("\tSTUDENT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Student")
    print("2. View Students")
    print("3. Enter Scores")
    print("4. Calculate Grade")
    print("5. Show Class Statistics")
    print("6. Search Student")
    print("7. Exit")

def student_view(name,id):
    print("========== STUDENTS ==========")
    for i in range(0,len(name)):
        print(f"ID : {id[i]}")
        print(f"name: {name[i]}\n")
id_list = []
student_list = [] 
menu()
while True :
    while True:
        try:
            user_entry = int(input("Enter choice(1-7): ") )
        except ValueError:
            print("Please enter a valid number.")
        if user_entry <= 0 : 
            print("Enter a valid number.")   
            continue
        else:
            break
    if user_entry == 1 :
        while True:
            student_name = input("Enter student name:").strip().capitalize()
            if not student_name:
                print("Student name cannot be empty")
            elif student_name in "0123456789" :
                print("Student name cannot contain number")
            else :
                break
        student_list.append(student_name)
        while True :
            try :
                student_id = int(input("Enter Student Id: ")) 
            except ValueError:
                print("Enter a valid number")
            id_list.append(student_id)
    elif user_entry == 2 :
        student_view(student_list,id_list)