
def convert_to_win1251(text):
    try:
        converted_text = text.encode('utf-8').decode('utf-8').encode('windows-1251')
        return converted_text
    except UnicodeEncodeError as e:
        print(f"Ошибка перекодировки: {e}")
        return None

if __name__ == "__main__":
    # Примеры строк для тестирования
    test_strings = [
        "Этот документ требует согласования CEO.",  # UTF-8
        "Документ должен быть сохранён.",  # UTF-8
        "Здесь используется кодировка Windows-1251."  # UTF-8
    ]

    for text in test_strings:
        converted_text = convert_to_win1251(text)
        if converted_text:
            print(f"Original: {text}")
            print(f"Converted: {converted_text.decode('windows-1251')}\n")
