import telebot
from telebot import types
import random
import schedule
import time


bot = telebot.TeleBot('5964468386:AAEwp0m0SGnG1kN6DaHPq9_xBXfrXyo1Y50')

# def job(message):
#     bot.send_message(message.chat.id, 'чего не заходишь? я скучаю(', parse_mode='html')
# schedule.every(1).minutes.do(job)
# while True:
#     schedule.run_pending()
#     time.sleep(1)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет! Меня зовут Кукуха) Приятно познакомиться <b>{message.from_user.first_name}<u>' \
           f'{message.from_user.last_name}</u>>)</b> Для начала нажми /kyky'
    bot.send_message(message.chat.id, mess, parse_mode='html')



@bot.message_handler(commands=['opa'])
def handle_text(message):
    numvan = bot.send_message(message.chat.id, 'напиши первое число')
    bot.register_next_step_handler(numvan, num1_fun)


def num1_fun(message):
    global num1;
    num1 = message.text
    numtwo = bot.send_message(message.chat.id, 'а второе?')
    bot.register_next_step_handler(numtwo, num2_fun)


def num2_fun(message):
    global num2;
    num2 = message.text
    operu = bot.send_message(message.chat.id, 'а что сделать, то надо?(+,-,*,/)')
    bot.register_next_step_handler(operu, operi)


def operi(message):
    global oper;
    oper = message.text
    if oper == "+":
        resylit = int(num1) + int(num2)
        bot.send_message(message.chat.id, resylit)
    elif oper == "-":
        resylit = int(num1) - int(num2)
        bot.send_message(message.chat.id, resylit)
    elif oper == "*":
        resylit = int(num1) * int(num2)
        bot.send_message(message.chat.id, resylit)
    elif oper == "/":
        resylit = int(num1) / int(num2)
        bot.send_message(message.chat.id, resylit)
    else:
        bot.send_message(message.chat.id, "ошибка введите /opa")

balanse = 2000;
@bot.message_handler(commands=['casino'])
def casino(message):
    global balanse;
    if balanse == 0 :
        bot.send_message(message.chat.id, "а у тебя больше нет")
        balanse =+ 2000
    else:
        ctav = bot.send_message(message.chat.id, f"в кошельке: {balanse} сколько закинем?")
        bot.register_next_step_handler(ctav ,ctavka_fun)
def ctavka_fun(message):
    global balanse;
    ctavka = int(message.text)
    if ctavka > balanse:
        bot.send_message(message.chat.id, "пф, у тебя столько нет")
    else:
        ran = bot.send_message(message.chat.id, "1 или 2")
        bot.register_next_step_handler(ran ,ran_fun,ctavka)
def ran_fun(message,ctavka):
    global balanse;
    ran = int(message.text)
    ranr = random.randint(0, 2)
    balanse-=ctavka
    if ran == ranr:
        ctavka*=2
        balanse+=ctavka
        cas = bot.send_message(message.chat.id, f"Ура, поздравляю! У тебя: {balanse} ещё хочешь?) /casino")
    else:
        cas = bot.send_message(message.chat.id, f"ЭЭх, не везет что-то! У тебя: {balanse} ещё? /casino")



@bot.message_handler(commands=['kyky'])
def kyky(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    b1 = types.KeyboardButton('👩‍💻 классный сайт')
    b2= types.KeyboardButton('🧐️ интересненькое')
    b3= types.KeyboardButton('🤪 шутка')
    b4= types.KeyboardButton('🥸 что-то скучное')
    markup.add(b1, b2, b3, b4)
    bot.send_message(message.chat.id,'Выбирай:', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.chat.type == 'private':
        if message.text == '🧐️ интересненькое':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            b1 = types.KeyboardButton('🪙 орёл или решка')
            b2 = types.KeyboardButton('🔀 число до 1000')
            b3 = types.KeyboardButton('🎰 казино')
            b4 = types.KeyboardButton('📎приборчик')
            back = types.KeyboardButton('↩ назад')
            markup.add(b1, b2, b3,b4, back)
            bot.send_message(message.chat.id, 'что выберешь?🧐️ ', reply_markup=markup)
        elif message.text == '🪙 орёл или решка':
            variants = ['🦅 орёл', '1️⃣ решка']
            bot.send_message(message.chat.id, 'Опа!' + str(random.choice(variants)))
        elif message.text == '🔀 число до 1000':
            bot.send_message(message.chat.id, 'Ого! Это число:' + str(random.randint(0, 1000)))

        elif message.text == '🎰 казино':
            bot.send_message(message.chat.id, 'Хочешь попытать удачу? Жми! /casino', parse_mode='html')

        elif message.text == '📎приборчик':
            bot.send_message(message.chat.id, 'Плохо с математикой?) Тебе сюда /opa', parse_mode='html')


        elif message.text == '🤪 шутка':
            variants = ['По салону самолета проходит пилот с парашютом. Пассажирка интересуется:– Что случилось?Пилот '
                        'отвечает:– А так, ерунда, неприятности на работе.',
                        'Профессор финансовой академии идет по коридору. Доходит до аудитории и видит на пороге в хлам пьяного студента.'
                        ' В ярости он спрашивает:— Какой курс?!— 61 рубля 25 копейки',
                        'Олег хотел прикинуться дрессировщиком тигров.Но его быстро раскусили.',
                        'В мaршрутке стaрушкa долго и пристaльно смотрелa нa жующего жвaчку студента...Смотрелa-смотрелa'
                        ' и говорит, нaклонившись: "Зря, сынок, ты это мне всё рaсскaзывaешь... не слышу ничего!"',
                        'Кто-нибудь из ваших друзей страдает алкоголизмом?Никто не страдает, всем нравится']
            bot.send_message(message.chat.id,  str(random.choice(variants)))
        elif message.text == '🥸 что-то скучное':
            bot.send_message(message.chat.id, 'Приветик! Прошу не судить строго) Это мой первый бот.'
                                              ' Создан с целью юмора, без него было бы очень туго. Дальше - больше!)'
                                              ' Готова учесть всю критику и пожелания🙃', parse_mode='html')
        elif message.text == '↩ назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            b1 = types.KeyboardButton('👩‍💻 классный сайт')
            b2 = types.KeyboardButton('🧐️ интересненькое')
            b3 = types.KeyboardButton('🤪 шутка')
            b4 = types.KeyboardButton('🥸 что-то скучное')
            markup.add(b1, b2, b3, b4)
            bot.send_message(message.chat.id, 'Выбирай:', reply_markup=markup)
        elif message.text == '👩‍💻 классный сайт':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Посетить веб-сайт", url="https://overone.by/"))
            bot.send_message(message.chat.id, 'Для сайта -сюда)', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Не понимаю, что ты хочешь.Давай сначала)", parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Вот это да! Это ты?)')







bot.polling(none_stop=True)