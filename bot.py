import telebot
import config
import random
import time
import schedule

from datetime import datetime
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    """adm = [723412213, 1301071397]  # список из id пользователей 723412213
    if message.chat.id not in adm:
        bot.send_message(message.chat.id, 'Нет доступа')
        print('Пытались пройти: ')
        current_dt = datetime.now().strftime("%y.%m.%d %H:%M:%S")
        print("Время: ")
        print(current_dt.split(), "\n")"""

    if message.chat.type == 'private':
        #sti = open('D:\Downloads\static\welcome.webp', 'rb')
        #bot.send_sticker(message.chat.id, sti)

        # keyboard
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("👋 Поздороваться")
        btn2 = types.KeyboardButton("❓ Задать вопрос")
        btn3 = types.KeyboardButton("⚙️ Функции")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         text="Привет, {0.first_name}! Я тестовый бот".format(
                             message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):

    if message.chat.type == 'private':
        """i = 0
        adm = [723412213, 1301071397]  # список из id пользователей [723412213, 1301071397]
        if message.chat.id not in adm:
            bot.send_message(message.chat.id, 'Нет доступа')
            print('Пытались пройти: ', i)
            current_dt = datetime.now().strftime("%y.%m.%d %H:%M:%S")
            print("Время: ")
            print(current_dt.split(), "\n")
            i += 1"""

        if (message.text == 'Что это?'):
            bot.send_message(message.chat.id, "Это бот, специально созданный для расписаний")

        elif message.text == 'Получить расписание':
            markup = types.InlineKeyboardMarkup(row_width= 2)
            item1 = types.InlineKeyboardButton("Первый", callback_data='per')
            item2 = types.InlineKeyboardButton("Второй", callback_data='vto')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Какой курс?', reply_markup=markup)

        elif message.text == 'Включить рассылку':
            markup = types.InlineKeyboardMarkup(row_width= 2)
            bot.send_message(message.chat.id, 'Рассылка временно не работает', reply_markup=markup)

        elif (message.text == "❓ Задать вопрос"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            btn1 = types.KeyboardButton("Как тебя зовут?")
            btn2 = types.KeyboardButton("Что я могу?")
            btn3 = types.KeyboardButton("Кто разраб?")
            back = types.KeyboardButton("Вернуться в главное меню")
            markup.add(btn1, btn2, btn3, back)
            bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

        elif message.text == "Кто разраб?":
            bot.send_message(message.chat.id, text="Контакты:\nhttps://vk.com/o.elbikov\nelbikov@sfedu.ru")

        elif (message.text == "Как тебя зовут?"):
            bot.send_message(message.chat.id, "У меня нет имени...")

        elif message.text == "Что я могу?":
            bot.send_message(message.chat.id, text="Ты можешь:")
            bot.send_message(message.chat.id, text="Заказать справку")
            bot.send_message(message.chat.id, text="Включить рассылку")
            bot.send_message(message.chat.id, text="Получить расписание")

        elif (message.text == "👋 Поздороваться"):
            bot.send_message(message.chat.id, text="Спасибо, что пользуешься моими функциями")
            """bot.send_sticker(message.chat.id,
                             "CAACAgIAAxkBAAEE2MRikmdsd2Qpv-o6887neQo6fGWrRQAChxoAAr1NOEq9sPjp-eU-CSQE")
            audio = open('D:\Downloads\project\Голосовое сообщение.mp3', 'rb')
            bot.send_audio(message.chat.id, audio)
            audio.close()"""
            time.sleep(15) or time.sleep(20)
            #bot.send_message(message.chat.id, text='Пасхалка - напиши "Хасбик"')

        elif message.text == "Хасбик" or message.text == "хасбик":
            bot.send_sticker(message.chat.id,
                             "CAACAgIAAxkBAAEE2LZikmHQ1logUTtBQD2Fk2EVL3VF3AACJxgAApd54UvWARYS3sXfTyQE")
            bot.send_message(message.chat.id, text="Иууфф")

        elif (message.text == "Хасбулла") or (message.text == "Хасбула")\
                or (message.text == "хасбулла") or (message.text == "хасбула"):
            bot.send_sticker(message.chat.id,
                             "CAACAgIAAxkBAAEE2N5ikm-lsFXB6fZ8JAL8KWLp6AQusgACGRcAAqyBoEon3iKWmrOFFSQE")

        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            btn1 = types.KeyboardButton("Заказать справку")
            btn2 = types.KeyboardButton("Включить рассылку")
            back = types.KeyboardButton("Получить расписание")
            back1 = types.KeyboardButton("Вернуться в главное меню")
            markup.add(btn1, btn2, back, back1)
            bot.send_message(message.chat.id, text="Выбери функцию", reply_markup=markup)

        elif (message.text == "Вернуться в главное меню"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            button1 = types.KeyboardButton("👋 Поздороваться")
            button2 = types.KeyboardButton("❓ Задать вопрос")
            button3 = types.KeyboardButton("⚙️ Функции")
            markup.add(button1, button2, button3)
            bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

        elif (message.text == "⚙️ Функции"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            btn1 = types.KeyboardButton("Заказать справку")
            btn2 = types.KeyboardButton("Включить рассылку")
            back = types.KeyboardButton("Получить расписание")
            back1 = types.KeyboardButton("Вернуться в главное меню")
            markup.add(btn1, btn2, back, back1)
            bot.send_message(message.chat.id, text="Выбери функцию", reply_markup=markup)

        elif message.text == "Заказать справку":
            bot.send_message(message.chat.id,
                             text="Заказать ее ты можешь здесь:\n\n https://docs.google.com/forms/d/1AmbcEKWbro1Z9-mdXZyIlKV3tzNL1njpOWoCEq_qMfU/viewform?edit_requested=true")

        elif message.text == "Прикладная информатика":
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Пн", callback_data='inf-mon-2')
            item2 = types.InlineKeyboardButton("Вт", callback_data='inf-tue-2')
            item3 = types.InlineKeyboardButton("Ср", callback_data='inf-wed-2')
            item4 = types.InlineKeyboardButton("Чт", callback_data='inf-thur-2')
            item5 = types.InlineKeyboardButton("Пт", callback_data='inf-fd-2')
            item6 = types.InlineKeyboardButton("Сб", callback_data='inf-sat-2')
            markup.add(item1, item2, item3, item4, item5, item6)

            bot.send_message(message.chat.id, 'День недели?', reply_markup=markup)

        elif message.text == "Инноватика":
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Пн", callback_data='inn-mon-2')
            item2 = types.InlineKeyboardButton("Вт", callback_data='inn-tue-2')
            item3 = types.InlineKeyboardButton("Ср", callback_data='inn-wed-2')
            item4 = types.InlineKeyboardButton("Чт", callback_data='inn-thur-2')
            item5 = types.InlineKeyboardButton("Пт", callback_data='inn-fd-2')
            item6 = types.InlineKeyboardButton("Сб", callback_data='inn-sat-2')
            markup.add(item1, item2, item3, item4, item5, item6)

            bot.send_message(message.chat.id, 'День недели?', reply_markup=markup)

        elif (message.text == "Инноватика - 1.2"):
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Пн", callback_data='inn-mon-1')
            item2 = types.InlineKeyboardButton("Вт", callback_data='inn-tue-1')
            item3 = types.InlineKeyboardButton("Ср", callback_data='inn-wed-1')
            item4 = types.InlineKeyboardButton("Чт", callback_data='inn-thur-1')
            item5 = types.InlineKeyboardButton("Пт", callback_data='inn-fd-1')

            markup.add(item1, item2, item3, item4, item5)

            bot.send_message(message.chat.id, 'День недели?', reply_markup=markup)
        elif (message.text == "Прикладная информатика - 1.6"):
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Пн", callback_data='inf-mon-1')
            item2 = types.InlineKeyboardButton("Вт", callback_data='inf-tue-1')
            item3 = types.InlineKeyboardButton("Ср", callback_data='inf-wed-1')
            item4 = types.InlineKeyboardButton("Чт", callback_data='inf-thur-1')
            item5 = types.InlineKeyboardButton("Пт", callback_data='inf-fd-1')

            markup.add(item1, item2, item3, item4, item5)

            bot.send_message(message.chat.id, 'День недели?', reply_markup=markup)

        else:
            bot.send_message(message.chat.id, 'Даже не знаю как ответить☹️')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'vto':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                btn1 = types.KeyboardButton("Прикладная информатика")
                btn2 = types.KeyboardButton("Инноватика")
                btn7 = types.KeyboardButton("Назад")
                markup.add(btn1, btn2, btn7)
                bot.send_message(call.message.chat.id, text="Какое направление?", reply_markup=markup)
                time.sleep(0)
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Второй курс")
            elif call.data == 'inf-mon-2':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn7 = types.KeyboardButton("Назад")
                markup.add(btn7)
                bot.send_message(call.message.chat.id, text="Понедельник", reply_markup=markup)
                bot.send_photo(call.message.chat.id, open('D:\Downloads\project\inf-mon-21.jpg', 'rb'))
                bot.send_photo(call.message.chat.id, open('D:\Downloads\project\inf-mon-22.jpg', 'rb'))
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Группа 2.6")
            elif call.data == 'inf-tue-2':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn7 = types.KeyboardButton("Назад")
                markup.add(btn7)
                bot.send_message(call.message.chat.id, text="Вторник", reply_markup=markup)
                bot.send_photo(call.message.chat.id, open('D:\Downloads\project\inf-tue-2.jpg', 'rb'))
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Группа 2.6")
            elif call.data == 'inf-wed-2':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn7 = types.KeyboardButton("Назад")
                markup.add(btn7)
                bot.send_message(call.message.chat.id, text="Среда", reply_markup=markup)
                bot.send_photo(call.message.chat.id, open('D:\Downloads\project\inf-wed-2.jpg', 'rb'))
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Группа 2.6")
            elif call.data == 'inf-thur-2':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn7 = types.KeyboardButton("Назад")
                markup.add(btn7)
                bot.send_message(call.message.chat.id, text="Четверг", reply_markup=markup)
                bot.send_photo(call.message.chat.id, open('D:\Downloads\project\inf-thur-2.jpg', 'rb'))
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Группа 2.6")
            elif call.data == 'inf-fd-2':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn7 = types.KeyboardButton("Назад")
                markup.add(btn7)
                bot.send_message(call.message.chat.id, text="Пятница", reply_markup=markup)
                bot.send_photo(call.message.chat.id, open('D:\Downloads\project\inn-friday-2.jpg', 'rb'))
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Группа 2.6")
            elif call.data == 'inf-sat-2':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn7 = types.KeyboardButton("Назад")
                markup.add(btn7)
                bot.send_message(call.message.chat.id, text="Суббота", reply_markup=markup)
                bot.send_photo(call.message.chat.id, open('D:\Downloads\project\inf-sat-2.jpg', 'rb'))
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Группа 2.6")

            elif call.data == 'inn-mon-2':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn7 = types.KeyboardButton("Назад")
                markup.add(btn7)
                bot.send_message(call.message.chat.id, text="Понедельник", reply_markup=markup)
                bot.send_photo(call.message.chat.id, open('D:\Downloads\project\inn-mon-2.png', 'rb'))
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Группа 2.2")
            elif call.data == 'inn-tue-2':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn7 = types.KeyboardButton("Назад")
                markup.add(btn7)
                bot.send_message(call.message.chat.id, text="Вторник", reply_markup=markup)
                bot.send_photo(call.message.chat.id, open('D:\Downloads\project\inn-tue-2.jpg', 'rb'))
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Группа 2.2")
            elif call.data == 'inn-wed-2':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn7 = types.KeyboardButton("Назад")
                markup.add(btn7)
                bot.send_message(call.message.chat.id, text="Среда", reply_markup=markup)
                bot.send_photo(call.message.chat.id, open('D:\Downloads\project\inn-wed-2.jpg', 'rb'))
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Группа 2.2")
            elif call.data == 'inn-thur-2':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn7 = types.KeyboardButton("Назад")
                markup.add(btn7)
                bot.send_message(call.message.chat.id, text="Четверг", reply_markup=markup)
                bot.send_photo(call.message.chat.id, open('D:\Downloads\project\inn-thur-2.jpg', 'rb'))
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Группа 2.2")
            elif call.data == 'inn-fd-2':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn7 = types.KeyboardButton("Назад")
                markup.add(btn7)
                bot.send_message(call.message.chat.id, text="Пятница", reply_markup=markup)
                bot.send_photo(call.message.chat.id, open('D:\Downloads\project\inn-friday-2.jpg', 'rb'))
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Группа 2.2")
            elif call.data == 'inn-sat-2':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn7 = types.KeyboardButton("Назад")
                markup.add(btn7)
                bot.send_message(call.message.chat.id, text="Суббота", reply_markup=markup)
                bot.send_photo(call.message.chat.id, open('D:\Downloads\project\inn-sat-2.jpg', 'rb'))
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Группа 2.2")

            elif call.data == 'per':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                btn1 = types.KeyboardButton("Прикладная информатика - 1.6")
                btn2 = types.KeyboardButton("Инноватика - 1.2")
                btn7 = types.KeyboardButton("Назад")
                markup.add(btn1, btn2, btn7)
                bot.send_message(call.message.chat.id, text="Какое направление?", reply_markup=markup)
                time.sleep(0)
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Первый курс")
            elif call.data == 'inf-mon-1':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn7 = types.KeyboardButton("Назад")
                markup.add(btn7)
                bot.send_message(call.message.chat.id, text="Понедельник", reply_markup=markup)
                bot.send_photo(call.message.chat.id, open('D:\Downloads\project\inf-mon-1.jpg', 'rb'))
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Группа 1.6")
            elif call.data == 'inf-tue-1':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn7 = types.KeyboardButton("Назад")
                markup.add(btn7)
                bot.send_message(call.message.chat.id, text="Вторник", reply_markup=markup)
                bot.send_photo(call.message.chat.id, open('D:\Downloads\project\inf-tue-1.jpg', 'rb'))
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Группа 1.6")
            elif call.data == 'inf-wed-1':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn7 = types.KeyboardButton("Назад")
                markup.add(btn7)
                bot.send_message(call.message.chat.id, text="Среда", reply_markup=markup)
                bot.send_photo(call.message.chat.id, open('D:\Downloads\project\inn-wed-1.jpg', 'rb'))
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Группа 1.6")
            elif call.data == 'inf-thur-1':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn7 = types.KeyboardButton("Назад")
                markup.add(btn7)
                bot.send_message(call.message.chat.id, text="Четверг", reply_markup=markup)
                bot.send_photo(call.message.chat.id, open('D:\Downloads\project\inf-thur-1.jpg', 'rb'))
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Группа 1.6")
            elif call.data == 'inf-fd-1':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn7 = types.KeyboardButton("Назад")
                markup.add(btn7)
                bot.send_message(call.message.chat.id, text="Пятница", reply_markup=markup)
                bot.send_photo(call.message.chat.id, open('D:\Downloads\project\inn-friday-1.jpg', 'rb'))
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Группа 2.6")

            elif call.data == 'inn-mon-1':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn7 = types.KeyboardButton("Назад")
                markup.add(btn7)
                bot.send_message(call.message.chat.id, text="Понедельник", reply_markup=markup)
                bot.send_photo(call.message.chat.id, open('D:\Downloads\project\inn-mon-1.jpg', 'rb'))
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Группа 1.2")
            elif call.data == 'inn-tue-1':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn7 = types.KeyboardButton("Назад")
                markup.add(btn7)
                bot.send_message(call.message.chat.id, text="Вторник", reply_markup=markup)
                bot.send_photo(call.message.chat.id, open('D:\Downloads\project\inn-tue-1.jpg', 'rb'))
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Группа 1.2")
            elif call.data == 'inn-wed-1':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn7 = types.KeyboardButton("Назад")
                markup.add(btn7)
                bot.send_message(call.message.chat.id, text="Среда", reply_markup=markup)
                bot.send_photo(call.message.chat.id, open('D:\Downloads\project\inn-wed-1.jpg', 'rb'))
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Группа 1.2")
            elif call.data == 'inn-thur-1':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn7 = types.KeyboardButton("Назад")
                markup.add(btn7)
                bot.send_message(call.message.chat.id, text="Четверг", reply_markup=markup)
                bot.send_photo(call.message.chat.id, open('D:\Downloads\project\inn-thur-1.jpg', 'rb'))
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Группа 1.2")
            elif call.data == 'inn-fd-1':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn7 = types.KeyboardButton("Назад")
                markup.add(btn7)
                bot.send_message(call.message.chat.id, text="Пятница", reply_markup=markup)
                bot.send_photo(call.message.chat.id, open('D:\Downloads\project\inn-friday-1.jpg', 'rb'))
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Группа 1.2")

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Курс", reply_markup=None)

            # show alert
            #bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Дальше - значит больше")

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)