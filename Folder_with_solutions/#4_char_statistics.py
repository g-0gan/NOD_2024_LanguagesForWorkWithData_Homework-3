from collections import Counter


def main():
    sentence = input("Введите предложение: ")  # Ввод предложения от пользователя
    statistics = Counter(sentence.lower())  # Подсчет статистики символов без учета регистра

    # Вывод статистики символов и их количества
    for char, count in statistics.items():
        print(f"{char} = {count}")


if __name__ == "__main__":
    main()
