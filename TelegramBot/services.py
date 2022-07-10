from datetime import datetime
from time import sleep
from settnigs import bot


def my_timer(message, add_min, add_hour):
    minutes = str(int(datetime.now().minute) + add_min)
    hour = str(datetime.now().hour + add_hour)
    second = str(datetime.now().second)
    bot.send_message(message.from_user.id, 'Timer set')
    while True:
        if str(datetime.now().hour) == hour and str(datetime.now().minute) == minutes and str(
                datetime.now().second) == second:
            bot.send_message(message.from_user.id, 'Timer')
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
    bot.send_message(message.from_user.id, f'Alarm clock set to {add_hour}:{add_min}')

    while True:
        if str(datetime.now().hour) == hour and str(datetime.now().minute) == minutes and str(
                datetime.now().second) == second:
            bot.send_message(message.from_user.id, 'Alarm!!!')
            break
        sleep(1)


"""minutes validator"""


def time_calculation(total_minute: int):
    if total_minute > 60:
        extra_hours = total_minute // 60
        extra_minute = total_minute - 60 * extra_hours
        return extra_hours, extra_minute
    else:

        return 0, total_minute



