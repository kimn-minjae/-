print("1. 입력한 수식 계산  2. 두 수 사이의 합")
choice = int(input("선택하세요 : "))

if choice == 1:
    expr = input("*** 수식을 입력하세요 : ")
    result = eval(expr)
    print(expr, "결과는", result, "입니다.")

elif choice == 2:
    num1 = int(input("*** 첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("*** 두 번째 숫자를 입력하세요 : "))

    total = 0
    for i in range(num1, num2 + 1):
        total += i

    print(f"{num1}+...+{num2}는 {total}입니다.")