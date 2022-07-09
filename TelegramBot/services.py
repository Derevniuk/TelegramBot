from datetime import datetime
from time import sleep
from settnigs import bot


def my_timer(message, add_min, add_hour):
    minutes = str(int(datetime.now().minute) + add_min)
    hour = str(datetime.now().hour + add_hour)
    second = str(datetime.now().second)
    bot.send_message(message.from_user.id, 'Таймер установлен')
    while True:
        if str(datetime.now().hour) == hour and str(datetime.now().minute) == minutes and str(
                datetime.now().second) == second:
            bot.send_message(message.from_user.id, 'Таймер')
            break
        sleep(1)


def my_alarm(message, add_min, add_hour):
    minutes = str(add_min)
    hour = str(add_hour)
    second = '0'
    if add_min < 10:
        add_min = '0' + str(add_min)
    if add_hour < 10:
        add_hour = '0' + str(add_hour)
    bot.send_message(message.from_user.id, f'Будильник установлен на {add_hour}:{add_min}')

    while True:
        if str(datetime.now().hour) == hour and str(datetime.now().minute) == minutes and str(
                datetime.now().second) == second:
            bot.send_message(message.from_user.id, 'Будильник')
            break
        sleep(1)
