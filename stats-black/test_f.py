import requests
import logging

# Настройка логгера
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


# Функция для получения всех пользователей из Bitrix24
def fetch_all_users_from_bitrix24():
    all_users = []
    url = 'https://dodo.bitrix24.ru/rest/167193/l1g6cizuvamq7ki2/user.get.json'
    has_more_users = True
    start = 0

    while has_more_users:
        params = {
            "start": start
        }

        response = requests.get(url, params=params)
        print(response)
        data = response.json()

        if 'result' in data:
            all_users.extend(data['result'])
            if 'next' in data:
                start = data['next']
            else:
                has_more_users = False
        else:
            has_more_users = False

    return all_users


# Функция для форматирования номера телефона
def format_number(number):
    formatted_number = ''.join(filter(str.isdigit, number))
    return formatted_number


# Основная функция для получения пользователей и их вывода в лог
def main():
    user_list = fetch_all_users_from_bitrix24()

    print(user_list)
    formatted_users = []
    for user in user_list:
        if user.get('ACTIVE'):
            mobile_phone = format_number(user.get('PERSONAL_MOBILE', '')) if user.get('PERSONAL_MOBILE') else ''
            formatted_users.append([
                user.get('ID'),
                user.get('NAME'),
                user.get('LAST_NAME'),
                user.get('EMAIL'),
                user.get('PERSONAL_PHONE'),
                mobile_phone,
                user.get('ACTIVE'),
                user.get('UF_USR_1685967004218'),
                user.get('UF_USR_1667290893115')
            ])

    # Выводим массив в лог
    for formatted_user in formatted_users:
        print(formatted_user)
        logger.info(formatted_user)


# Запуск основной функции
if __name__ == '__main__':
    main()
