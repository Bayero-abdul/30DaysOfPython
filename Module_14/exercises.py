import random
import string


def random_user_id():
    characters = string.ascii_letters + string.digits
    return "".join(random.choices(characters, k=6))


def user_id_gen_by_user():
    character_count = int(input("Number of characters: "))
    id_count = int(input("Number of IDs: "))
    characters = string.ascii_letters + string.digits
    ids = ["".join(random.choices(characters, k=character_count)) for _ in range(id_count)]
    return "\n".join(ids)


def rgb_color_gen():
    red, green, blue = (random.randint(0, 255) for _ in range(3))
    return f"rgb({red},{green},{blue})"


def list_of_hexa_colors(count):
    return [f"#{random.randint(0, 0xFFFFFF):06x}" for _ in range(count)]


def list_of_rgb_colors(count):
    return [rgb_color_gen() for _ in range(count)]


def generate_colors(color_type, count):
    if color_type == "hexa":
        return list_of_hexa_colors(count)
    if color_type == "rgb":
        return list_of_rgb_colors(count)
    return []


def shuffle_list(items):
    shuffled_items = items.copy()
    random.shuffle(shuffled_items)
    return shuffled_items


def seven_unique_digits():
    return random.sample(range(10), 7)


print(random_user_id())
print(user_id_gen_by_user())
print(rgb_color_gen())
print(list_of_hexa_colors(3))
print(list_of_rgb_colors(3))
print(generate_colors("hexa", 3))
print(generate_colors("rgb", 3))
print(shuffle_list([1, 2, 3, 4, 5]))
print(seven_unique_digits())
