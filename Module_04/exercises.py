thirty_days_of_python = " ".join(("Thirty", "Days", "Of", "Python"))
print(f"{thirty_days_of_python}")

coding_for_all = " ".join(("Coding", "For", "All"))
print(f"{coding_for_all}")

company = "Coding For All"
print(f'company = "{company}"')
print(f"{company}")
print(f"{len(company)}")
print(f"{company.upper()}")
print(f"{company.lower()}")
print(f"{company.capitalize()} | {company.title()} | {company.swapcase()}")
print(f"{company[company.index(' ') + 1:]}")
print(f"{'Coding' in company}")
print(f"{company.replace('Coding', 'Python')}")

python_for_everyone = "Python for Everyone"
print(f"{python_for_everyone.replace('Everyone', 'All')}")
print(f"{company.split()}")

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(f"`{companies.split(', ')}")
print(f"{company[0]}")
print(f"{len(company) - 1}")
print(f"{company[10]!r}")

python_for_everyone = "Python For Everyone"
print(f"{''.join(word[0] for word in company.split())}")
print(f"{''.join(word[0] for word in python_for_everyone.split())}")
print(f"{company.index('C')}")
print(f"{company.index('F')}")

coding_for_all_people = "Coding For All People"
print(f"{coding_for_all_people.rfind('l')}")

sentence = "You cannot end a sentence with because because because is a conjunction"
first_because = sentence.index("because")
last_because = sentence.rindex("because")
because_phrase = sentence[first_because:last_because + len("because")]
print(f"{first_because}")
print(f"{last_because}")
print(f"{because_phrase}")
print(f"{sentence.find('because')}")
print(f"{sentence[first_because:last_because + len('because')]}")

print(f"{company.startswith('Coding')}")
print(f"{company.endswith('coding')}")

spaced_company = "  Coding For All   "
print(f"{spaced_company.strip()!r}")

invalid_identifier = "30DaysOfPython"
valid_identifier = "thirty_days_of_python"
print(f"{invalid_identifier.isidentifier()} | {valid_identifier.isidentifier()}")

libraries = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print(f"{'# '.join(libraries)}")

print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\tAge\tCountry\tCity")
print("    Asabeneh\t250\tFinland\tHelsinki")

radius = 10
area = 3.14 * radius**2
print("The area of a circle with radius {} is {:g} meters square.".format(radius, area))

first_number = 8
second_number = 6
print("{} + {} = {}".format(first_number, second_number, first_number + second_number))
print("{} - {} = {}".format(first_number, second_number, first_number - second_number))
print("{} * {} = {}".format(first_number, second_number, first_number * second_number))
print("{} / {} = {:.2f}".format(first_number, second_number, first_number / second_number))
print("{} % {} = {}".format(first_number, second_number, first_number % second_number))
print("{} // {} = {}".format(first_number, second_number, first_number // second_number))
print("{} ** {} = {}".format(first_number, second_number, first_number**second_number))