from pathlib import Path
from runpy import run_path


print("LIST EXERCISES - LEVEL 1")
empty_list = []
print(f"Empty list: {empty_list}")

items = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
print(f"List with more than five items: {items}")
print(f"List length: {len(items)}")
print(f"First, middle, last: {items[0]}, {items[len(items) // 2]}, {items[-1]}")

mixed_data_types = ["Abdulkadir", 26, 1.75, False, "Zaria, Nigeria"]
print(f"Mixed data types: {mixed_data_types}")

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(f"IT companies: {it_companies}")
print(f"Number of companies: {len(it_companies)}")
print(f"First, middle, last company: {it_companies[0]}, {it_companies[len(it_companies) // 2]}, {it_companies[-1]}")

it_companies[0] = "Meta"
print(f"Modified company list: {it_companies}")
it_companies.append("Twitter")
print(f"Added a company: {it_companies}")
it_companies.insert(len(it_companies) // 2, "NVIDIA")
print(f"Inserted NVIDIA in the middle: {it_companies}")
it_companies[1] = it_companies[1].upper()
print(f"Uppercase company name (not IBM): {it_companies}")
print(f"Joined companies: {'#; '.join(it_companies)}")
print(f"Is Meta in the list? {'Meta' in it_companies}")

it_companies.sort()
print(f"Sorted companies: {it_companies}")
it_companies.reverse()
print(f"Reversed companies: {it_companies}")
print(f"First three companies: {it_companies[:3]}")
print(f"Last three companies: {it_companies[-3:]}")

middle_start = (len(it_companies) - 1) // 2
middle_end = (len(it_companies) + 2) // 2
print(f"Middle company or companies: {it_companies[middle_start:middle_end]}")
removed_first = it_companies.pop(0)
print(f"Removed first company ({removed_first}): {it_companies}")

middle_start = (len(it_companies) - 1) // 2
middle_end = (len(it_companies) + 2) // 2
removed_middle = it_companies[middle_start:middle_end]
del it_companies[middle_start:middle_end]
print(f"Removed middle company or companies ({removed_middle}): {it_companies}")
removed_last = it_companies.pop()
print(f"Removed last company ({removed_last}): {it_companies}")
it_companies.clear()
print(f"Removed all companies: {it_companies}")
del it_companies
print("Deleted the it_companies list")

front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]
joined_stack = front_end + back_end
print(f"Joined front-end and back-end lists: {joined_stack}")
full_stack = joined_stack.copy()
redux_index = full_stack.index("Redux")
full_stack[redux_index + 1:redux_index + 1] = ["Python", "SQL"]
print(f"Full stack with Python and SQL after Redux: {full_stack}")


print("\nLIST EXERCISES - LEVEL 2")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
minimum_age = min(ages)
maximum_age = max(ages)
print(f"Sorted ages: {ages}; minimum: {minimum_age}; maximum: {maximum_age}")
ages.extend([minimum_age, maximum_age])
ages.sort()
middle = len(ages) // 2
median_age = (ages[middle - 1] + ages[middle]) / 2 if len(ages) % 2 == 0 else ages[middle]
average_age = sum(ages) / len(ages)
age_range = maximum_age - minimum_age
print(f"Ages with min and max added: {ages}")
print(f"Median age: {median_age}")
print(f"Average age: {average_age:g}")
print(f"Age range: {age_range}")
print(f"abs(min - average) = {abs(minimum_age - average_age):g}; abs(max - average) = {abs(maximum_age - average_age):g}")

countries_path = Path(__file__).resolve().parents[1] / ".." / "30-Days-of-Python-main" / "data" / "countries.py"
countries = run_path(str(countries_path.resolve()))["countries"]
country_middle = len(countries) // 2
middle_countries = countries[country_middle:country_middle + 1] if len(countries) % 2 else countries[country_middle - 1:country_middle + 1]
print(f"Middle country or countries in the supplied dataset: {middle_countries}")
first_half_size = (len(countries) + 1) // 2
print(f"Countries split into halves of {first_half_size} and {len(countries) - first_half_size}: {countries[:first_half_size]} | {countries[first_half_size:]}")

