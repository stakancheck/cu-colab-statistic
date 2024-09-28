import chardet

def detect_encoding(text):
    result = chardet.detect(text)
    return result['encoding']

if __name__ == "__main__":
    # Примеры строк для тестирования
    test_strings = [
        b"Hello, how are you?",  # ASCII
        "Привет, как дела?".encode('utf-8'),  # UTF-8
        "こんにちは、元気ですか？".encode('utf-8'),  # UTF-8
        "¡Hola! ¿Cómo estás?".encode('utf-8')  # UTF-8
    ]

    for text in test_strings:
        encoding = detect_encoding(text)
        print(f"Detected encoding: {encoding}")