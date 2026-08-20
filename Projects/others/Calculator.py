# while True:
#     print("\n=== Python Calculator ===")
#     print("Type 'quit' to exit")
    
#     op = input("Choose operator + - * / : ")
#     if op == "quit":
#         print("Bye!")
#         break
        
#     if op not in ["+", "-", "*", "/"]:
#         print("Error: Invalid operator")
#         continue

#     try:
#         num1 = float(input("First number: "))
#         num2 = float(input("Second number: "))
#     except ValueError:
#         print("Error: Please enter numbers only")
#         continue

#     if op == "+":
#         result = num1 + num2
#     elif op == "-":
#         result = num1 - num2
#     elif op == "*":
#         result = num1 * num2
#     elif op == "/":
#         if num2 == 0:
#             print("Error: Can't divide by 0")
#             continue
#         result = num1 / num2

#     print(f"Result: {num1} {op} {num2} = {result}")


# def add(a,b):
#     return (a+b)
# def subtract(a,b):
#     return (a-b)
# def multiply(a,b):
#     return (a*b)
# def divide(a,b):
#     return (a/b)
# def init():
#     print("====== WELCOME ======")
#     print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
# init()
# user_option = int(input("Choose an option(1-4) : "))
# while True:
#     try :
#         user_num1 = int(input("Enter the first number(1-9) : "))
#         user_num2 = int(input("Enter the second number(1-9) : "))
#         break
#     except ValueError :
#         print("Enter a valid number.")
# if user_option == 1 :
#     print(f"The sum of {user_num1} and {user_num2} is : {add(user_num1,user_num2)}")
# elif user_option == 2 :
#     if user_num1 > user_num2 :
#         print(f"The subtraction of {user_num2} from {user_num1} is : {subtract(user_num1,user_num2)}")
#     else :
#         print(f"The subtraction of {user_num2} from {user_num1} is negative : {subtract(user_num1,user_num2)}")
# elif user_option == 3 :
#     print(f"The result : {multiply(user_num1,user_num2)}")
# elif user_option == 4 :
#     try :
#         print(f"The division of {user_num1} by {user_num2} is : {divide(user_num1,user_num2)}")
#     except ZeroDivisionError :
#         print("Cannot divide by zero(0)")

# print("Thank you ")
