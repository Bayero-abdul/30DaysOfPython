import importlib
import math

try:
    compile("print 'hello world'", "<example>", "exec")
except SyntaxError as error:
    print(type(error).__name__)

try:
    print(undefined_age)
except NameError as error:
    print(type(error).__name__)

numbers = [1, 2, 3, 4, 5]
try:
    print(numbers[5])
except IndexError as error:
    print(type(error).__name__)

try:
    importlib.import_module("maths")
except ModuleNotFoundError as error:
    print(type(error).__name__)

try:
    print(math.PI)
except AttributeError as error:
    print(type(error).__name__)
print(math.pi)

user = {"name": "Asab", "age": 250, "country": "Finland"}
try:
    print(user["county"])
except KeyError as error:
    print(type(error).__name__)
print(user["country"])

try:
    print(4 + "3")
except TypeError as error:
    print(type(error).__name__)
print(4 + int("3"))

try:
    from math import power
except ImportError as error:
    print(type(error).__name__)
print(math.pow(2, 3))

try:
    int("12a")
except ValueError as error:
    print(type(error).__name__)

try:
    print(1 / 0)
except ZeroDivisionError as error:
    print(type(error).__name__)

try:
    name = "Asabeneh"
    year_born = "1920"
    age = 2019 - year_born
except TypeError:
    print("Type error occurred")

try:
    name = "Asabeneh"
    year_born = "1920"
    age = 2019 - int(year_born)
except ValueError:
    print("Value error occurred")
else:
    print(f"You are {name}. And your age is {age}.")
finally:
    print("This always runs.")


def sum_of_five_numbers(first, second, third, fourth, fifth):
    return first + second + third + fourth + fifth


values = [1, 2, 3, 4, 5]
print(sum_of_five_numbers(*values))
print(list(range(*[2, 7])))

countries = ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]
finland, sweden, norway, *rest = countries
print(finland, sweden, norway, rest)

numbers = [1, 2, 3, 4, 5, 6, 7]
first, *middle, last = numbers
print(first, middle, last)


def unpack_person(name, country, city, age):
    return f"{name} lives in {country}, {city}. He is {age} years old."


person = {"name": "Asabeneh", "country": "Finland", "city": "Helsinki", "age": 250}
print(unpack_person(**person))


def sum_all(*values):
    return sum(values)


print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5, 6, 7))


def packing_person_info(**details):
    return details


print(packing_person_info(name="Asabeneh", country="Finland", city="Helsinki", age=250))

first_numbers = [1, 2, 3]
second_numbers = [4, 5, 6, 7]
print([0, *first_numbers, *second_numbers])

nordic_countries = ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]
print(nordic_countries)

for index, country in enumerate(nordic_countries):
    print(index, country)

fruits = ["banana", "orange", "mango", "lemon", "lime"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
fruits_and_vegetables = []
for fruit, vegetable in zip(fruits, vegetables):
    fruits_and_vegetables.append({"fruit": fruit, "veg": vegetable})
print(fruits_and_vegetables)

countries = ["Finland", "Sweden", "Norway", "Denmark", "Iceland", "Estonia", "Russia"]
*nordic_countries, es, ru = countries
print(nordic_countries, es, ru)
