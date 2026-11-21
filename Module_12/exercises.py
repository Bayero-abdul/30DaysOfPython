import re
from collections import Counter
from keyword import iskeyword

paragraph = (
    "I love teaching. If you do not love teaching what else can you love. "
    "I love Python if you do not love something which can give you all the "
    "capabilities to develop an application what else can you love."
)
words = re.findall(r"[A-Za-z]+", paragraph)
print(sorted(((count, word) for word, count in Counter(words).items()), reverse=True))

points_text = "The positions are -12, -4, -3, -1, 0, 4 and 8."
points = [int(point) for point in re.findall(r"-?\d+", points_text)]
print(points)
print(max(points) - min(points))


def is_valid_variable(name):
    return bool(re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", name)) and not iskeyword(name)


print(is_valid_variable("first_name"))
print(is_valid_variable("first-name"))
print(is_valid_variable("1first_name"))
print(is_valid_variable("firstname"))

sentence = (
    """%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; """
    """&as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. """
    """;I found tea@ching m%o@re interesting tha@n any other %jo@bs. """
    """%Do@es thi%s mo@tivate yo@u to be a tea@cher!?"""
)


def clean_text(text):
    cleaned = re.sub(r"[^A-Za-z\s]", "", text)
    return re.sub(r"\s+", " ", cleaned).strip()


def most_frequent_words(text):
    counts = Counter(re.findall(r"[A-Za-z]+", text))
    return sorted(((count, word) for word, count in counts.items()), reverse=True)[:3]


cleaned_text = clean_text(sentence)
print(cleaned_text)
print(most_frequent_words(cleaned_text))
