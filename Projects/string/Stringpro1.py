def introduction():
    print("=" * 40)
    print("\tEMPLOYEE RECORD SYSTEM")
    print("=" * 40)

introduction()
user_entry = input("Enter the records : ")
user_entry = user_entry.split("|")

employee = user_entry[0].strip()
field = user_entry[1].strip()
ai = user_entry[2].strip()
mail = user_entry[3].strip()

employee = employee.title()
field = field.title()
ai = ai.capitalize()
mail = mail.lower()

employee_tag = employee[:3].upper()
field_tag = field[:3].upper()
ai_tag = ai[:3].upper()
code = "-".join([employee_tag, field_tag])

employee_ab = employee[0].upper()
employee_abl = employee[-1]
initials = employee[0] + employee[8]
employee_reverse = employee[::-1].title()

print(
    f"{'Employee Name':<10} : {employee}\n"
    f"{'Department':<10} : {field}\n"
    f"{'Company':<10} : {ai}\n"
    f"{'Email':<10} : {mail}\n\n"
    f"{'Employee Code':<10} : {code}\n"
    f"{'Company Code':<10} : {ai_tag}\n\n"
    f"{'-' * 40}"
)

print(
    "\nSTRING ANALYSIS\n\n"
    f"{'First Letter of Name':<10} : {employee_ab}\n"
    f"{'Last Letter of Name':<10} : {employee_abl}\n\n"
    f"{'Initials':<10} : {initials}\n\n"
    f"{'Company Abbreviation':<10} : {ai_tag}\n\n"
    f"{'Reversed Name':<10} : {employee_reverse}\n\n"
    f"{'-' * 40}\n"
)

print(
    "Employee successfully registered !"   
)
