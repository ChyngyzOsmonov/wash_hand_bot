import random
from threading import Thread
import telebot
from telebot import types
import cfg
import time

Langs = types.ReplyKeyboardMarkup(resize_keyboard=True)
bl1 = types.KeyboardButton('English 🇬🇧')
bl2 = types.KeyboardButton('Русский 🇷🇺')
bl3 = types.KeyboardButton('Кыргызча 🇰🇬')
start = types.KeyboardButton('/start')
b4eng = types.KeyboardButton('Stop')
b4rus = types.KeyboardButton('Остановить')
b4kgz = types.KeyboardButton('Токтотуу')
Langs.add(bl1, bl2)
Langs.add(bl3)
Langs.add(start)

time_Eng = types.ReplyKeyboardMarkup(resize_keyboard=True)
t1 = types.KeyboardButton('30')
t2 = types.KeyboardButton('60')
t3 = types.KeyboardButton('Change language')
time_Eng.add(t1, t2)
time_Eng.add(t3)

time_Rus = types.ReplyKeyboardMarkup(resize_keyboard=True)
rus = types.KeyboardButton('Сменить язык')
time_Rus.add(t1, t2)
time_Rus.add(rus)

time_Kgz = types.ReplyKeyboardMarkup(resize_keyboard=True)
kgz = types.KeyboardButton('Тилди алмаштыруу')
time_Kgz.add(t1, t2)
time_Kgz.add(kgz)

stop_Eng = types.ReplyKeyboardMarkup(resize_keyboard=True)
stop_Eng.add(b4eng)

stop_Kgz = types.ReplyKeyboardMarkup(resize_keyboard=True)
stop_Kgz.add(b4kgz)

stop_Rus = types.ReplyKeyboardMarkup(resize_keyboard=True)
stop_Rus.add(b4rus)

bot = telebot.TeleBot(cfg.token)


def random_rus():
    text = ['Пора мыть руки! \n\nДержите руки в чистоте, ',
            'Пора мыть руки! \n\nЧасто мойте их с мылом или используйте дезинфицирующее средство, перед едой обязательно мойте руки. Старайтесь не касаться рта, носа или глаз немытыми руками;',
            'Пора мыть руки! \n\nНа работе регулярно очищайте поверхности и устройства, к которым вы прикасаетесь (клавиатура компьютера, панели оргтехники общего использования, экран смартфона, пульты, дверные ручки и поручни).',
            'Пора мыть руки! \n\nНосите с собой одноразовые салфетки и всегда прикрывайте нос и рот, когда вы кашляете или чихаете, и утилизируйте их после использования.',
            'Пора мыть руки! \n\nНосите обязательно с собой дезинфицирующее средство для рук, чтобы в любой обстановке вы могли очистить их.',
            'Пора мыть руки! \n\nЧасто проветривайте помещение.',
            'Пора мыть руки! \n\nРасскажите детям о профилактике коронавируса.',
            'Пора помыть руки!',
            'Пора мыть руки! \n\nМытье рук – самый простой способ профилактики.',
            'Время мыть руки! \n\nЧерез грязные руки в наш кишечник попадают паразиты и возбудители диареи всех видов.',
            'Время мыть руки! \n\nМыть руки нужно, как минимум, в 8 случаях: когда вы сходили в туалет, чихнули, покашляли, высморкались, приготовили еду, выбросили мусор, погладили животное и вернулись с улицы.',
            'Пора мыть руки! \n\nЕсли мыла нет – все равно лучше помыть руки, чем пойти с грязными.',
            'Пора мыть руки! \n\nМойте руки от 20 секунд до минуты. Главное – не меньше.',
            'Пора мыть руки! \n\nВытирайте руки сухим или бумажным полотенцем. Использовать сушку – лучше, чем не использовать.',
            'Пора мыть руки! \n\nВытирать об одежду или не вытирать совсем – свести все на нет.',
            'Пора мыть руки! \n\nЕсли помыть руки негде – используйте антисептик.',
            'Пора мыть руки! \n\nБольшинство бактерий на руках находиться на кончиках пальцев и под ногтями',
            'Пора мыть руки! \n\nРуки необходимо мыть с внутренней и тыльной стороны, между пальцами и стараться промыть под ногтями.',
            'Пора мыть руки! \n\nУже научились мыть руки? А теперь не забывайте дезинфекцировать ваш телефон! \nПомните, 97% спирт НЕ убивает вирус, а только оглушает его. Раствор должен быть от 60%'
            ]
    return random.choice(text)


