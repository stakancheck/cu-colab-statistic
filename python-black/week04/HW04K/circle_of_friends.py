import string

def caesar_cipher(text, shift):
    encrypted_text = []
    for char in text:
        if char in string.ascii_letters:
            offset = 65 if char.isupper() else 97
            encrypted_text.append(chr((ord(char) - offset + shift) % 26 + offset))
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

if __name__ == "__main__":
    friends = {}
    num_friends = int(input('Сколько друзей в сети? '))
    initial_shift = int(input('Введите начальный сдвиг для шифра Цезаря: '))

    for _ in range(num_friends):
        name = input('Имя союзника: ')
        text = input(f'Сообщение для {name}: ')
        shift = initial_shift
        encrypted_message = []
        for line in text.split('\n'):
            encrypted_message.append(caesar_cipher(line, shift))
            shift += 1
        friends[name] = '\n'.join(encrypted_message)

    for name, message in friends.items():
        print(f'Зашифрованное сообщение для {name}: {message}')
