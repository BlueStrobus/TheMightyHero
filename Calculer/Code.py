# 간단한 계산기 코드

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("사칙연산을 선택하세요.")
print("1. 더하기")
print("2. 빼기")
print("3. 곱하기")
print("4. 나누기")
// 수정할거
while True:
    choice = input("선택 (1/2/3/4): ")
    
    if choice in ('1', '2', '3', '4'):
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
        break
    
    else:
        print("잘못된 입력입니다. 다시 선택하세요.")
        print("잘못된 입력입니다. 다시 선택하세요.")