def random_eng():
    text = [
        'It’s time to wash your hands! \n\nKeep your hands clean, wash them often using soap or disinfect, make sure that you washed your hands before eating.',
        'It’s time to wash your hands! \n\nTry not to touch your mouth, nose or eyes with unwashed hands.',
        'It’s time to wash your hands! \n\nClean regularly surfaces and devices you touch (computer’s keyboard, office equipment panels, smartphone’s screen, remotes, door handles, handrails).',
        'It’s time to wash your hands! \n\nCarry one-off napkins with you and cover your nose and mouth every time you cough or sneeze, and always utilize them after using. ',
        'It’s time to wash your hands! \n\nCarry a hand  sanitizer so that you can clean them anytime.',
        'It’s time to wash your hands! \n\nAir out the space often. Tell the children about coronavirus preventions.',
        'It’s time to wash your hands!',
        'It’s time to wash your hands! \n\nWashing hands is the easiest way for prevention.',
        'It’s time to wash your hands! \n\nThrough dirty hands parasites and all-kinds of diarrhea pathogens enter our intestine.',
        'It’s time to wash your hands! \n\nYou should wash your hands at least in 8 cases: when you go to the WC, sneeze, cough, blow your nose, prepare food, throw out the trash, stroke the animal and return from outside. ',
        'It’s time to wash your hands! \n\nEven if you don’t have soap, it’s still better to wash your hands than to go with dirty ones. ',
        'It’s time to wash your hands! \n\nWash your hands for 20 seconds to a minute. No less.',
        'It’s time to wash your hands! \n\nWipe your hands with dry or paper towel. To use drying is better than not to do.',
        'It’s time to wash your hands! \n\nTo wipe them on clothes or not to wipe them at all – to reduce all to nothing.',
        'It’s time to wash your hands! \n\nIf you have no place where you can wash your hands in, use the antiseptic.',
        'Time to wash your hands! \n\nMost of the bacteria on the hands are on your fingertips and under your nails.',
        'It’s time to wash your hands! \n\nHands should be washed from the inside and from the back, between fingers and under the nails.'
    ]
    return random.choice(text)


def random_kgz():
    text = [
        'Кол жууш мезгили!',
        'Кол жууш мезгили! \n\nКолду жууганы- оорулардын алдын алууга эң жөнөкөй жолу.',
        'Кол жууш мезгили! \n\nКир кол аркылуу биздин ичегибизге паразиттер жана диареянын козгогучтарынын бардык түрлөрү кире алат.',
        'Кол жууш мезгили! \n\nКолду, эң аз дегенде, 8 учурда жууш керек: дааратканага барганда,  чүчкүргөндө, жөтөлгөндө, чимкиргенде, тамак даярдаганда, таштандыларды чыгарганда, жаныбарларды сылаганда жана көчөдөн келгенде.',
        'Кол жууш мезгили! \n\nЭгерде самын жок болсо, кир кол менен жүрбөстөн,  колду жууганы артык. Колду 20 секундадан бир мүнөтко чейинки убакытта жуугула. Эң негизи - андан аз болбосун.',
        'Кол жууш мезгили! \n\nКолду кургак же кагаз сүлгү менен аарчыгыла. Кургаткычты колдонуу - колдонбогондон артык.',
        'Кол жууш убагы! \n\nКолду кийимге аарчыганы же такыр аарчыбаганы  ишти жокко чыгарат. Кол жууган жай болбосо, антисептикти колдонгула.',
        'Кол жууш мезгили. \n\nБактериялардын көбүнчөсү бармактын учунда жана тырмактардын астында жайгашат. Колду ичинен жана сыртынан, бармактардын ортосунан жууш керек, жана тырмак астында жууганга аракет кылыш керек.'
    ]
    return random.choice(text)


@bot.message_handler(commands=['start'])
def welcome(m):
    def start_thread():
        # if m.chat.id in cfg.users:
        #     pass
        # else:
        outfile = open('users.txt', 'a')
        cfg.users[m.chat.id] = {'lang': 'rus', 'work30': False, 'work60': False, 'say': 0}
        outfile.write(str(m.from_user.first_name + '\n'))
        outfile.close()
        bot.send_message(m.chat.id, 'Выберите язык', reply_markup=Langs)
        print('New user:', m.from_user.first_name, m.from_user.last_name, 'nick:', m.from_user.username)

    if __name__ == '__main__':
        Thread(target=start_thread).start()


