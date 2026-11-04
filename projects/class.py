# class Subject:
#     pass

# elephant = Subject()
# elephant.name = "Elephant"
# elephant.category = "Nature & Life"
# elephant.description = "Largest land animal on earth."
# print(elephant.name)
# print(elephant.category)
# print(elephant.description)


####################
# class Subject:
#     def __init__(self,name,category):
#         self.name = name
#         self.category = category

#     def change_category(self,new_category):
#         self.category = new_category

#     def describe(self):
#         print(f"{self.name} belongs to the {self.category} category.")

# saturn = Subject(
#     "Saturn",
#     "Space & Astronomy"
# )
# heart = Subject(
#     "Human heart",
#     "Human Body"
# )
# class Animal(Subject):
#     def describe(self):
#         super().describe()
#         print(f"{self.name} is an animal in {self.category}.")

# saturn = Animal(
#     "Saturn",
#     "Nature & Life"
# )
# saturn.describe()


# saturn.change_category("Science & Technology")
# print(heart.name)
# print(heart.category)
# print(saturn.name)
# print(saturn.category)
# saturn.describe()
# heart.describe()


##############################

# class Subject:
#     def __init__(self, name , category):
#         self.name = name
#         self.category = category
#     def describe(self):
#         print(f"{self.name} is from the {self.category} category.")


# class Planet(Subject):
#     def describe(self):
#         super().describe()
#         print(f"{self.name} is a part of {self.category}.")

# jupiter = Planet(
#     "Jupiter",
#     "Big Planet"
# )
# jupiter.describe()

###########################
# class Subject:
#     def __init__(self,name ,category ,description):
#         self.name = name
#         self.category = category
#         self.description = description

#     def rename(self, new_name):
#         self.name = new_name

#     def describe(self):
#         print(f"{self.name} belongs to {self.category}")
#         print(f"{self.description}")

# jupiter = Subject(
#     "Jupiter",
#     "Space & Astronomy",
#     "The largest planet in our Solar System."
# )
# jupiter.rename("Planet Jupiter")
# jupiter.describe()

##########################
# class Subject:
#     def __init__(self, name, category):
#         self.name = name
#         self.category = category
#     def describe(self):
#         print(f"{self.name} is from the {self.category}.")

# class Planet(Subject):
#     def describe(self):
#         print(f"{self.name} is a planet in our {self.category}.")

# jupiter = Planet("Jupiter","Solar System")
# jupiter.describe()


#########################
# class Subject:
#     def __init__(self, name, category):
#         self.name = name
#         self.category = category

#     def describe(self):
#         print(f"{self.name} is in {self.category} category.")


# class Planet(Subject):
#     def __init__(self, name, category, number_of_moons: int):
#         super().__init__(name, category)
#         self.number_of_moons = number_of_moons

#     def show_moons(self):
#         print(f"The number of the moons : {self.number_of_moons}")


# jupiter = Planet("Jupiter", "Space & Astronomy", 95)
# jupiter.describe()
# jupiter.show_moons()
