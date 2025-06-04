
class Expense:
    def __init__(self, date, person, category, description, amount):
        self.date = date
        self.person = person
        self.category = category
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"[{self.date}] {self.person} | {self.category} | {self.description}: {self.amount}원"