@bot.message_handler(content_types=['text'])
def answers(m):
    def text_thread():
        if m.text == 'English 🇬🇧':
            cfg.users[m.chat.id]['lang'] = 'eng'
            bot.send_message(m.chat.id, 'Choose a time to remind', reply_markup=time_Eng)
        elif m.text == 'Русский 🇷🇺':
            cfg.users[m.chat.id]['lang'] = 'rus'
            bot.send_message(m.chat.id, 'Выберите время для напоминания', reply_markup=time_Rus)
        elif m.text == 'Кыргызча 🇰🇬':
            cfg.users[m.chat.id]['lang'] = 'kgz'
            bot.send_message(m.chat.id, 'Эскертүү үчүн убакытты тандаңыз', reply_markup=time_Kgz)

        if m.text == '30':
            cfg.users[m.chat.id]['say'] = 30
            cfg.users[m.chat.id]['work30'] = True
        if m.text == '60':
            cfg.users[m.chat.id]['say'] = 60
            cfg.users[m.chat.id]['work60'] = True

        if m.text == 'Stop' or m.text == 'Остановить' or m.text == 'Токтотуу':
            cfg.users[m.chat.id]['work30'] = False
            cfg.users[m.chat.id]['work60'] = False
            if m.text == 'Stop':
                bot.send_message(m.chat.id, 'Stopped!', reply_markup=time_Eng)
            elif m.text == 'Остановить':
                bot.send_message(m.chat.id, 'Остановлено!', reply_markup=time_Rus)
            elif m.text == 'Токтотуу':
                bot.send_message(m.chat.id, 'Токтотулду!', reply_markup=time_Kgz)

        if m.text == 'Change language' or m.text == 'Сменить язык' or m.text == 'Тилди алмаштыруу':
            if m.text == 'Change language':
                cfg.users[m.chat.id]['lang'] = 'eng'
                bot.send_message(m.chat.id, 'Choose language!', reply_markup=Langs)
            elif m.text == 'Сменить язык':
                cfg.users[m.chat.id]['lang'] = 'rus'
                bot.send_message(m.chat.id, 'Выберите язык!', reply_markup=Langs)
            elif m.text == 'Тилди алмаштыруу':
                cfg.users[m.chat.id]['lang'] = 'kgz'
                bot.send_message(m.chat.id, 'Тилди тандаңыз!', reply_markup=Langs)
        if 22 <= int(time.strftime('%H')) <= 7:
            pass
        else:
            while cfg.users[m.chat.id]['work30'] == True:
                if cfg.users[m.chat.id]['lang'] == 'rus':
                    if m.text == '30':
                        bot.send_message(m.chat.id, random_rus(), reply_markup=stop_Rus)
                        time.sleep(1800)
                elif cfg.users[m.chat.id]['lang'] == 'kgz':
                    if m.text == '30':
                        bot.send_message(m.chat.id, random_kgz(), reply_markup=stop_Kgz)
                        time.sleep(1800)
                elif cfg.users[m.chat.id]['lang'] == 'eng':
                    if m.text == '30':
                        bot.send_message(m.chat.id, random_eng(), reply_markup=stop_Eng)
                        time.sleep(1800)

            while cfg.users[m.chat.id]['work60'] == True:
                if cfg.users[m.chat.id]['lang'] == 'rus':
                    if m.text == '60':
                        bot.send_message(m.chat.id, random_rus(), reply_markup=stop_Rus)
                        time.sleep(3600)
                elif cfg.users[m.chat.id]['lang'] == 'kgz':
                    if m.text == '60':
                        bot.send_message(m.chat.id, random_kgz(), reply_markup=stop_Kgz)
                        time.sleep(3600)
                elif cfg.users[m.chat.id]['lang'] == 'eng':
                    if m.text == '60':
                        bot.send_message(m.chat.id, random_eng(), reply_markup=stop_Eng)
                        time.sleep(3600)

    if __name__ == '__main__':
        Thread(target=text_thread).start()


try:
    bot.polling(none_stop=True, interval=0, timeout=30)
except Exception as E:
    print(E)
