import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen

OUTPUT_DIR = Path(__file__).resolve().parent


def fetch_page(url):
    request = Request(url, headers={"User-Agent": "Python learning exercise contact: student@example.com"})
    with urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def save_json(filename, data):
    path = OUTPUT_DIR / filename
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Saved {path.name}")


class BUFactsParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.headings = []
        self.list_items = []
        self.stats = []
        self.pending_stat = None
        self.stat_values = []
        self.current_heading = None
        self.current_item = None
        self.capture = None
        self.buffer = []

    def handle_starttag(self, tag, attrs):
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.save_stat()
            self.capture = "heading"
            self.buffer = []
        elif tag == "li":
            self.capture = "list_item"
            self.buffer = []

    def handle_data(self, data):
        if self.capture and data.strip():
            self.buffer.append(data.strip())
        elif self.pending_stat and data.strip():
            self.stat_values.append(data.strip())

    def save_stat(self):
        if self.pending_stat:
            value = " ".join(self.stat_values)
            if value:
                self.stats.append({"name": self.pending_stat, "value": value})
        self.pending_stat = None
        self.stat_values = []

    def handle_endtag(self, tag):
        if self.capture == "heading" and tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            heading = " ".join(self.buffer)
            if heading:
                self.headings.append(heading)
                if tag == "h3":
                    self.pending_stat = heading
            self.capture = None
            self.buffer = []
        elif self.capture == "list_item" and tag == "li":
            item = " ".join(self.buffer)
            if item:
                self.list_items.append(item)
            self.capture = None
            self.buffer = []


class DatasetLinksParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.datasets = []
        self.seen = set()
        self.current = None

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        href = attributes.get("href", "")
        if tag == "a" and "/dataset/" in href:
            self.current = {"url": href, "name": ""}

    def handle_data(self, data):
        if self.current and data.strip():
            self.current["name"] += data.strip()

    def handle_endtag(self, tag):
        if tag == "a" and self.current:
            url = self.current["url"]
            if self.current["name"] and url not in self.seen:
                self.current["url"] = "https://archive.ics.uci.edu" + url
                self.datasets.append(self.current)
                self.seen.add(url)
            self.current = None


class PresidentTablesParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tables = []
        self.in_target_table = False
        self.table_depth = 0
        self.rows = []
        self.row = None
        self.cell = None
        self.cell_tag = None

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        classes = attributes.get("class", "").split()
        if tag == "table" and "wikitable" in classes:
            self.in_target_table = True
            self.table_depth = 1
            self.rows = []
        elif self.in_target_table and tag == "table":
            self.table_depth += 1
        elif self.in_target_table and tag == "tr":
            self.row = []
        elif self.in_target_table and tag in {"td", "th"}:
            self.cell = []
            self.cell_tag = tag

    def handle_data(self, data):
        if self.cell is not None and data.strip():
            self.cell.append(data.strip())

    def handle_endtag(self, tag):
        if not self.in_target_table:
            return
        if tag in {"td", "th"} and self.cell is not None:
            self.row.append(" ".join(self.cell))
            self.cell = None
            self.cell_tag = None
        elif tag == "tr" and self.row is not None:
            if self.row:
                self.rows.append(self.row)
            self.row = None
        elif tag == "table":
            self.table_depth -= 1
            if self.table_depth == 0:
                if self.rows:
                    self.tables.append(self.rows)
                self.in_target_table = False


def scrape_bu_facts():
    url = "https://www.bu.edu/president/boston-university-facts-stats/"
    parser = BUFactsParser()
    parser.feed(fetch_page(url))
    facts = [
        item
        for item in parser.list_items
        if any(character.isdigit() for character in item)
        and not item.startswith(("One Silber Way", "617-", "©"))
    ]
    data = {
        "url": url,
        "headings": parser.headings,
        "stats": parser.stats,
        "facts_and_stats": facts,
    }
    save_json("bu_facts_stats.json", data)


def scrape_uci_datasets():
    url = "https://archive.ics.uci.edu/datasets"
    parser = DatasetLinksParser()
    parser.feed(fetch_page(url))
    save_json("uci_datasets.json", parser.datasets)


def scrape_presidents():
    url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
    parser = PresidentTablesParser()
    parser.feed(fetch_page(url))
    save_json("us_presidents.json", {"url": url, "tables": parser.tables})


def main():
    for scrape in (scrape_bu_facts, scrape_uci_datasets, scrape_presidents):
        try:
            scrape()
        except (URLError, TimeoutError) as error:
            print(f"Could not scrape {scrape.__name__}: {error}")

    print("API: a documented interface that lets programs exchange data or request services.")
    print("HTTP: the request-response protocol used by clients and servers; GET reads, POST creates, PUT updates, and DELETE removes resources.")


if __name__ == "__main__":
    main()
