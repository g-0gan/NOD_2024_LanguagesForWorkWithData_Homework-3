def caesar_cipher(text, shift):
    result = ""  # Инициализация переменной для хранения результата
    for char in text:
        if char.isalpha():  # Проверка, является ли символ буквой
            shift_base = ord('А') if char.isupper() else ord('а')  # Определение базового значения для сдвига
            result += chr((ord(char) - shift_base + shift) % 32 + shift_base)  # Применение шифра
        else:
            result += char  # Оставляем знаки препинания без изменений
    return result


def main():
    text = input("Введите текст для шифрования: ")  # Получение текста от пользователя
    shift = int(input("Введите сдвиг: "))  # Получение сдвига для шифра
    encrypted = caesar_cipher(text, shift)  # Шифрование текста
    print(f"Зашифрованный текст: {encrypted}")

    decrypted = caesar_cipher(encrypted, -shift)  # Расшифрование текста
    print(f"Расшифрованный текст: {decrypted}")


if __name__ == "__main__":
    main()
