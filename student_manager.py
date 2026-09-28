# BASIC DATA
students = [
    {
        "name": "Abraham",
        "age": 20,
        "course": "Python",
        "score": 95
    },
    {
        "name": "John",
        "age": 22,
        "course": "Java",
        "score": 72
    },
    {
        "name": "Mary",
        "age": 19,
        "course": "Python",
        "score": 49
    }
]

# HELPER FUNCTIONS FOR SCORE VALIDATION THAT WORKS FOR ANY INPUT FUNCTION THAT GETS SCORE 
def get_valid_score(prompt):
    while True:
        try:
            score = int(input(prompt))
            if score < 0 or score > 100 :
                print("Score must be valid.")
                continue 
            return score 
        except ValueError :
            print("Please enter a valid score.")


# HELPER FUNCTIONS FOR NAME VALIDATION THAT WORKS FOR ANY INPUT FUNCTION THAT GETS NAME 
def get_valid_name(prompt):
    while True :
        name = input(prompt).strip().capitalize()
        if not name.isalpha():
            print("Name must contain letters only.")
            continue
        return name 

def get_valid_age(prompt):
    while True :
        try :
            age = int(input(prompt))
            if age <= 0 or age >= 100 :
                print("Age must be between 1-99.")
                continue 
            return age 
        except ValueError :
            print("Please enter a valid age.")

def get_valid_course(prompt):
    while True :
        student_course = input(prompt).strip().capitalize()
        if not student_course.isalpha():
            print("Student course must contain letters only.")
            continue 
        return student_course 

#  ADD STUDENT FUNCTION 
def add_student():
    student_name = get_valid_name("Enter student's name: ")
    student_age = get_valid_age("Enter Student's age: ")
    student_course = get_valid_course("Enter student's course: ")
    student_score = get_valid_score("Enter student's score: ")
    student_dict = {
        "name":student_name,
        "age":student_age,
        "course":student_course,
        "score":student_score
    }
    students.append(student_dict)

# VIEW STUDENTS FUNCTION 
def view_students():
    if students :
        for i in range(len(students)):
            print(f"{i+1}. {students[i]['name']:<10} | Age: {students[i]['age']:<10} | {students[i]['course']:<10} | Score: {students[i]['score']:<10}")
    else :
        print("No students available.")

# SEARCH STUDENT FUNCTION 
def search_student():
    search_student_by_name = get_valid_name("Enter student's name: ")
    found = False 
    for student in students :
        if student["name"] == search_student_by_name:
            print("Student found!")
            print(student)
            found = True 
    if not found :
        print("Student not found")

# UPDATE STUDENT FUNCTION 
def update_student_score():
    name_to_update = get_valid_name("Enter student's name: ")
    found = False 
    for student in students :
        if student["name"] == name_to_update :
            found = True 
            found_student = student 
    if found :
        score_to_update = get_valid_score("Enter student's score: ")
        found_student["score"] = score_to_update
        print("Score updated successfully.")
    else :
        print("Student not found.")

# DELETE STUDENT FUNCTION 
def delete_student():
    name_to_delete = get_valid_name("Enter name to delete: ")
    found = False 
    for student in students:
        if student["name"] == name_to_delete:
            students.remove(student)
            found = True 
    if not found :
        print("Student not found.")
    else :
        print("Student deleted successfully.")

# CHECKING PASSED STUDENTS
def passed_students():
    passed = False 
    if students :
        for student in students:
            if student["score"] >= 50 :
                print(student["name"],"->",student["score"])
                passed = True 
        if not passed:
            print("No students passed.")
    else :
        print("No Students available.")
    
# SHOWS STATISTICS
def show_statistics():
    if students :
        total_students = len(students)
        total_scores = 0 
        highest = students[0]["score"]
        lowest = students[0]["score"]
        for student in students :
            total_scores += student["score"]
            if student["score"] > highest:
                highest = student["score"]
            if student["score"] < lowest:
                lowest = student["score"]
        student_average = total_scores / total_students
        print("Total students: ",total_students)
        print("Average score: ",float(student_average))
        print("Highest score: ",highest)
        print("Lowest score: ",lowest)
    else :
        print("No students available.\n")

def show_unique_courses():
    if students :
        unique_courses = set()
        for student in students :
            unique_courses.add(student["course"])
        for each in unique_courses :
            print(each)
    else :
        print("No students available.")

def sort_students():
    if students :
            while True:
                    print("Sort by: ")
                    print("Name ")
                    print("Score ")
                    sorting_choice = (input("Enter choice(Name or Score) : ")).strip().lower()
                    if sorting_choice == "name" or sorting_choice == "score":
                        sorted_students = sorted(students,key=lambda student: student[sorting_choice])
                        for i in range(len(sorted_students)):
                            print(f"{i+1}. {sorted_students[i]['name']} | Score: {sorted_students[i]['score']}")
                        break
                    else :
                        print("Invalid option.\n")
    else :
        print("No students available.")

# MENU FUNCTION 
def show_menu():
    print("=" * 40)
    print("\tSTUDENT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("\n1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Update student score")
    print("5. Delete student")
    print("6. Show passed students")
    print("7. Show statistics")
    print("8. Show unique courses")
    print("9. Sort students")
    print("0. Exit")

# PROGRAM ENTTRY 
while True:
    show_menu()
    try :
        user_option = int(input("Choose an option(0-9): "))

        if user_option < 0 :
            print("Option can't be negative.")

        elif  user_option == 0 :
            print("Thank you, bye!")
            break

        elif user_option == 1 :
            add_student()

        elif user_option == 2 :
            view_students()

        elif user_option == 3 :
            search_student()

        elif user_option == 4 :
            update_student_score()

        elif user_option == 5 :
            delete_student()

        elif user_option == 6:
            passed_students()

        elif user_option == 7 :
            show_statistics()
        elif user_option == 8 :
            show_unique_courses()

        elif user_option == 9 :
            sort_students()

        else :
            print("Invalid option.\n")

    except ValueError:
        print("Your option should be a number(0-9)\n")