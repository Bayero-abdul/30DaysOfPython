from collections import Counter
from statistics import median, pstdev, pvariance


class Statistics:
    def __init__(self, data):
        self.data = list(data)

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return self.sum() / self.count()

    def median(self):
        return median(self.data)

    def mode(self):
        value, count = Counter(self.data).most_common(1)[0]
        return {"mode": value, "count": count}

    def var(self):
        return pvariance(self.data)

    def std(self):
        return pstdev(self.data)

    def percentile(self, percent):
        ordered_data = sorted(self.data)
        index = max(0, (len(ordered_data) * percent + 99) // 100 - 1)
        return ordered_data[min(index, len(ordered_data) - 1)]

    def freq_dist(self):
        frequencies = Counter(self.data)
        return sorted(
            ((count / self.count() * 100, value) for value, count in frequencies.items()),
            reverse=True,
        )

    def describe(self):
        mode = self.mode()
        return (
            f"Count: {self.count()}\n"
            f"Sum: {self.sum()}\n"
            f"Min: {self.min()}\n"
            f"Max: {self.max()}\n"
            f"Range: {self.range()}\n"
            f"Mean: {self.mean():g}\n"
            f"Median: {self.median():g}\n"
            f"Mode: ({mode['mode']}, {mode['count']})\n"
            f"Variance: {self.var():.1f}\n"
            f"Standard Deviation: {self.std():.1f}\n"
            f"Frequency Distribution: {self.freq_dist()}"
        )


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print(data.describe())
print("50th percentile:", data.percentile(50))


class PersonAccount:
    def __init__(self, firstname, lastname, incomes=None, expenses=None):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = set() if incomes is None else set(incomes)
        self.expenses = set() if expenses is None else set(expenses)

    def total_income(self):
        return sum(amount for amount, _ in self.incomes)

    def total_expense(self):
        return sum(amount for amount, _ in self.expenses)

    def account_info(self):
        return f"{self.firstname} {self.lastname}: income {self.total_income()}, expenses {self.total_expense()}"

    def add_income(self, amount, description):
        self.incomes.add((amount, description))

    def add_expense(self, amount, description):
        self.expenses.add((amount, description))

    def account_balance(self):
        return self.total_income() - self.total_expense()


account = PersonAccount("Alex", "Morgan")
account.add_income(3000, "salary")
account.add_income(250, "freelance")
account.add_expense(1200, "rent")
account.add_expense(300, "groceries")
print(account.account_info())
print("Balance:", account.account_balance())
