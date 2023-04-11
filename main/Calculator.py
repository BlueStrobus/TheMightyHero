# 시작하세요
def calculator():
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    op = input("연산자를 입력하세요 (+, -, *, /): ")
    num2 = float(input("두 번째 숫자를 입력하세요: "))

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    else:
        print("잘못된 연산자입니다.")
        return

    print(f"{num1} {op} {num2} = {result}")
