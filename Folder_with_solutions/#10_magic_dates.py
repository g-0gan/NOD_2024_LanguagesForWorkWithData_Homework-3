def is_magic_date(day, month, year):
    # Проверка, является ли дата магической
    return day * month == year % 100


def main():
    print("Магические даты XX века:")
    for year in range(1900, 2000):  # Перебор всех лет 20 века
        for month in range(1, 13):  # Перебор всех месяцев
            for day in range(1, 32):  # Перебор всех дней
                if is_magic_date(day, month, year):
                    print(f"{day:02}.{month:02}.{year}")  # Вывод магической даты в формате ДД.ММ.ГГГГ


if __name__ == "__main__":
    main()
