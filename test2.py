#boolean
is_available = True
is_active = False

print(type(is_available))

full_name = "Frank John"

get_by_index = full_name[0]
print(get_by_index)

get_by_index = full_name[1:3]
print(get_by_index.upper()) #upper case method

print(len(get_by_index)) # length fuction

#Data Structure
#list
#first method of creating a list
names_of_student = ["nathaniel", "udeme",
"frank", "john", "solomon"]

#second method of creating a list
names_of_girls = list(("rose","ruth", "sandra", "flora", "daniella"))

print("type of object: ", type(names_of_girls))

print(names_of_girls[2])

names_of_student[1] = "Lewis"

print(names_of_student)

names_of_student.append("udeme") # A method to add add item to the list
print(names_of_student)

print(len(names_of_student))

names_of_student.remove("john")
print(names_of_student)

#names = []
#names = list()  (empty list)
#name.append("frank")

#tuple
fruits = ("mango", "organge", "banana")

print(type(fruits))

names_of_boys = tuple(("franky", "solo", "godwin", "danny")) #wrap with 2 brackets
print(type(names_of_boys))

print(fruits[2])

#Sets(unordered list in python)

name_of_laptop = {"HP", "Toshiba", "lenova", "dell", "compaq"}

name_of_cars = set(("toyata", "lexus", "mourano"))

# print(type(name_of_laptop))
# print(type(name_of_cars))

print(name_of_laptop)
name_of_laptop.add("apple") #adding to a set

# creating dictionaries (a key value pair tye of data structure)

student_details = {
    "name" : "samuel john",
    "age" : "23",
    "location" : "united states",
    "previous_school" : "St. Lewis",
    "best_subject" : "mathematics"

}
print(type(student_details))

""" execirse
on an empty list user input list of ingridient for soup and print 
hold multiple dict in an empty list
"""

name_of_local_government = dict(akwaibom ="uyo", abia ="umuahia", anambra ="awka")

print(type(name_of_local_government))

print(student_details["location"])


