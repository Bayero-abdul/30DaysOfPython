import csv
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from runpy import run_path

project_root = Path(__file__).resolve().parents[2]
data_folder = project_root / "30-Days-of-Python-main" / "data"
files_folder = project_root / "30-Days-of-Python-main" / "files"

now = datetime.now()
print(now.day, now.month, now.year, now.hour, now.minute, now.timestamp())
print(now.strftime("%m/%d/%Y, %H:%M:%S"))
print(datetime.strptime("5 December, 2019", "%d %B, %Y"))
new_year = datetime(now.year + 1, 1, 1)
print(new_year - now)
print(now - datetime(1970, 1, 1))
print("Date and time are useful for time series, activity timestamps, and post dates.")


def count_lines_and_words(filename):
    text = (data_folder / filename).read_text(encoding="utf-8")
    return len(text.splitlines()), len(text.split())


def get_data_path(filename):
    path = Path(filename)
    if path.is_file():
        return path
    return data_folder / path.name


for speech in (
    "obama_speech.txt",
    "michelle_obama_speech.txt",
    "donald_speech.txt",
    "melina_trump_speech.txt",
):
    print(speech, count_lines_and_words(speech))


def most_spoken_languages(filename, number):
    with get_data_path(filename).open(encoding="utf-8") as file:
        countries = json.load(file)
    language_counts = Counter(
        language for country in countries for language in country["languages"]
    )
    return sorted(((count, language) for language, count in language_counts.items()), reverse=True)[:number]


def most_populated_countries(filename, number):
    with get_data_path(filename).open(encoding="utf-8") as file:
        countries = json.load(file)
    countries_by_population = sorted(
        countries, key=lambda country: country["population"], reverse=True
    )[:number]
    return [
        {"country": country["name"], "population": country["population"]}
        for country in countries_by_population
    ]


print(most_spoken_languages("./data/countries_data.json", 10))
print(most_populated_countries("./data/countries_data.json", 10))

email_text = (data_folder / "email_exchanges_big.txt").read_text(encoding="utf-8")
email_addresses = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email_text)
print(email_addresses)


def read_text(source):
    if isinstance(source, Path):
        return source.read_text(encoding="utf-8")
    if "\n" not in source and len(source) < 256:
        path = Path(source)
        if path.is_file():
            return path.read_text(encoding="utf-8")
    return source


def find_most_common_words(source, number):
    words = re.findall(r"[A-Za-z]+", read_text(source))
    counts = Counter(words)
    return sorted(((count, word) for word, count in counts.items()), reverse=True)[:number]


def find_most_frequent_words(source, number):
    return find_most_common_words(source, number)


print(find_most_common_words(files_folder / "example.txt", 10))
for speech in (
    "obama_speech.txt",
    "michelle_obama_speech.txt",
    "donald_speech.txt",
    "melina_trump_speech.txt",
):
    print(speech, find_most_frequent_words(data_folder / speech, 10))


def clean_text(text):
    return " ".join(re.findall(r"[A-Za-z]+", text.lower()))


def remove_support_words(text):
    stop_words = run_path(str(data_folder / "stop_words.py"))["stop_words"]
    return [word for word in clean_text(text).split() if word not in stop_words]


def check_text_similarity(first_source, second_source):
    first_words = set(remove_support_words(read_text(first_source)))
    second_words = set(remove_support_words(read_text(second_source)))
    shared_words = first_words & second_words
    all_words = first_words | second_words
    return len(shared_words) / len(all_words) if all_words else 0


print(check_text_similarity(
    data_folder / "michelle_obama_speech.txt",
    data_folder / "melina_trump_speech.txt",
))
print(find_most_frequent_words(data_folder / "romeo_and_juliet.txt", 10))

with (data_folder / "hacker_news.csv").open(encoding="utf-8", newline="") as file:
    hacker_news_rows = list(csv.reader(file))

python_lines = sum(any("python" in cell.lower() for cell in row) for row in hacker_news_rows)
javascript_lines = sum(any("javascript" in cell.lower() for cell in row) for row in hacker_news_rows)
java_lines = sum(
    any("java" in cell.lower() for cell in row)
    and not any("javascript" in cell.lower() for cell in row)
    for row in hacker_news_rows
)
print(python_lines, javascript_lines, java_lines)
