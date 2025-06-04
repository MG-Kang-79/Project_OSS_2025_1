from budget import Budget

def main():
    budget = Budget()
    family_members = ["부", "모", "첫째", "둘째"]

    while True:
        print("==== 가족 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 내역 보기")
        print("3. 총 지출 보기")
        print("4. 종료")
        
        choice = input("선택 > ")

        if choice == "1":
            print("가족 구성원을 선택하세요:")
            print("0. 전체 구성원")  # ✅ 추가됨
            for idx, name in enumerate(family_members, 1):
                print(f"{idx}. {name}")
            try:
                idx = int(input("선택 > "))
                if idx == 0:
                    person = "all"  # ✅ 추가됨
                else:
                    person = family_members[idx - 1]
            except (ValueError, IndexError):
                print("잘못된 선택입니다.\n")
                continue

            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue

            # ✅ 공동 지출 기능 추가
            if person == "all":
                split_amount = amount // len(family_members)
                for member in family_members:
                    budget.add_expense(member, category, f"[공동] {description}", split_amount)
                print(f"{amount}원을 {len(family_members)}명에게 분할하여 등록했습니다.\n")  # ✅ 안내 메시지
            else:
                budget.add_expense(person, category, description, amount)

        elif choice == "2":
            print("누구의 지출을 확인할까요?")
            print("0. 전체")
            for idx, name in enumerate(family_members, 1):
                print(f"{idx}. {name}")
            try:
                idx = int(input("선택 > "))
                target = "all" if idx == 0 else family_members[idx - 1]
            except (ValueError, IndexError):
                print("잘못된 선택입니다.\n")
                continue

            budget.list_expenses(target)

        elif choice == "3":
            budget.total_spent()

        elif choice == "4":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
