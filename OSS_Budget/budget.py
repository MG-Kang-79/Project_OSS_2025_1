import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount, payment_method):
        today = datetime.date.today().isoformat()
        
        if payment_method.lower() == "카드":
            original = amount
            amount = int(amount * 0.9)  # 정수로 반올림하여 할인
            print(f"카드 결제로 10% 할인 적용됨: {original}원 → {amount}원\n")
        
        expense = Expense(today, category, description, amount, payment_method)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")
        
        daily_total = sum(e.amount for e in self.expenses if e.date == today)
        if daily_total > 50000:
            print(f"경고: 오늘 하루 총 지출이 {daily_total}원입니다. 지출을 조절하세요.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")
