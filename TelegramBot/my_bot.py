from telebot import types
from settnigs import bot
from services import my_timer, my_alarm, time_calculation, my_alert

bd_note = []
bd_alert = []


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_1 = types.KeyboardButton("Alarm")
    btn_2 = types.KeyboardButton("Timer")
    btn_3 = types.KeyboardButton("Notes")
    btn_4 = types.KeyboardButton("Alert")
    markup.add(btn_1, btn_2, btn_3, btn_4)
    bot.send_message(message.chat.id, text="I am your personal organizer. Choose what needs to be done.".format(message.from_user), reply_markup=markup)


@bot.message_handler(commands=['next_start'])
def next_star(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_1 = types.KeyboardButton("Alarm")
    btn_2 = types.KeyboardButton("Timer")
    btn_3 = types.KeyboardButton("Notes")
    btn_4 = types.KeyboardButton("Alert")
    markup.add(btn_1, btn_2, btn_3, btn_4)
    bot.send_message(message.chat.id,
                     text="Main menu".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_timer(message):
    if message.text == 'Timer':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton("1 minute")
        btn_2 = types.KeyboardButton("2 minute")
        btn_3 = types.KeyboardButton("5 minute")
        btn_4 = types.KeyboardButton("10 minute")
        btn_5 = types.KeyboardButton("30 minute")
        btn_6 = types.KeyboardButton("Main menu")
        markup.add(btn_1, btn_2, btn_3, btn_4, btn_5, btn_6)
        bot.send_message(message.chat.id, text="Select the timer time, or enter manually (in minutes)"
                         .format(message.from_user), reply_markup=markup)
    input_text = message.text.split(':')
    if len(input_text) == 1 and input_text[0].isdigit():
        add_hour, add_minutes = time_calculation(int(input_text[0]))
        print(add_hour, add_minutes)
        my_timer(message, add_minutes, add_hour)
    if message.text == '1 minute':
        my_timer(message, 1, 0)
    if message.text == '2 minute':
        my_timer(message, 2, 0)
    if message.text == '5 minute':
        my_timer(message, 5, 0)
    if message.text == '10 minute':
        my_timer(message, 10, 0)
    if message.text == '30 minute':
        my_timer(message, 30, 0)
    if message.text == 'Main menu':
        next_star(message)
    if message.text == "Alarm":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton("06:00")
        btn_2 = types.KeyboardButton("07:00")
        btn_3 = types.KeyboardButton("08:00")
        btn_4 = types.KeyboardButton("09:00")
        btn_5 = types.KeyboardButton("14:00")
        btn_6 = types.KeyboardButton("Main menu")
        markup.add(btn_1, btn_2, btn_3, btn_4, btn_5, btn_6)
        bot.send_message(message.chat.id,
                         text="Choose the alarm time, or enter manually (hours, minutes)".format(message.from_user),
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
    if message.text == "Notes":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton("Add note")
        btn_2 = types.KeyboardButton("Edit note")
        btn_3 = types.KeyboardButton("Show notes")
        btn_4 = types.KeyboardButton("Delete note")
        btn_5 = types.KeyboardButton("Main menu")
        markup.add(btn_1, btn_2, btn_3, btn_4, btn_5)
        bot.send_message(message.chat.id,
                         text="Choose your course of action".format(message.from_user),
                         reply_markup=markup)
    if message.text == "Add note":
        bot.send_message(message.from_user.id, 'To add a note, type: add_(note content)')
    if message.text.split('_')[0].lower() == 'add':
        bd_note.append(message.text[4:])
        bot.send_message(message.from_user.id, f'Added {len(bd_note)} note')
    if message.text == "Show notes":
        for one_bd in bd_note:
            bot.send_message(message.from_user.id, f'{bd_note.index(one_bd) + 1}. {one_bd}')
    if message.text == "Delete note":
        bot.send_message(message.from_user.id, 'To delete a note write(Del_number note)')
    if message.text.split('_')[0].lower() == 'del':
        if message.text.split('_')[1].isdecimal() and int(message.text.split('_')[1]) <= len(bd_note) and \
                int(message.text.split('_')[1]) != 0:
            stung_note_index = int(message.text.split('_')[1])
            bd_note.pop(stung_note_index - 1)
            bot.send_message(message.from_user.id, f'Note number {stung_note_index} deleted')
        else:
            bot.send_message(message.from_user.id, 'Enter the correct value!!!')
    if message.text == "Edit note":
        bot.send_message(message.from_user.id, 'For note names, type(edi_(note number)_(edited note text)))')
    if message.text.split('_')[0].lower() == 'edi':
        if message.text.split('_')[1].isdecimal() and int(message.text.split('_')[1]) <= len(bd_note) and \
                int(message.text.split('_')[1]) != 0:
            stung_note_index = int(message.text.split('_')[1])
            bd_note[int(message.text.split('_')[1]) - 1] = (message.text.split('_')[2])
            bot.send_message(message.from_user.id, f'Note number {stung_note_index} changed')
        else:
            bot.send_message(message.from_user.id, 'Enter the correct value!!!')
    if message.text == "Alert":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton("Add alert")
        btn_2 = types.KeyboardButton("Show alert")
        btn_3 = types.KeyboardButton("Delete alert")
        btn_4 = types.KeyboardButton("Main menu")
        markup.add(btn_1, btn_2, btn_3, btn_4)
        bot.send_message(message.chat.id,
                         text="Choose your course of action".format(message.from_user),
                         reply_markup=markup)
    if message.text == "Add alert":
        bot.send_message(message.from_user.id, 'To add a note, type: aadd_(time_alert(hour:min)_(text alert))')
    if message.text.split('_')[0].lower() == 'aadd':
        bd_alert.append(message.text[11:])
        next_star(message)
        my_alert(message, int(message.text.split('_')[1].split(':')[1]), int(message.text.split('_')[1].split(':')[0]),
                 bd_alert[0])



bot.polling(none_stop=True, interval=0)



