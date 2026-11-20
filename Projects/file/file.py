# opening a file through python 
# file = open("notes.txt")
# content = file.read()
# print(content)
# file.close()
# or like this :
# with open("notes.txt") as file :
#     content = file.read()
# print(content)

# with open("student.txt") as file :
#     content = file.read()
# print(content)

with open("test.txt","a")  as file:
    content = file.read()
print(content)
