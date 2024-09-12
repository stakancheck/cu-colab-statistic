#! /usr/bin/env python3
# Задача 8

password = "Qwerty123"

# Инициализация флагов
has_digit = False
has_upper = False
has_lower = False
is_long_enough = False

# Проверяем, что пароль содержит хотя бы одну цифру
for char in password:
    if char.isdigit():
        has_digit = True
        break

# Проверяем, что пароль содержит хотя бы одну заглавную букву
for char in password:
    if char.isupper():
        has_upper = True
        break

# Проверяем, что пароль содержит хотя бы одну строчную букву
for char in password:
    if char.islower():
        has_lower = True

# Проверяем, что пароль длиннее 8 символов
if len(password) >= 8:
    is_long_enough = True


# Проверяем, соответствует ли пароль всем требованиям
if has_digit and has_upper and has_lower and is_long_enough:
    print('Пароль принят')
else:
    print('Пароль не соответствует требованиям')
