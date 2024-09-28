import holidays
from datetime import datetime, timedelta

# Национальные праздники России и Китая
ru_holidays = holidays.Russia(years=2024)
cn_holidays = holidays.China(years=2024)

# Время начала и окончания рабочего дня в Москве
moscow_start = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)
moscow_end = datetime.now().replace(hour=18, minute=0, second=0, microsecond=0)

# Время начала и окончания рабочего дня в Китае с учетом разницы в 5 часов с Москвой
china_start = moscow_start + timedelta(hours=5)
china_end = moscow_end + timedelta(hours=5)

# Время обеденного перерыва в Москве и Китае
moscow_lunch_start = moscow_start.replace(hour=13, minute=0)
moscow_lunch_end = moscow_start.replace(hour=14, minute=0)
china_lunch_start = china_start.replace(hour=13, minute=0)
china_lunch_end = china_start.replace(hour=14, minute=0)


# Рассчитываем пересекающиеся рабочие часы
def calculate_daily_working_hours():
    start_time = max(moscow_start, china_start)
    end_time = min(moscow_end, china_end)

    if start_time >= end_time:
        return 0

    working_hours = (end_time - start_time).seconds // 3600

    # Учитываем обеденные перерывы
    if moscow_lunch_start < end_time and moscow_lunch_end > start_time:
        working_hours -= 1
    if china_lunch_start < end_time and china_lunch_end > start_time:
        working_hours -= 1

    return working_hours


# Рассчитываем общее количество рабочих часов в году
total_working_hours = 0
start_of_year = datetime(2024, 1, 1)

for day in range(366):  # Високосный год
    current_day = start_of_year + timedelta(days=day)

    if current_day.weekday() < 5 and current_day not in ru_holidays and current_day not in cn_holidays:
        total_working_hours += calculate_daily_working_hours()

print(f'Общее количество рабочих часов в году: {total_working_hours}')
