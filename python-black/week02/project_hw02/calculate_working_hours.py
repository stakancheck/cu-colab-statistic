import holidays
from datetime import datetime, timedelta


# Создаем объекты для хранения национальных праздников России и Китая
ru_holidays = holidays.Russia(years=2024)
cn_holidays = holidays.China(years=2024)

# Выводим первые несколько праздников для проверки
print(f'Праздники в России: {list(ru_holidays.items())[:5]}')
print(f'Праздники в Китае: {list(cn_holidays.items())[:5]}')

moscow_start = datetime(2024, 1, 1, 9, 0)
moscow_end = datetime(2024, 1, 1, 18, 0)

china_start = moscow_start + timedelta(hours=5)
china_end = moscow_end + timedelta(hours=5)

moscow_lunch_start = moscow_start.replace(hour=13, minute=0)
moscow_lunch_end = moscow_start.replace(hour=14, minute=0)
china_lunch_start = china_start.replace(hour=13, minute=0)
china_lunch_end = china_start.replace(hour=14, minute=0)

start_time = max(moscow_start, china_start)
end_time = min(moscow_end, china_end)

# Учитываем обеденный перерыв
if start_time < moscow_lunch_end and end_time > moscow_lunch_start:
    working_hours = (end_time - start_time).seconds // 3600 - 1
else:
    working_hours = (end_time - start_time).seconds // 3600

print(f'Количество совместных рабочих часов в день: {working_hours}')

# Рассчитываем общее количество рабочих часов в году
working_days = 0
total_working_hours = 0

for day in range(1, 366):
    current_day = datetime(2024, 1, 1) + timedelta(days=day - 1)
    if current_day.weekday() < 5 and current_day not in ru_holidays and current_day not in cn_holidays:
        working_days += 1
        total_working_hours += working_hours

print(f'Общее количество рабочих часов в году: {total_working_hours}')
print(f'Количество рабочих дней в году: {working_days}')
