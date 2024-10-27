def is_palindrome(s):
    # Проверка, является ли строка палиндромом
    return s == s[::-1]


def main():
    user_input = input("Введите строку: ")  # Ввод строки от пользователя
    if is_palindrome(user_input):
        print("Это палиндром!")  # Вывод, если строка палиндром
    else:
        print("Это не палиндром.")  # Вывод, если строка не палиндром


if __name__ == "__main__":
    main()
