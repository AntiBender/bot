import telebot
import config
import random
import datetime

then = datetime.datetime(2019, 3, 15,1,19,45)

from telebot import types

bot = telebot.TeleBot(config.TOKEN)
now = datetime.datetime.now()
idi=0

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIhUF45HEQMuHoZU6AjWuKPkGxqhag_AAJXAwACz7vUDnOJW_OaTIUaGAQ')

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('⌛Сколько мы вместе?⌛')
    item2 = types.KeyboardButton("😊 Как дела?")

    markup.add(item1, item2)

    bot.send_message(message.chat.id,
                     "Зайчик мой, поздравляю тебя с Днем святого Валентина и дарю тебе твой персональный Телеграм бот, он создан специально для тебя, ведь ты у меня особенная. Я тебя безумно, люблю и хочу чтобы у тебя было все самое лучшие, и то чего у остальных никогда не будет.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    idi = message.chat.id
    now = datetime.datetime.now()
    if str(now.strftime("%X")) == "19:01:00":
        bot.send_message(message.chat.id, "Люблю тебя !!!!!!!")
    if message.chat.type == 'private':
        if message.text == '⌛Сколько мы вместе?⌛':
            delta = now - then
            string=''
            if(delta.days // 365) !=0:
                if (delta.days // 365) % 10 == 1:
                    string += str(delta.days // 365) + " Год "
                elif (delta.days // 365) % 10 >= 2 and (delta.days // 365) % 10 <= 4:
                    string += str(delta.days // 365) + " Годa "
                else:
                    string += str(delta.days // 365) + " Лет "


            if (delta.days%365)%10==1 :
                string += str(delta.days%365)+" День "
            elif (delta.days%365)%10>=2 and (delta.days%365)%10<=4 :
                string += str(delta.days%365) + " Дня "
            else:
                string += str(delta.days%365) + " Дней "

            if (delta.seconds//3600)%10==1 :
                string += str(delta.seconds//3600)+" Час "
            elif (delta.seconds//3600)%10>=2 and (delta.seconds//3600)%10<=4 :
                string += str(delta.seconds//3600) + " Часа "
            else:
                string += str(delta.seconds//3600) + " Часов "

            if ((delta.seconds%3600)//60)%10==1 :
                string += str((delta.seconds%3600)//60)+" Минуту "
            elif ((delta.seconds%3600)//60)%10>=2 and ((delta.seconds%3600)//60)%10<=4 :
                string += str((delta.seconds%3600)//60) + " Минуты "
            else:
                string += str((delta.seconds%3600)//60) + " Минут "

            if ((delta.seconds%3600)%60)%10==1 :
                string += str((delta.seconds%3600)%60)+" Секунда "
            elif ((delta.seconds%3600)%60)%10>=2 and ((delta.seconds%3600)%60)%10<=4 :
                string += str((delta.seconds%3600)%60) + " Секунды "
            else:
                string += str((delta.seconds%3600)%60) + " Секунд "

            bot.send_message(message.chat.id, string )
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIhVF45HHjry4Xnu51TgWtmjQ4fz8rrAAJsAwACz7vUDpl9IK2QyV_hGAQ')
        elif message.text == '😊 Как дела?':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Отлично, сама как?', reply_markup=markup)
        elif message.text == '1':
            bot.send_message(message.chat.id, str(now.strftime("%X")))
            bot.send_message(message.chat.id, str(idi))

        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
                bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAIhVl45HLf4zwPYk4msWP0kbnCOMXXLAAJiAwACz7vUDosKqm0O4xndGAQ')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Блиииин😢 Позвони котику !!!! ')

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                                  reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Люблю тебя!!!!")

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)