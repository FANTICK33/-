import telebot
from telebot import types
import webbrowser

bot = telebot.TeleBot("5734323883:AAG2ySfHjAFy1EFz7_WWIlCIQmGlFCPsn5I")

check_photo = False

# Привествие


@bot.message_handler(commands=['start'])
def profile(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('Перейти на сайт')
    itembtn2 = types.KeyboardButton('Работа с фото')
    itembtn3 = types.KeyboardButton('Узнать свое ID')
    markup.row(itembtn1)
    markup.row(itembtn2, itembtn3)
    file = open('./Photo/photo.webp', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    bot.send_message(
        message.chat.id, f"Привет, {message.from_user.first_name} {message.from_user.last_name}", reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

# Обработчик кнопок привествия


def on_click(message):
    global check_photo
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'Website is open')
        bot.register_next_step_handler(message, site)
    elif message.text == 'Узнать свое ID':
        bot.reply_to(message, f'ID: {message.from_user.id}')
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'Работа с фото':
        bot.send_message(message.chat.id, 'Вы можете отправить фотографию?')
        check_photo = True

# Обработка фото


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    global check_photo
    if check_photo:
        # Обрабатываем фото
        markup = types.InlineKeyboardMarkup()
        itembtn1 = types.InlineKeyboardButton(
            'Загрузить в инстаграм', url='https://www.instagram.com/')
        itembtn2 = types.InlineKeyboardButton(
            'Удалить фото', callback_data='delete')
        itembtn3 = types.InlineKeyboardButton(
            'Добавить текст', callback_data='edit')
        markup.row(itembtn1)
        markup.row(itembtn2, itembtn3)
        bot.reply_to(message, 'Какое красивое фото!', reply_markup=markup)
        # добавляем регистрацию on_click
        bot.register_next_step_handler(message, on_click)
        check_photo = False  # Сбрасываем флаг после обработки
    else:
        bot.reply_to(message, 'Вы не запрашивали работу с фото')

# Обработчик кнопок для фото


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id,
                           callback.message.message_id-1)
    elif callback.data == 'edit':
        bot.edit_message_text(
            'Текст добавлен', callback.message.chat.id, callback.message.message_id)


@bot.message_handler(commands=['site', 'website'])
def site(message):
    # Получить идентификатор чата пользователя
    chat_id = message.chat.id
    # Установить уникальный идентификатор сессии для пользователя на вашем веб-сайте
    session_id = generate_session_id(chat_id)
    # Сформировать URL-адрес веб-сайта с установленным идентификатором сессии
    site_url = "https://yoip.ru/{}".format(session_id)
    # Открыть веб-сайт в браузере пользователя
    webbrowser.open(site_url)

# Помощь


@bot.message_handler(commands=['help'])
def help_information(message):
    bot.send_message(
        message.chat.id, "<b>В этом боте идут работы, вам пока лучше выйти.</b>", parse_mode='html')


bot.infinity_polling()
