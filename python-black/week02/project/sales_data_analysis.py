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
    sales_data = [
        "Товар: Кофе; Количество: 10; Цена: 500 рублей".encode('utf-8'),  # UTF-8
        "Product: Laptop; Quantity: 5; Price: $1200".encode('ascii'),  # ASCII
        "Producto: Teléfono; Cantidad: 20; Precio: 300 EUR".encode('macroman')  # MacRoman
    ]

    for data in sales_data:
        try:
            standardized_data = standardize_encoding(data)
            print(f"Original: {data}")
            print(f"Standardized: {standardized_data.decode('utf-8')}\n")
        except ValueError as e:
            print(f"Ошибка: {e}")
