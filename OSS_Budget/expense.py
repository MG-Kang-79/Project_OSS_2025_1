
class Expense:
    def __init__(self, date, time, place, category, description, amount):
        self.date = date
        self.time = time
        self.place = place
        self.category = category
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"[{self.date} {self.time}] {self.place} - {self.category} - {self.description}: {self.amount}원"