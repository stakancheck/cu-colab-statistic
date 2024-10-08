### Квест: Путешествие по древним храмам

Ты — исследователь, который отправился в экспедицию для изучения древних храмов. По пути тебе предстоит решать задачи, использовать функции для принятия решений и взаимодействовать с различными препятствиями.

#### **Задачи квеста**

### 1. **Создание команды и подготовка к экспедиции**
- Создай переменные:
  - `explorer_name` для имени исследователя,
  - `energy_level` для уровня энергии исследователя (целое число, начальное значение — 100),
  - `equipment` для списка экипировки (пустой список).
  
- Перед началом экспедиции выбери один из трёх храмов (переменная `temple_choice`):
  - "Лесной храм" (умеренный климат, минимальные опасности),
  - "Огненный храм" (суровые условия, требуется защита),
  - "Ледяной храм" (экстремально холодный климат).

Каждый из храмов влияет на начальный уровень энергии и обязательное оборудование для исследователя:
- В "Лесном храме" уровень энергии уменьшается на 10, добавляется в экипировку фонарь.
- В "Огненном храме" уровень энергии уменьшается на 30, добавляется в экипировку огнетушитель.
- В "Ледяном храме" уровень энергии уменьшается на 40, добавляется в экипировку термоодежда.

### 2. **Навигация по запутанным коридорам храма**

- Используй переменную `steps`, чтобы задать количество шагов исследователя в коридорах (целое число, например, 10).
  
- При каждом шаге, энергия исследователя уменьшается. Если случается случайная ловушка (50% шанс), энергия уменьшается на 15, в ином случае — на 5. Для случайных событий используй модуль `random` и цикл `for`.


### 3. **Древняя головоломка стражей храма**

- В одном из залов исследователя встречают стражи. Чтобы пройти дальше, нужно решить древнюю математическую задачу:
  - Напиши функцию `solve_puzzle(a, b, c)`, которая принимает три числа и возвращает произведение этих чисел. Используй эту функцию, чтобы решить древнюю математическую головоломку.
  - Если результат равен 24, исследователь получает бонус в виде восстановления энергии на 20 единиц. Если ответ неверный, энергия уменьшается на 20.

### 4. **Поиск древних артефактов**

- В храме исследователь должен найти три артефакта. Для этого Напиши функцию `find_artifacts(artifacts)`, которая принимает список артефактов, найденных исследователем. Артефакты могут быть:
  - "Золотой кубок" — восстанавливает 30 единиц энергии,
  - "Сапфир скорости" — снижает потерю энергии при следующем этапе,
  - "Карта храма" — открывает скрытые проходы.

Используй условные операторы, чтобы определить, какой артефакт был найден и какой бонус получит исследователь.

### 5. **Финальная битва с древним стражем**

- В конце пути исследователь встречает стража, который блокирует выход из храма.
  
- Напиши функцию `battle_guardian(energy_level, guardian_strength)`, которая принимает два аргумента: текущее количество энергии исследователя и силу стража (например, 60).
  
- Во время битвы исследователь теряет по 10 единиц энергии за каждый ход, а страж — по 15. Битва продолжается до тех пор, пока энергия или сила не станет равна нулю.

- Если энергия исследователя остаётся положительной, он побеждает, иначе — проигрывает и вынужден искать другой путь домой.

Используй циклы для симуляции боя, где каждый ход отнимает энергию как у стража, так и у исследователя, пока один из них не победит.

### 6. **Загадка выхода из храма**

- Последнее препятствие перед выходом из храма — древняя загадка.
- Напиши функцию `solve_exit_puzzle(stars)`, которая принимает список чисел `stars` и проверяет, отсортирован ли он по возрастанию.

- Если список отсортирован, функция возвращает "Звезды расположены правильно! Выход открыт.", в противном случае — "Звезды расположены неправильно. Выход закрыт."

### 7. **Возвращение домой**

- Если исследователь преодолевает все препятствия и решает головоломку выхода, его ждёт триумфальное возвращение с артефактами и сокровищами.

Напиши финальную функцию `return_home(artifacts)`, которая принимает список найденных артефактов и выводит сообщение: "Поздравляем, исследователь успешно завершил экспедицию!" и список найденных артефактов.
