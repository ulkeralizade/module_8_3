def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    if not isinstance(numbers, (list, tuple)):
        raise TypeError("В numbers записан некорректный тип данных")

    for number in numbers:
        try:
            if not isinstance(number, int):
                print(f"Некорректный тип данных для подсчёта суммы - {number}")
                incorrect_data += 1
            else:
                result += number
        except TypeError as e:
            print(f"Ошибка: {e}")
            incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    if isinstance(numbers, str):
        numbers = list(numbers)

    try:
        total, errors = personal_sum(numbers)
        if len(numbers) == 0:
            return 0
        return total / len(numbers)
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


# Пример выполнения программы:

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

