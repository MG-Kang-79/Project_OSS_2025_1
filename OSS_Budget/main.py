from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 종료")
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            time = input("지출 시간 (예: 13:45): ")
            place = input("지출 장소 (예: 영남대, 임당, 만촌 등): ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount, time, place)

        elif choice == "2":
            print("정렬 방식 선택:")
            print("1. 시간순")
            print("2. 금액순")
            sort_option = input("선택 > ")
            if sort_option == "1":
                budget.list_expenses(sort_by="time")
            elif sort_option == "2":
                budget.list_expenses(sort_by="amount")
            else:
                print("잘못된 선택입니다. 시간순으로 기본 출력합니다.\n")
                budget.list_expenses()

        elif choice == "3":
            budget.total_spent()

        elif choice == "4":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
