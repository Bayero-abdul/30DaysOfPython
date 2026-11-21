# Write a python comment saying 'Day 2: 30 Days of python programming'
"""Day 2: 30 Days of python programming"""

# Exercises: Level 1

first_name = "Abdulkadir"
last_name = "Bayero"
full_name = first_name + " " + last_name
country = "Nigeria"
city = "Zaria"
age = 26
year = 2026
is_married = False
is_true = True
is_light_on = True
first_name, last_name, full_name = "Abdulkadir", "Bayero", "Abdulkadir Bayero"

# Exercises: Level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))
print(len(last_name))

if len(first_name) > len(last_name):
    print("First name is longer than last name")
elif len(first_name) < len(last_name):
    print("Last name is longer than first name")
else:
    print("First name and last name have the same length")

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two


area_of_circle = 3.14 * 30 ** 2
circum_of_circle = 2 * 3.14 * 30  
radius = float(input("Enter the radius of the circle: "))
area_of_circle_user = 3.14 * radius ** 2

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))

help('keywords')