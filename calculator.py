def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль")
    return a / b


def multiply(a, b):
    return a * b


def subtract(a, b):
    return a - b



def main():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    result = add(a, b)
    print(f"{a} + {b} = {result}")
    print('Суммирование выполнено!')
    print("divide(6, 3) =", divide(6, 3))
    print("multiply(2, 3) =", multiply(2, 3))
    print("subtract(5, 3) =", subtract(5, 3))

    
if __name__ == "__main__":
    main()