from cmath import sqrt
from json import load
from keyword import iskeyword
from math import prod
from pathlib import Path
from statistics import mean, median, multimode, pstdev, pvariance


def add_two_numbers(number_one, number_two):
    return number_one + number_two


def area_of_circle(radius):
    return 3.14 * radius**2


def add_all_nums(*numbers):
    if all(isinstance(number, (int, float)) for number in numbers):
        return sum(numbers)
    return "All arguments must be numbers."


def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def check_season(month):
    month = month.lower()
    if month in ("september", "october", "november"):
        return "Autumn"
    if month in ("december", "january", "february"):
        return "Winter"
    if month in ("march", "april", "may"):
        return "Spring"
    if month in ("june", "july", "august"):
        return "Summer"
    return "Invalid month"


def calculate_slope(x_one, y_one, x_two, y_two):
    return (y_two - y_one) / (x_two - x_one)


def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4 * a * c
    return ((-b + sqrt(discriminant)) / (2 * a), (-b - sqrt(discriminant)) / (2 * a))


def print_list(items):
    for item in items:
        print(item)


def reverse_list(items):
    reversed_items = []
    for index in range(len(items) - 1, -1, -1):
        reversed_items.append(items[index])
    return reversed_items


def capitalize_list_items(items):
    return [item.capitalize() for item in items]


def add_item(items, item):
    return items + [item]


def remove_item(items, item):
    result = items.copy()
    if item in result:
        result.remove(item)
    return result


def sum_of_numbers(number):
    return sum(range(number + 1))


def sum_of_odds(number):
    return sum(value for value in range(number + 1) if value % 2)


def sum_of_even(number):
    return sum(value for value in range(number + 1) if value % 2 == 0)


def evens_and_odds(number):
    evens = sum(1 for value in range(number + 1) if value % 2 == 0)
    odds = number + 1 - evens
    return evens, odds


def factorial(number):
    return prod(range(1, number + 1))


def is_empty(value):
    return len(value) == 0


def calculate_mean(numbers):
    return mean(numbers)


def calculate_median(numbers):
    return median(numbers)


def calculate_mode(numbers):
    return multimode(numbers)


def calculate_range(numbers):
    return max(numbers) - min(numbers)


def calculate_variance(numbers):
    return pvariance(numbers)


def calculate_std(numbers):
    return pstdev(numbers)


def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False
    return True


def all_unique(items):
    return len(items) == len(set(items))


def same_data_type(items):
    return not items or all(type(item) is type(items[0]) for item in items)


def is_valid_variable(name):
    return name.isidentifier() and not iskeyword(name)


def most_spoken_languages(countries, number=10):
    language_counts = {}
    for country in countries:
        for language in country["languages"]:
            language_counts[language] = language_counts.get(language, 0) + 1
    return sorted(language_counts.items(), key=lambda item: item[1], reverse=True)[:number]


def most_populated_countries(countries, number=10):
    return sorted(countries, key=lambda country: country["population"], reverse=True)[:number]


print(add_two_numbers(2, 3))
print(area_of_circle(10))
print(add_all_nums(1, 2, 3))
print(add_all_nums(1, "two", 3))
print(convert_celsius_to_fahrenheit(25))
print(check_season("October"))
print(calculate_slope(1, 2, 3, 6))
print(solve_quadratic_eqn(1, -3, 2))
print_list(["Python", "Functions"])
print(reverse_list([1, 2, 3, 4, 5]))
print(capitalize_list_items(["python", "functions"]))
print(add_item(["Potato", "Tomato"], "Meat"))
print(remove_item(["Potato", "Tomato", "Mango"], "Mango"))
print(sum_of_numbers(10))
print(sum_of_odds(10))
print(sum_of_even(10))
print(evens_and_odds(100))
print(factorial(5))
print(is_empty([]))

numbers = [1, 2, 2, 3, 4]
print(calculate_mean(numbers))
print(calculate_median(numbers))
print(calculate_mode(numbers))
print(calculate_range(numbers))
print(calculate_variance(numbers))
print(calculate_std(numbers))

print(is_prime(7))
print(all_unique([1, 2, 3]))
print(same_data_type([1, 2, 3]))
print(is_valid_variable("valid_name"))

project_root = Path(__file__).resolve().parents[2]
data_path = project_root / "30-Days-of-Python-main" / "data" / "countries_data.json"
with data_path.open(encoding="utf-8") as file:
    countries = load(file)
print(most_spoken_languages(countries))
print([country["name"] for country in most_populated_countries(countries)])

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print([number for number in numbers if number <= 0])

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
print([number for outer in list_of_lists for inner in outer for number in inner])

print([tuple([number] + [number**power for power in range(6)]) for number in range(11)])

countries_and_cities = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]
print([[country.upper(), country[:3].upper(), city.upper()] for group in countries_and_cities for country, city in group])
print([{"country": country.upper(), "city": city.upper()} for group in countries_and_cities for country, city in group])

names = [[("Asabeneh", "Yetayeh")], [("David", "Smith")], [("Donald", "Trump")], [("Bill", "Gates")]]
print([f"{first_name} {last_name}" for group in names for first_name, last_name in group])

line_parameters = lambda x_one, y_one, x_two, y_two: (
    (y_two - y_one) / (x_two - x_one),
    y_one - ((y_two - y_one) / (x_two - x_one)) * x_one,
)
print(line_parameters(1, 3, 3, 7))
