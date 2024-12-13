# Семинарная работа 12 (⚫️ BLACK PYTHON)

## Preparing

### Шаг 1: Создание Google Service Account
1. Перейдите на [Google Cloud Console](https://console.cloud.google.com/).
2. Создайте новый проект или выберите существующий.
3. Перейдите в раздел **APIs & Services** -> **Credentials**.
4. Нажмите **Create Credentials** и выберите **Service Account**.
5. Укажите имя и описание для Service Account, затем нажмите **Create**.
6. На следующем шаге выберите роль **Editor** или **Owner** и нажмите **Continue**.
7. На последнем шаге нажмите **Done**.
8. В списке Service Accounts найдите созданный аккаунт и нажмите на его название.
9. Перейдите на вкладку **Keys** и нажмите **Add Key** -> **Create New Key**.
10. Выберите формат JSON и нажмите **Create**. Файл с ключом будет загружен на ваш компьютер.

### Шаг 2: Настройка проекта

1. Скопируйте файл с ключом в директорию проекта и переименуйте его в `google_service_account.json`.
2. Создайте таблицу в Google Sheets и **укажите права редактора для сервисного аккаунта**.
3. Создайте файл `.env` в корне проекта и добавьте в него следующие строки:

    ```env
    GOOGLE_SHEET_CREDENTIALS_JSON=./google_service_account.json
    SPREADSHEET_ID=your_spreadsheet_id
    WORKSHEET_NAME=YourWorksheetName
    ```

    - `GOOGLE_SHEET_CREDENTIALS_JSON` — путь к файлу с ключом сервисного аккаунта.
    - `SPREADSHEET_ID` — ID вашей таблицы Google Sheets. Его можно найти в URL таблицы.
    - `WORKSHEET_NAME` — название рабочего листа в таблице Google Sheets.


## Installation

### Запуск проекта
1. Создайте venv и установите зависимости:
    ```bash
    make setup
    ```

2. Запустите проект:
    ```bash
    make run
    ```
   
> [Пример таблицы](https://docs.google.com/spreadsheets/d/1pWDMXP5qigxhhHyBoEBEYOfRAj_m07dn1fecj_i0FHo/edit?usp=sharing), которая использовалась для тестирования.
