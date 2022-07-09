from telebot import types
from settnigs import bot
from services import my_timer, my_alarm


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Будильник")
    btn2 = types.KeyboardButton("Таймер")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Я твой личный органайзер. Выбери что необходимо сделать".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Таймер':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1 минута")
        btn2 = types.KeyboardButton("2 минуты")
        btn3 = types.KeyboardButton("5 минут")
        btn4 = types.KeyboardButton("10 минут")
        btn5 = types.KeyboardButton("30 минут")
        btn6 = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.chat.id, text="Выбери время таймера, либо введи вручную(в минутах)".format(message.from_user), reply_markup=markup)
    if message.text == '1 минута':
        my_timer(message, 1, 0)
    if message.text == '2 минуты':
        my_timer(message, 2, 0)
    if message.text == '5 минут':
        my_timer(message, 5, 0)
    if message.text == '10 минут':
        my_timer(message, 10, 0)
    if message.text == '30 минут':
        my_timer(message, 30, 0)
    if message.text == 'Назад':
        start(message)
    if message.text == "Будильник":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("06:00")
        btn2 = types.KeyboardButton("07:00")
        btn3 = types.KeyboardButton("08:00")
        btn4 = types.KeyboardButton("09:00")
        btn5 = types.KeyboardButton("14:00")
        btn6 = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.chat.id,
                         text="Выбери время будильника, либо введи вручную(часы, минуты)".format(message.from_user),
                         reply_markup=markup)
    if message.text == '06:00':
        my_alarm(message, 0, 6)
    if message.text == '07:00':
        my_alarm(message, 0, 7)
    if message.text == '08:00':
        my_alarm(message, 0, 8)
    if message.text == '09:00':
        my_alarm(message, 0, 9)
    if message.text == '14:00':
        my_alarm(message, 0, 14)
    if message.text == 'Назад':
        start(message)


bot.polling(none_stop=True, interval=0)



