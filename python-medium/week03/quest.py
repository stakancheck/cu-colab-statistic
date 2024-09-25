import random


# 1. Создание команды и подготовка к экспедиции
def prepare_expedition():
    explorer_name = input("Введите имя исследователя: ")
    energy_level = 100
    equipment = []

    print("Вы отправляетесь в экспедицию по древним храмам. Ваша энергия:", energy_level)
    print("Выберите храм: 1 - Лесной храм, 2 - Огненный храм, 3 - Ледяной храм")
    temple_choice = int(input("Ваш выбор (1/2/3): "))

    if temple_choice == 1:
        energy_level -= 10
        equipment.append("Фонарь")
        print("Вы выбрали Лесной храм.")
    elif temple_choice == 2:
        energy_level -= 30
        equipment.append("Огнетушитель")
        print("Вы выбрали Огненный храм.")
    elif temple_choice == 3:
        energy_level -= 40
        equipment.append("Термоодежда")
        print("Вы выбрали Ледяной храм.")

    print(f"Начальный уровень энергии: {energy_level}")
    print(f"Экипировка: {equipment}")
    return explorer_name, energy_level, equipment


# 2. Навигация по запутанным коридорам храма
def navigate_temple(energy_level):
    steps = int(input("Введите количество шагов по коридорам храма: "))
    for step in range(steps):
        if random.random() < 0.5:
            energy_level -= 15
            print(f"Шаг {step + 1}: Попали в ловушку! Энергия уменьшена на 15.")
        else:
            energy_level -= 5
            print(f"Шаг {step + 1}: Всё спокойно. Энергия уменьшена на 5.")

        if energy_level <= 0:
            print("Исследователь потерял всю энергию и не может продолжить.")
            return 0

    return energy_level


# 3. Древняя головоломка стражей храма
def solve_puzzle(a, b, c, energy_level):
    result = a * b * c
    print(f"Решение головоломки: {result}")

    if result == 24:
        energy_level += 20
        print("Верное решение! Энергия восстановлена на 20.")
    else:
        energy_level -= 20
        print("Неверное решение. Энергия уменьшена на 20.")

    return energy_level


# 4. Поиск древних артефактов
def find_artifacts(artifacts, energy_level):
    for artifact in artifacts:
        if artifact == "Золотой кубок":
            energy_level += 30
            print("Найден Золотой кубок! Энергия восстановлена на 30.")
        elif artifact == "Сапфир скорости":
            print("Найден Сапфир скорости! Потеря энергии снижена.")
        elif artifact == "Карта храма":
            print("Найдена Карта храма! Открыты скрытые проходы.")
    return energy_level


# 5. Финальная битва с древним стражем
def battle_guardian(energy_level, guardian_strength):
    while energy_level > 0 and guardian_strength > 0:
        energy_level -= 10
        guardian_strength -= 15
        print(f"Во время боя: Энергия исследователя {energy_level}, Сила стража {guardian_strength}")

    if energy_level > 0:
        print("Исследователь победил стража!")
        return True
    else:
        print("Исследователь проиграл стражу.")
        return False


# 6. Загадка выхода из храма
def solve_exit_puzzle(stars):
    if stars == sorted(stars):
        print("Звезды расположены правильно! Выход открыт.")
        return True
    else:
        print("Звезды расположены неправильно. Выход закрыт.")
        return False


# 7. Возвращение домой
def return_home(artifacts):
    print("Поздравляем, исследователь успешно завершил экспедицию!")
    print("Найденные артефакты:", artifacts)


# Основная программа
def main():
    # Этап 1: Подготовка
    explorer_name, energy_level, equipment = prepare_expedition()

    # Этап 2: Навигация по коридорам
    energy_level = navigate_temple(energy_level)
    if energy_level <= 0:
        return

    # Этап 3: Головоломка стражей
    a, b, c = 2, 3, 4  # Пример
    energy_level = solve_puzzle(a, b, c, energy_level)
    if energy_level <= 0:
        return

    # Этап 4: Поиск артефактов
    artifacts = ["Золотой кубок", "Карта храма"]  # Пример
    energy_level = find_artifacts(artifacts, energy_level)

    # Этап 5: Битва со стражем
    guardian_strength = 60
    if not battle_guardian(energy_level, guardian_strength):
        return

    # Этап 6: Загадка выхода
    stars = [1, 2, 3, 4, 5]  # Пример
    if not solve_exit_puzzle(stars):
        return

    # Этап 7: Возвращение домой
    return_home(artifacts)


if __name__ == "__main__":
    main()
