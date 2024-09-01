import telebot
import random
import  webbrowser
from telebot import types
from hangman import HangmanGame


API_TOKEN = "7320550150:AAF1ygOgSgonhnrd7ovfQpDNwn1GvaKB6XA"
bot = telebot.TeleBot(API_TOKEN)
hg = HangmanGame()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Приветствую , Я Лиса , твой помощник !")

@bot.message_handler(commands=['site','website'])
def site(message):
    webbrowser.open('66b66c03a42e7.site123.me')    

@bot.message_handler(commands=['tg'])
def main(message):
    bot.send_message(
        message.chat.id,
        '✧─── ･ ｡ﾟ★: *.✦ .* :★. ───✧\n' +
        'Канал с важными новостями:\n'
        'https://t.me/Princess_lisa_info'
        )

@bot.message_handler(commands=['help'])
def help_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Message the developer', url='66b66c03a42e7.site123.me'
        )
    )
    bot.send_message(
        message.chat.id,
        '✧─── ･ ｡ﾟ★: *.✦ .* :★. ───✧\n' +
        '1) Установка - инструкция бота\n' +
        '2) Команды - список команд\n' +
        '3) Информация о нас\n'+
        '✧─── ･ ｡ﾟ★: *.✦ .* :★. ───✧\n',
        reply_markup=keyboard
    )

saved_messages = []

@bot.message_handler(func=lambda message: message.text.startswith("Лис самый крутой ком"))
def respond_to_lis_request(message):
    if saved_messages:
        random_message = random.choice(saved_messages)
        user_input = " ".join(message.text.split()[3:]) 
        bot.reply_to(message, f"Самый лучший коментарий сегодня : {random_message}")
    else:
        bot.reply_to(message, "Извините, пока нет сохраненных сообщений.")



@bot.message_handler()
def on_message(message):
    if hg.game_on :
        if len(message.text) > 1:
            bot.send_message(message.chat.id , text = 'Вводить можно только буквы ! ')
            return
        msg = hg.game_step(message.text)
        bot.send_message(message.chat.id , text=msg)
        return
    if message.text == 'виселица':
        hg.start()
        text = f'Добро пожаловать в игру ! \n {hg.info()}'
        bot.send_message(message.chat.id , text = text  )

bot.polling

@bot.message_handler(func=lambda message: True)
def save_user_message(message):
    saved_messages.append(message.text)




if __name__ == "__main__":
    bot.polling(none_stop=True)



