
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Создайте объект credentials из файла client_secret.json
creds = Credentials.from_authorized_user_file('client_secret.json', scopes=['https://www.googleapis.com/auth/spreadsheets'])

# Создайте объект sheets API
service = build('1uClkxjKnIHsnrjAp9NKGjirv8v24uQItZ1v7z8DE8dk', 'v4', credentials=creds)

# Задайте ID таблицы
spreadsheet_id = '<your_spreadsheet_id>'

# Получите список листов в таблице
sheets = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()['1uClkxjKnIHsnrjAp9NKGjirv8v24uQItZ1v7z8DE8dk']
sheet_names = [sheet['properties']['title'] for sheet in sheets]

# Выведите список названий листов
print("List of sheets:")
for name in sheet_names:
    print(name)

# Выберите лист
sheet_name = input("Enter sheet name to edit: ")
sheet = None
for s in sheets:
    if s['properties']['title'] == sheet_name:
        sheet = s
        break

if not sheet:
    print(f"Sheet {sheet_name} not found")
    exit

range = sheet['properties']['title'] + '!A1:Z1000'

# Получите данные из выбранной таблицы
try:
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range).execute()
    values = result.get('values', [])
    # Выведите данные на экран
    for row in values:
        print('\t'.join(row))
except HttpError as error:
    print(f"An error occurred: {error}")

# Редактирование ячеек таблицы
update_range = sheet['properties']['title'] + '!A2:A2'

value_input_option = 'RAW'

body = {
    'values': [['test']]
}

try:
    response = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=update_range,
        valueInputOption=value_input_option,
        body=body).execute()
    print(f"Updated {response['updatedCells']} cells")
except HttpError as error:
    print(f"An error occurred: {error}")
