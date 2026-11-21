dog = {}
print(dog)

dog["name"] = "Buddy"
dog["color"] = "brown"
dog["breed"] = "Labrador"
dog["legs"] = 4
dog["age"] = 3
print(dog)

student = {
    "first_name": "Alex",
    "last_name": "Morgan",
    "gender": "unspecified",
    "age": 20,
    "marital_status": False,
    "skills": ["Python", "HTML"],
    "country": "Nigeria",
    "city": "Zaria",
    "address": "Main Street",
}

print(len(student))
print(student["skills"])
print(type(student["skills"]))

student["skills"].extend(["CSS", "JavaScript"])
print(student["skills"])

print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))

student.pop("age")
print(student)

del dog
