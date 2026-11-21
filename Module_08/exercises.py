from json import load
from pathlib import Path
from runpy import run_path

print("For loop from 0 to 10")
for number in range(11):
    print(number)

print("While loop from 0 to 10")
number = 0
while number <= 10:
    print(number)
    number += 1

print("For loop from 10 to 0")
for number in range(10, -1, -1):
    print(number)

print("While loop from 10 to 0")
number = 10
while number >= 0:
    print(number)
    number -= 1

for number in range(1, 8):
    print("#" * number)

for row_number in range(8):
    row = []
    for column_number in range(8):
        row.append("#")
    print(" ".join(row))

for number in range(11):
    print(f"{number} x {number} = {number * number}")

for technology in ["Python", "Numpy", "Pandas", "Django", "Flask"]:
    print(technology)

for number in range(101):
    if number % 2 == 0:
        print(number)

for number in range(101):
    if number % 2 != 0:
        print(number)

number_sum = 0
for number in range(101):
    number_sum += number
print(f"The sum of all numbers is {number_sum}.")

even_sum = 0
odd_sum = 0
for number in range(101):
    if number % 2 == 0:
        even_sum += number
    else:
        odd_sum += number
print(f"The sum of all evens is {even_sum}. And the sum of all odds is {odd_sum}.")

project_root = Path(__file__).resolve().parents[2]
data_folder = project_root / "30-Days-of-Python-main" / "data"
countries = run_path(str(data_folder / "countries.py"))["countries"]
for country in countries:
    if "land" in country.lower():
        print(country)

fruits = ["banana", "orange", "mango", "lemon"]
reversed_fruits = []
for index in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[index])
print(reversed_fruits)

with (data_folder / "countries_data.json").open(encoding="utf-8") as file:
    countries_data = load(file)

language_counts = {}
for country in countries_data:
    for language in country["languages"]:
        language_counts[language] = language_counts.get(language, 0) + 1

print(f"Total languages: {len(language_counts)}")
for language, count in sorted(language_counts.items(), key=lambda item: item[1], reverse=True)[:10]:
    print(language, count)

for country in sorted(countries_data, key=lambda item: item["population"], reverse=True)[:10]:
    print(country["name"], country["population"])
