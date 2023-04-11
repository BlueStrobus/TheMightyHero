import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def arcsin(x):
    return math.asin(x)

def arccos(x):
    return math.acos(x)

def arctan(x):
    return math.atan(x)

def log10(x):
    return math.log10(x)

def log(x):
    return math.log(x)

print("공학용 계산기를 실행합니다.")

while True:
    print("사칙연산을 선택하세요.")
    print("1. 더하기")
    print("2. 빼기")
    print("3. 곱하기")
    print("4. 나누기")
    print("5. 사인(sin)")
    print("6. 코사인(cos)")
    print("7. 탄젠트(tan)")
    print("8. 아크사인(arcsin)")
    print("9. 아크코사인(arccos)")
    print("10. 아크탄젠트(arctan)")
    print("11. 로그(log10)")
    print("12. 자연로그(log)")
    print("13. 종료")

    choice = input("선택 (1~13): ")

    if choice == '13':
        print("계산기를 종료합니다.")
        break

    elif choice in ('1', '2', '3', '4'):
        num1 = float(input("첫번째 숫자를 입력하세요: "))
        num2 = float(input("두번째 숫자를 입력하세요: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

    elif choice in ('5', '6', '7', '8', '9', '10', '11', '12'):
        num = float(input("숫자를 입력하세요: "))

        if choice == '5':
            print("sin(", num, ") =", sin(num))

        elif choice == '6':
            print("cos(", num, ") =", cos(num))

        elif choice == '7':
            print("tan(", num, ") =", tan(num))

        elif choice == '8':
            print("arcsin(", num, ") =", arcsin(num))

        elif choice == '9':
            print("arccos(", num, ") =", arccos(num))

        elif choice == '10':
            print("arctan(", num, ") =", arctan(num))

        elif choice == '11':
            print("log10(", num, ") =", log10(num
