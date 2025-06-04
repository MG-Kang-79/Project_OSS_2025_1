import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, person, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, person, category, description, amount)
        self.expenses.append(expense)
        print(f"지출이 추가되었습니다: {person} - {description} ({amount}원)\n")

    def list_expenses(self, target="all"):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return

        filtered = (
            self.expenses if target == "all"
            else [e for e in self.expenses if e.person == target]
        )

        if not filtered:
            print(f"{target}의 지출 내역이 없습니다.\n")
            return

        print(f"\n[지출 목록 - {target if target != 'all' else '전체'}]")
        for idx, e in enumerate(filtered, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")
