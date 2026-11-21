print("LEVEL 1")

age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")

my_age = 26
your_age = int(input("Enter your age: "))
age_difference = abs(my_age - your_age)
if your_age > my_age:
    print(f"You are {age_difference} {'year' if age_difference == 1 else 'years'} older than me.")
elif your_age < my_age:
    print(f"I am {age_difference} {'year' if age_difference == 1 else 'years'} older than you.")
else:
    print("We are the same age.")

number_one = int(input("Enter number one: "))
number_two = int(input("Enter number two: "))
if number_one > number_two:
    print(f"{number_one} is greater than {number_two}")
elif number_one < number_two:
    print(f"{number_one} is smaller than {number_two}")
else:
    print(f"{number_one} is equal to {number_two}")

print("\nLEVEL 2")

score = int(input("Enter your score: "))
if score >= 80:
    print("A")
elif score >= 70:
    print("B")
elif score >= 60:
    print("C")
elif score >= 50:
    print("D")
else:
    print("F")

month = input("Enter a month: ").lower()
if month in ("september", "october", "november"):
    print("Autumn")
elif month in ("december", "january", "february"):
    print("Winter")
elif month in ("march", "april", "may"):
    print("Spring")
elif month in ("june", "july", "august"):
    print("Summer")
else:
    print("Invalid month")

fruits = ["banana", "orange", "mango", "lemon"]
fruit = input("Enter a fruit: ").lower()
if fruit in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(fruit)
    print(fruits)

print("\nLEVEL 3")

person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_married": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {
        "street": "Space street",
        "zipcode": "02210",
    },
}

if "skills" in person:
    skills = person["skills"]
    print(skills[len(skills) // 2])
    print("Python" in skills)

    if len(skills) == 2 and "JavaScript" in skills and "React" in skills:
        print("He is a front end developer")
    elif "Node" in skills and "Python" in skills and "MongoDB" in skills:
        print("He is a backend developer")
    elif "React" in skills and "Node" in skills and "MongoDB" in skills:
        print("He is a fullstack developer")
    else:
        print("unknown title")

if person["is_married"] and person["country"] == "Finland":
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
