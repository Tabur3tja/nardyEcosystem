import telebot
import webbrowser
import sqlite3
from telebot import types
import re


bot = telebot.TeleBot('6870812177:AAFx3pZv96ETLcFPO7oVL25HI7ct3mVGwkA')
#'https://t.me/b_nardy_bot?startgroup=pm'
@bot.message_handler(commands=['start'])
def main(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Додати бот до чату', 'https://t.me/b_nardy_bot?startgroup=pm'))
    bot.send_message(message.chat.id,f'Привіт {message.from_user.first_name}',reply_markup=markup)
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,'Плотну всім нашим!!!💪💪💪 \n '
                                    '1.  Валюта – єМарка 💰💰💰\n \n'
                                     '2.  Система переходу на наступний ранг накопичувальна. Якщо для переходу на наступний ранг необхідно умовно 10 ударів то це не обхідно нанести сумарно 10 ударів по одному або декількох противниках. \n\n'
                                     '3.  єМарки надаються учаснику при виклику функції єДопомога (команда /esupply), окрім певних винятків(див. п. 9).\n'
                                     '\t3.1.  Можливість викликати єДопомога визначається для кожного учасника випадково від 30 хвилин до 90 хвилин\n'
                                     '\t3.2.  єШанс отримати «тисячу Зеленського» \n\n'
                                     '4.  Нанесення удару по противнику. (команда /bayraktar) 🚀🚀🚀'
                                    '\t4.1.  Для цього потрібно використати «відбайрактарювання», окрім певних винятків(див. п. 9).\n'
                                    '\t4.2.  1 байрактар =1 єМарка\n\n'

                                    '5.  Ракети до Петріота.(/patriot) 🛡🛡🛡\n'
                                    '\t5.1.  «Ракети до Петріот» захищає від ударів «байрактару».\n'
                                    '\t5.2.  1 Ракета до Петріот = 1 єМарка\n'
                                    '\t5.3.  При настакуванні більше 5 Ракет до Петріот, від 5 до 10 Ракет до Петріот вартує 2єМарки.Від 10 Ракет до Петріот 10 єМарок\n\n'

                                    '6.  Ранги. (команда /ranks)\n'
                                    '\t6.1.  Щоб підвищити ранг потрібно нанести певну к-сть «відбайрактарювань». К-сть «відбайрактарювань» зазначена у даному документі у пункті 6.2.\n'
                                    '6.2.  \n'
                                    '\t1 ранг «Ухилянт» -  1 «відбайрактарювання»\n'
                                    '\t2 ранг «Зйобок» - 20 «відбайрактарювань»\n'
                                    '\t3 ранг «Гой» - 50 «відбайрактарювань»\n'
                                    '\t4 ранг «Кіріл Буданов» - 100 «відбайрактарювань» 🐅🐅🐅\n'
                                    '\t5 ранг «Заступник Єрмака» - 500 «відбайрактарювань»\n\n'

                                    '7. єДопомога.\n'
                                    '7.1.\n'
                                    '\t1 ранг = 1 єМарка\n'
                                    '\t2 ранг = 2 єМарок\n'
                                    '\t3 ранг = 5 єМарок\n'
                                    '\t4 ранг = 10 єМарок\n\n'

                                    '8. ТЦК (/buy_recruiting_center\n'
                                    '\t8.1. ТЦК коштує 10 єМарок\n'
                                    '\t8.2. При виклику ф-ції єДопомога ти отримуєш 5 ТЦКшників за кожен ТЦК.\n'
                                    '\t8.3 Одна повістка коштує 15 ТЦКшників і к-сть єМарок яка дорівнює рівню твого рангу.\n'
                                    '\t8.4 ТЦК можна стакати і відповідно стакати ТЦКшників при сталій ціні повістки.\n'
                                    '\t8.5 Ефект повістки блокує рахунок,відтерміновує виклик єДопомога. Ефект повісток стакається по формулі +5хв нижній поріг і +10 хв верхній поріг.\n'
                                     ' Наприклад:  1 повістка = рандомна довжина ефекту від 5хв до 10хв. 2 повістка = рандомна довжина ефекту від 10хв до 20 хв. І так далі.\n\n'

                                    '9. Заступник Єрмака 🐷🐷🐷\n'
                                    '\t 9.1.  По досягненню 5 рангу гравець перестає отримувати єМарки за єДопомогу, замість цього гравець отримує 18% з єДопомоги кожного гравця\n'
                                    '\t9.2.  Не можливо "відбайрактарити" кого-небудь, маючи 5 ранг\n'
                                    '\t9.3.  При досягненні кимось з гравців 4 рангу квоти "відбайрактарювань", при наявності Заступника Єрмака, гравець, який набрав квоту набуває 5 рангу, натомість поточний "Заступник", понижується до 4 рангу\n'
                     ,parse_mode='html')
@bot.message_handler(commands=['esupply'])
def esupply(message):
    #файл має зберігатися на сервері та відкриватися відповідно звідти
    file = open('./copium-4.mp4','rb')
    bot.send_video(message.chat.id,file,caption='*гравець* зібрав єДопомогу 🇺🇦 \nєМарки - 💰\nТЦКшники - 👮🏾‍♀️')
@bot.message_handler(commands=['bayraktar'])
def bayraktar(message):
    num_bayraktar_str = message.text
    splitted_bayraktar_num = num_bayraktar_str.split()


    if len(splitted_bayraktar_num) == 2:
        try:
            num_bayraktar = int(splitted_bayraktar_num[1])
        except ValueError:
            bot.send_message(message.chat.id,'Введене некоректне числове значення')
    elif len(splitted_bayraktar_num) == 1:
        num_bayraktar = 1
    else:
        bot.send_message(message.chat.id, 'Не вдалось відбайрактарити')

    if message.reply_to_message is not None and message.reply_to_message.from_user.is_bot is False:
        bayraktared_user = message.reply_to_message.from_user.username
        bot.send_message(message.chat.id, f'Ви @{message.from_user.username} відбайрактарили: @{bayraktared_user} {num_bayraktar} раз')
    else:
        bot.send_message(message.chat.id, 'Не вдалось відбайрактарити бота')

@bot.message_handler(commands=['message'])
def mess(message):
    bot.send_message(message.chat.id,message)
bot.polling(none_stop=True)


