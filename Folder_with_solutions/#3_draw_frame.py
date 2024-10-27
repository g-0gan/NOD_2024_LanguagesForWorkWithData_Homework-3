def draw_frame(text, symbol):
    length = len(text) + 4  # Вычисление длины рамки
    print(symbol * length)  # Вывод верхней границы рамки
    print(f"{symbol} {text} {symbol}")  # Вывод текста с рамкой
    print(symbol * length)  # Вывод нижней границы рамки


def main():
    text = input("Введите текст: ")  # Получение текста от пользователя
    symbol = input("Введите символ для рамки: ")  # Получение символа для рамки
    draw_frame(text, symbol)  # Вызов функции для рисования рамки


if __name__ == "__main__":
    main()
