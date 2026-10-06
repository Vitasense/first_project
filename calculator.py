def calculate(a, b, operation):
    """
    Выполняет арифметическую операцию над двумя числами.

    :param a: первое число
    :param b: второе число
    :param operation: строка с операцией: '+', '-', '*', '/'
    :return: результат вычисления
    """
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            raise ZeroDivisionError('Деление на ноль невозможно')
        return a / b
    else:
        raise ValueError(f'Неизвестная операция: {operation}')


def main():
    print('Простой калькулятор')
    print('Доступные операции: +, -, *, /')
    print('Для выхода введите "выход"\n')

    while True:
        user_input = input('Введите выражение (например: 5 + 3): ')

        if user_input.strip().lower() == 'выход':
            print('Работа завершена.')
            break

        parts = user_input.split()
        if len(parts) != 3:
            print('Ошибка: введите выражение в формате "число операция число"\n')
            continue

        num1_str, operation, num2_str = parts

        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
            result = calculate(num1, num2, operation)
            print(f'Результат: {result}\n')
        except ValueError as error:
            print(f'Ошибка: {error}\n')
        except ZeroDivisionError as error:
            print(f'Ошибка: {error}\n')


if __name__ == '__main__':
    main()