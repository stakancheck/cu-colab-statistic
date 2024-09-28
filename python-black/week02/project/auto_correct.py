import chardet

corrections = {
    "превет": "привет",
    "спсибо": "спасибо",
    "кагда": "когда",
    "сегодна": "сегодня",
    "оформлние": "оформление",
    "обьём": "объём"
}


def standardize_encoding(text):
    detected_encoding = chardet.detect(text)['encoding']
    if detected_encoding is None:
        raise ValueError("Не удалось определить кодировку текста")

    if detected_encoding.lower() != 'utf-8':
        text = text.decode(detected_encoding).encode('utf-8')

    return text


def auto_correct(text):
    words = text.decode('utf-8').lower()
    for correction in corrections:
        words = words.replace(correction, corrections[correction])

    # Case correction
    words = '. '.join([word.strip().capitalize() for word in words.split('')])
    words = '? '.join([word.strip().capitalize() for word in words.split('?')])
    words = '! '.join([word.strip().capitalize() for word in words.split('!')])
    return words.encode('utf-8')


if __name__ == "__main__":
    # Примеры строк для тестирования
    test_strings = [
        "Дорогой клиент, преветствуем вас на борту!".encode('utf-8'),
        "Спсибо за оформлние заказа, кагда ваш заказ будет готов, мы сообщим вам.".encode('utf-8'),
        "Добрый день! Напоминаем, что ваше время для визита в офис назначено на сегодна.".encode('utf-8'),
        "Отчёт по продажам за квартал: продажа возросла на 15%. Общий обьём продаж составил 500 единиц.".encode('utf-8')
    ]

    for text in test_strings:
        try:
            standardized_text = standardize_encoding(text)
            corrected_text = auto_correct(standardized_text)
            print(f"Original: {text.decode('utf-8')}")
            print(f"Corrected: {corrected_text.decode('utf-8')}\n")
        except ValueError as e:
            print(f"Ошибка: {e}")
