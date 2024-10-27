from functools import reduce


# Функция для вычисления НОД (наибольший общий делитель)
def gcd(a, b):
    while b:
        a, b = b, a % b  # Применение алгоритма Евклида для нахождения НОД
    return a


# Функция для вычисления НОК (наименьшее общее кратное)
def lcm(a, b):
    return abs(a * b) // gcd(a, b)  # Использование НОД для вычисления НОК


def main():
    # Ввод чисел пользователем и их преобразование в список
    numbers = [int(x) for x in input("Введите числа через пробел: ").split()]

    # Вычисление НОК для всех чисел в списке с использованием reduce
    result_lcm = reduce(lcm, numbers)
    # Вычисление НОД для всех чисел в списке с использованием reduce
    result_gcd = reduce(gcd, numbers)

    # Вывод результата на экран
    print(f"Наименьшее общее кратное (НОК): {result_lcm}")
    print(f"Наибольший общий делитель (НОД): {result_gcd}")


if __name__ == "__main__":
    main()
