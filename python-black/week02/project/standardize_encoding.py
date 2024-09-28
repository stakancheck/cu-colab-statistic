import chardet


def standardize_encoding(text):
    detected_encoding = chardet.detect(text)['encoding']
    if detected_encoding is None:
        raise ValueError("Не удалось определить кодировку текста")

    if detected_encoding.lower() != 'utf-8':
        text = text.decode(detected_encoding).encode('utf-8')

    return text


if __name__ == "__main__":
    # Примеры строк для тестирования
    test_strings = [
        "Bonjour, comment ça va?".encode('iso-8859-1'),  # ISO-8859-1
        "Привет! Когда мы можем встретиться?".encode('utf-8'),  # UTF-8
        "Спасибо за вашу помощь.".encode('utf-8'),  # UTF-8
        "Auf Wiedersehen!".encode('ascii')  # ASCII
    ]

    for text in test_strings:
        try:
            standardized_text = standardize_encoding(text)
            print(f"Original: {text}")
            print(f"Standardized: {standardized_text.decode('utf-8')}\n")
        except ValueError as e:
            print(f"Ошибка: {e}")
