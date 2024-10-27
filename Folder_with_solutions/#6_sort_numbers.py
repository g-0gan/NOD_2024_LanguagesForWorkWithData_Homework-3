def sort_numbers(*args):
    # Сортировка отрицательных чисел по убыванию
    negatives = sorted([num for num in args if num < 0], reverse=True)
    # Сортировка неотрицательных чисел по возрастанию
    non_negatives = sorted([num for num in args if num >= 0])
    return negatives, non_negatives


def main():
    numbers = list(map(int, input("Введите числа через пробел: ").split()))  # Получение списка чисел
    negatives, non_negatives = sort_numbers(*numbers)  # Вызов функции сортировки

    # Вывод отсортированных списков
    print(f"Отрицательные (по убыванию): {negatives}")
    print(f"Неотрицательные (по возрастанию): {non_negatives}")


if __name__ == "__main__":
    main()
