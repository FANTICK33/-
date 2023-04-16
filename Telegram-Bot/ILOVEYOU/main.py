import telebot
from telebot import types

bot = telebot.TeleBot("6281321685:AAEckaL94nNa1EOUWkdvB-otNxGqbd_lKDY")

# Привествие
@bot.message_handler(commands=['start'])
def profile(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('Узнать что хочет Филипп')
    markup.row(itembtn1)
    file = open('./Telegram-Bot/ILOVEYOU/two.jpg', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name} {message.from_user.last_name}", reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

# Обработчик кнопок привествия

def on_click(message):
    if message.text == 'Узнать что хочет Филипп':
        file2 = open('./Telegram-Bot/ILOVEYOU/Nastya.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup()
        itembtn1 = types.KeyboardButton('Согласна')
        markup.row(itembtn1)
        bot.send_photo(message.chat.id, file2, reply_markup=markup)

        bot.send_message(message.chat.id, 'Дорогая Настя, \nЯ хочу, чтобы ты знала, как важна ты для меня и как сильно я тебя люблю. Ты - моя незаменимая половинка, моя подруга, моя любовь, которую я искал всю свою жизнь. Я всегда нахожу уют и покой рядом с тобой. Я мечтаю проводить оставшуюся жизнь с тобой, и рядом с твоим сердцем я чувствую себя настоящим. \nТы всегда поддерживаешь меня, мотивируешь и вдохновляешь на большие свершения. Я верю, что все, что я когда-либо достигну или стану, будет лучше и сильнее благодаря тебе. \nЯ хочу, чтобы ты стала моей женой, и мы могли душевно связаться на всю жизнь. Я обещаю любить, заботиться и поддерживать тебя всегда и везде, и быть надежной и крепкой опорой для нашей семьи. \nЯ прошу тебя, Настя, стать моей женой и поделится со мной всеми уроками, радостями и трудностями, которые жизнь может нам предложить. Я хочу, чтобы мы образовали неразрывную связь, которая превратит нашу жизнь в великое и чудесное путешествие.\nС любовью,\nТвой будущий муж',reply_markup=markup)
        bot.register_next_step_handler(message, yes)

def yes(message):
    bot.send_message(message.chat.id, 'Напиши это мне.')



bot.infinity_polling()
