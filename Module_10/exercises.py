from functools import reduce
from json import load
from pathlib import Path
from runpy import run_path

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("map applies a function to every item, filter selects items, and reduce combines the items into one value.")
print("A higher-order function takes or returns a function. A closure retains values from its enclosing scope. A decorator wraps a function to extend its behavior.")


def sum_numbers(values):
    return sum(values)


def is_even(number):
    return number % 2 == 0


print(sum_numbers(numbers))
print(list(filter(is_even, numbers)))
print(reduce(lambda total, number: total + number, numbers))

for country in countries:
    print(country)

for name in names:
    print(name)

for number in numbers:
    print(number)

print(list(map(str.upper, countries)))
print(list(map(lambda number: number**2, numbers)))
print(list(map(str.upper, names)))
print(list(filter(lambda country: "land" in country.lower(), countries)))
print(list(filter(lambda country: len(country) == 6, countries)))
print(list(filter(lambda country: len(country) >= 6, countries)))
print(list(filter(lambda country: country.startswith("E"), countries)))
print(list(filter(is_even, map(lambda number: number**2, numbers))))


def get_string_lists(items):
    return [item for item in items if isinstance(item, str)]


print(get_string_lists(["Python", 1, "Java", 2]))
print(reduce(lambda total, number: total + number, numbers))
print(
    reduce(
        lambda sentence, country: f"{sentence}, and {country}" if country == countries[-1] else f"{sentence}, {country}",
        countries,
    )
    + " are north European countries"
)

country_names = run_path(
    str(Path(__file__).resolve().parents[2] / "30-Days-of-Python-main" / "data" / "countries.py")
)["countries"]


def categorize_countries(pattern):
    return [country for country in country_names if pattern.lower() in country.lower()]


def count_countries_by_starting_letter():
    counts = {}
    for country in country_names:
        first_letter = country[0].upper()
        counts[first_letter] = counts.get(first_letter, 0) + 1
    return counts


def get_first_ten_countries():
    return country_names[:10]


def get_last_ten_countries():
    return country_names[-10:]


print(categorize_countries("land"))
print(count_countries_by_starting_letter())
print(get_first_ten_countries())
print(get_last_ten_countries())

project_root = Path(__file__).resolve().parents[2]
data_path = project_root / "30-Days-of-Python-main" / "data" / "countries_data.json"
with data_path.open(encoding="utf-8") as file:
    countries_data = load(file)

print(sorted(country["name"] for country in countries_data))
print(sorted(country["capital"] for country in countries_data))
print([country["name"] for country in sorted(countries_data, key=lambda country: country["population"])])

language_counts = {}
for country in countries_data:
    for language in country["languages"]:
        language_counts[language] = language_counts.get(language, 0) + 1

print(sorted(language_counts.items(), key=lambda item: item[1], reverse=True)[:10])
print([country["name"] for country in sorted(countries_data, key=lambda country: country["population"], reverse=True)[:10]])
