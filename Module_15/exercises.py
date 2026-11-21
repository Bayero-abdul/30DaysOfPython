import json
import re
import statistics
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen

project_root = Path(__file__).resolve().parents[2]
data_folder = project_root / "30-Days-of-Python-main" / "data"


def read_url(url):
    request = Request(url, headers={"User-Agent": "Python learning exercise"})
    with urlopen(request, timeout=15) as response:
        return response.read()


def most_common_words(text, number):
    words = re.findall(r"[A-Za-z]+", text.lower())
    return Counter(words).most_common(number)


romeo_url = "https://www.gutenberg.org/files/1112/1112.txt"
try:
    romeo_text = read_url(romeo_url).decode("utf-8", errors="replace")
except (URLError, TimeoutError):
    romeo_text = (data_folder / "romeo_and_juliet.txt").read_text(encoding="utf-8")
print(most_common_words(romeo_text, 10))


def numeric_range(value):
    numbers = [float(number) for number in re.findall(r"\d+(?:\.\d+)?", value)]
    if len(numbers) == 1:
        return numbers[0]
    return statistics.mean(numbers)


def describe(values):
    return {
        "min": min(values),
        "max": max(values),
        "mean": statistics.mean(values),
        "median": statistics.median(values),
        "standard_deviation": statistics.stdev(values),
    }


cats = json.loads((data_folder / "cats.json").read_text(encoding="utf-8"))
weights = [numeric_range(cat["weight"]["metric"]) for cat in cats]
lifespans = [numeric_range(cat["life_span"]) for cat in cats]
print(describe(weights))
print(describe(lifespans))

breeds_by_country = defaultdict(list)
for cat in cats:
    country = cat.get("origin", "Unknown")
    breeds_by_country[country].append(cat["name"])
print(Counter((country, breed) for country, breeds in breeds_by_country.items() for breed in breeds))


def load_countries():
    url = "https://raw.githubusercontent.com/mledoze/countries/master/countries.json"
    try:
        return json.loads(read_url(url))
    except (URLError, TimeoutError):
        return json.loads((data_folder / "countries_data.json").read_text(encoding="utf-8"))


def country_name(country):
    name = country["name"]
    return name["common"] if isinstance(name, dict) else name


countries = load_countries()
area_countries = [country for country in countries if country.get("area") is not None]
largest_countries = sorted(area_countries, key=lambda country: country["area"], reverse=True)[:10]
print([(country_name(country), country["area"]) for country in largest_countries])

language_counts = Counter()
for country in countries:
    languages = country.get("languages", [])
    language_counts.update(languages.values() if isinstance(languages, dict) else languages)
print(language_counts.most_common(10))
print(len(language_counts))


class DatasetLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.current_link = None
        self.seen_links = set()

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href", "")
            if "/dataset/" in href:
                self.current_link = {"url": href, "text": ""}

    def handle_data(self, data):
        if self.current_link is not None:
            self.current_link["text"] += data.strip()

    def handle_endtag(self, tag):
        if tag == "a" and self.current_link is not None:
            href = self.current_link["url"]
            if self.current_link["text"] and href not in self.seen_links:
                self.links.append(self.current_link)
                self.seen_links.add(href)
            self.current_link = None


try:
    catalog_html = read_url("https://archive.ics.uci.edu/datasets").decode("utf-8", errors="replace")
    catalog = DatasetLinks()
    catalog.feed(catalog_html)
    print(len(catalog.links), catalog.links[:10])
except (URLError, TimeoutError) as error:
    print(f"UCI catalog unavailable: {error}")
