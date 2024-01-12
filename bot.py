import telebot
import webbrowser
bot = telebot.TeleBot('6870812177:AAFx3pZv96ETLcFPO7oVL25HI7ct3mVGwkA')

@bot.message_handler()
def main(message):
    if message.text.lower()== '/start':
        bot.send_message(message.chat.id, "ІДІ нахуй, ")
    elif message.text.lower()== '/constitution':
        webbrowser.open('https://docs.google.com/document/d/1FAxjB5v1Fdb4C1x4vguf9BA6Witj4S2kW3mnLilIIcg/edit')
bot.polling(none_stop=True)


