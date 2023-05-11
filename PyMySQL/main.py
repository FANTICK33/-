import gspread
from oauth2client.service_account import ServiceAccountCredentials
import getpass

# Функция для авторизации пользователя
def authorize_user():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    return client

# Авторизуем пользователя
client = authorize_user()

# Получаем список всех таблиц
sheets = client.openall()

# Выводим список таблиц на экран
for sheet in sheets:
    print(sheet.title)
