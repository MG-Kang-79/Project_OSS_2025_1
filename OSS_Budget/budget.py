import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount, time, place):
        today = datetime.date.today().isoformat()
        expense = Expense(today, time, place, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self, sort_by="time"):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return

        print(f"\n[지출 목록 - 정렬 기준: {'시간' if sort_by == 'time' else '금액'}]")

        if sort_by == "time":
            sorted_expenses = sorted(self.expenses, key=lambda e: (e.date, e.time))
        elif sort_by == "amount":
            sorted_expenses = sorted(self.expenses, key=lambda e: e.amount, reverse=True)
        else:
            sorted_expenses = self.expenses

        for idx, e in enumerate(sorted_expenses, 1):
            print(f"{idx}. [{e.date} {e.time}] {e.place} | {e.category} | {e.description} | {e.amount}원")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")


