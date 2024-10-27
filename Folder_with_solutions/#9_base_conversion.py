def to_decimal(number, base):
    # Преобразование числа из произвольной системы счисления в десятичную
    return int(number, base)


def from_decimal(number, base):
    digits = "0123456789ABCDEF"  # Определение допустимых цифр для систем счисления
    if number == 0:
        return "0"  # Возвращение "0" для числа 0
    result = ""
    while number:
        result = digits[number % base] + result  # Постепенное построение результата
        number //= base  # Деление числа на основание системы
    return result


def main():
    source_base = int(input("Введите исходную систему счисления (2-16): "))  # Получение исходной системы
    target_base = int(input("Введите целевую систему счисления (2-16): "))  # Получение целевой системы
    number = input(f"Введите число в системе {source_base}: ")  # Ввод числа для преобразования

    if 2 <= source_base <= 16 and 2 <= target_base <= 16:
        decimal_number = to_decimal(number, source_base)  # Преобразование в десятичную систему
        converted_number = from_decimal(decimal_number, target_base)  # Преобразование в целевую систему
        print(f"Число {number} в системе {target_base}: {converted_number}")  # Вывод результата
    else:
        print("Ошибка: основание системы счисления должно быть от 2 до 16.")  # Вывод ошибки


if __name__ == "__main__":
    main()
