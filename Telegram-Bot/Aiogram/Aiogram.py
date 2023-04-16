from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
bot = Bot("5734323883:AAG2ySfHjAFy1EFz7_WWIlCIQmGlFCPsn5I")
dp = Dispatcher(bot)


# Привествие
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Открыть веб страницу', web_app = WebAppInfo( url = 'https://github.com/FANTICK33/Python/edit/main/Telegram-Bot/Aiogram/index.html')))
    await message.reply('Привет, мой друг', reply_markup = markup)

    # file = open('/some.png', ' rb') # Работа с файлом
    # await message.answer_photo(file)



@dp.message_handler(commands = ['reply'])
async def reply(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Site'))
    markup.add(types.KeyboardButton('Website'))
    await message.answer('Hello', reply_markup = markup)


executor.start_polling(dp)
