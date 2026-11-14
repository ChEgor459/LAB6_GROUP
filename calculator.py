def add(a, b):
    return a + b


def main():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    result = add(a, b)
    print(f"{a} + {b} = {result}")
    print('Суммирование выполнено!')

if __name__ == "__main__":
    main()