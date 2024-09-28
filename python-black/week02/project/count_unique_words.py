import chardet


def standardize_encoding(text):
    detected_encoding = chardet.detect(text)['encoding']
    if detected_encoding is None:
        raise ValueError("Не удалось определить кодировку текста")

    if detected_encoding.lower() != 'utf-8':
        text = text.decode(detected_encoding).encode('utf-8')

    return text


def count_unique_words(text):
    words = text.decode('utf-8').split()
    unique_words = set(words)
    return unique_words, len(unique_words)


if __name__ == "__main__":
    # Примеры строк для тестисования
    test_strings = [
        "Отличное обслуживание и быстрый сервис. Продукт очень понравился!".encode('utf-8'),
        "The product was delivered on time and met all expectations. Highly recommended!".encode('ascii'),
        "El servicio al cliente fue excelente, y el producto llegó en perfectas condiciones.".encode('utf-8'),
        "Продажи в январе выросли на 15%. Объём продаж составил 200 единиц.".encode('utf-8'),
        "Sales in January increased by 15%. The total sales volume was 200 units.".encode('ascii'),
        "Der Kundenservice war ausgezeichnet, und das Produkt wurde pünktlich geliefert.".encode('utf-8')
    ]

    for text in test_strings:
        try:
            standardized_text = standardize_encoding(text)
            unique_words, count = count_unique_words(standardized_text)
            print("Слова:")
            for word in unique_words:
                print(word)
            print(f"Количество уникальных слов: {count}\n")
        except ValueError as e:
            print(f"Ошибка: {e}")
