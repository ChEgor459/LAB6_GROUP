def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль")
    return a / b


def main():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    result = add(a, b)
    print(f"{a} + {b} = {result}")
    print('Суммирование выполнено!')
    print("divide(6, 3) =", divide(6, 3))

    
if __name__ == "__main__":
    main()