china, russia, usa, *scandic_countries = ["China", "Russia", "USA", "Finland", "Sweden", "Norway", "Denmark"]
print(f"First three countries: {[china, russia, usa]}; scandic countries: {scandic_countries}")


print("\nTUPLE EXERCISES - LEVEL 1")
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")
brothers = ("Liam", "Noah")
sisters = ("Ava", "Mia")
print(f"Brothers: {brothers}; sisters: {sisters}")
siblings = brothers + sisters
print(f"Siblings: {siblings}")
print(f"Number of siblings: {len(siblings)}")
family_members = siblings + ("James", "Olivia")
print(f"Family members: {family_members}")


print("\nTUPLE EXERCISES - LEVEL 2")
*siblings, father, mother = family_members
print(f"Siblings: {siblings}; parents: {(father, mother)}")
fruits = ("banana", "orange", "mango", "avocado")
vegetables = ("tomato", "potato", "cabbage", "onion", "carrot")
animal_products = ("milk", "meat", "butter", "yoghurt")
food_stuff_tp = fruits + vegetables + animal_products
print(f"Food tuple: {food_stuff_tp}")
food_stuff_lt = list(food_stuff_tp)
print(f"Food list: {food_stuff_lt}")
food_middle = len(food_stuff_tp) // 2
middle_food = food_stuff_tp[food_middle:food_middle + 1] if len(food_stuff_tp) % 2 else food_stuff_tp[food_middle - 1:food_middle + 1]
print(f"Middle food item or items: {middle_food}")
print(f"First three foods: {food_stuff_lt[:3]}; last three foods: {food_stuff_lt[-3:]}")
del food_stuff_tp
print("Deleted the food_stuff_tp tuple")
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
print(f"Is Estonia Nordic? {'Estonia' in nordic_countries}")
print(f"Is Iceland Nordic? {'Iceland' in nordic_countries}")


print("\nSET EXERCISES - LEVEL 1")
it_companies_set = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
print(f"Number of companies: {len(it_companies_set)}")
it_companies_set.add("Twitter")
print(f"Added Twitter: {sorted(it_companies_set)}")
it_companies_set.update({"NVIDIA", "LinkedIn", "Salesforce"})
print(f"Added multiple companies: {sorted(it_companies_set)}")
it_companies_set.remove("Facebook")
print(f"Removed Facebook: {sorted(it_companies_set)}")
print("remove() raises KeyError if the item is absent; discard() leaves the set unchanged.")


print("\nSET EXERCISES - LEVEL 2")
set_a = {19, 22, 24, 20, 25, 26}
set_b = {19, 22, 20, 25, 26, 24, 28, 27}
print(f"A union B: {sorted(set_a | set_b)}")
print(f"A intersection B: {sorted(set_a & set_b)}")
print(f"Is A a subset of B? {set_a.issubset(set_b)}")
print(f"Are A and B disjoint? {set_a.isdisjoint(set_b)}")
print(f"A union B: {sorted(set_a.union(set_b))}; B union A: {sorted(set_b.union(set_a))}")
print(f"Symmetric difference: {sorted(set_a.symmetric_difference(set_b))}")
del set_a, set_b
print("Deleted sets A and B")


print("\nSET EXERCISES - LEVEL 3")
age_list = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age_list)
print(f"List length: {len(age_list)}; set length: {len(age_set)}; the list is bigger.")
print("A string is immutable text; a list is ordered and mutable; a tuple is ordered and immutable; a set is mutable and stores unique, unordered items.")
sentence = "I am a teacher and I love to inspire and teach people."
unique_words = set(sentence.split())
print(f"Unique words ({len(unique_words)}): {sorted(unique_words)}")