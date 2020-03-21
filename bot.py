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
b4ukr = types.KeyboardButton('Токтотуу')
Langs.add(bl1, bl2)
Langs.add(bl3)
Langs.add(start)

time_Eng = types.ReplyKeyboardMarkup(resize_keyboard=True)
t1 = types.KeyboardButton('30')
t2 = types.KeyboardButton('60')
time_Eng.add(t1, t2)
time_Eng.add(b4eng)

time_Rus = types.ReplyKeyboardMarkup(resize_keyboard=True)
time_Rus.add(t1, t2)
time_Rus.add(b4rus)

time_Kgz = types.ReplyKeyboardMarkup(resize_keyboard=True)
time_Kgz.add(t1, t2)
time_Kgz.add(b4ukr)

bot = telebot.TeleBot(cfg.token)


def random_rus_30m():
    text = ['Держите руки в чистоте, '
            '\nЧасто мойте их с мылом или используйте дезинфицирующее средство, '
            '\nперед едой обязательно мойте руки.', 'Старайтесь не касаться рта, носа или глаз немытыми руками;',
            '\nНа работе регулярно очищайте поверхности и устройства, '
            '\nк которым вы прикасаетесь (клавиатура компьютера, панели оргтехники общего использования, '
            '\nэкран смартфона, пульты, дверные ручки и поручни).',
            '\nНосите с собой одноразовые салфетки и всегда прикрывайте нос и рот, когда вы кашляете или чихаете, '
            '\nи утилизируйте их после использования.',
            '\nНосите обязательно с собой дезинфицирующее средство для рук, '
            '\nчтобы в любой обстановке вы могли очистить их.',
            '\nЧасто проветривайте помещение.',
            '\nРасскажите детям о профилактике коронавируса.']
    return random.choice(text)


def random_rus_1h():
    text = [
        'Пора помыть руки.',
        'Мытье рук – самый простой способ профилактики.',
        'Время мыть руки. Через грязные руки в наш кишечник попадают паразиты и возбудители диареи всех видов.',
        'Время мыть руки. Мыть руки нужно, как минимум, в 8 случаях: когда вы сходили в туалет, чихнули, покашляли, '
        '\nвысморкались, приготовили еду, выбросили мусор, погладили животное и вернулись с улицы.',
        'Если мыла нет – все равно лучше помыть руки, чем пойти с грязными.',
        'Мойте руки от 20 секунд до минуты. Главное – не меньше.',
        'Вытирайте руки сухим или бумажным полотенцем. Использовать сушку – лучше, чем не использовать.',
        'Время мыть руки. Вытирать об одежду или не вытирать совсем – свести все на нет.',
        'Если помыть руки негде – используйте антисептик.',
        'Пора помыть руки. Большинство бактерий на руках находиться на кончиках пальцев и под ногтями',
        'Руки необходимо мыть с внутренней и тыльной стороны, между пальцами и стараться промыть под ногтями.'
    ]
    return random.choice(text)


def random_eng_30m():
    text = [
        'Keep your hands clean, wash them often using soap or disinfect, '
        '\nmake sure that you washed your hands before eating.',
        'Try not to touch your mouth, nose or eyes with unwashed hands.',
        'Clean regularly surfaces and devices you touch '
        '\n(computer’s keyboard, office equipment panels, smartphone’s screen, remotes, door handles, handrails).',
        'Carry one-off napkins with you and cover your nose and mouth every time you cough or sneeze, '
        '\nand always utilize them after using. ',
        'Carry a hand  sanitizer so that you can clean them anytime.',
        'Air out the space often.'
        'Tell the children about coronavirus preventions.'
    ]
    return random.choice(text)


def random_eng_1h():
    text = [
        'It’s time to wash your hands.',
        'Washing hands is the easiest way for prevention.',
        'Time to wash your hands. Through dirty hands parasites and all-kinds of diarrhea pathogens enter our intestine.',
        'Time to wash your hands. You should wash your hands at least in 8 cases: when you go to the WC, sneeze, cough,'
        '\nblow your nose, prepare food, throw out the trash, stroke the animal and return from outside. ',
        'Even if you don’t have soap, it’s still better to wash your hands than to go with dirty ones. ',
        'Wash your hands for 20 seconds to a minute. No less.',
        'Wipe your hands with dry or paper towel. To use drying is better than not to do.',
        'It’s time to wash your hands.  To wipe them on clothes or not to wipe them at all – to reduce all to nothing.',
        'If you have no place where you can wash your hands in, use the antiseptic.',
        'Time to wash your hands. Most of the bacteria on the hands are on your fingertips and under your nails.',
        'Hands should be washed from the inside and from the back, between fingers and under the nails.'
    ]
    return random.choice(text)


def random_kgz_30m():
    text = [
        'Кол жууш мезгили.',
        'Колду жууганы- оорулардын алдын алууга  эң жөнөкөй жолу.',
        'Кол жууш убагы. Кир кол аркылуу биздин ичегибизге паразиттер жана диареянын козгогучтарынын бардык түрлөрү кире алат.',
        'Кол жууш убагы. Колду, эң аз дегенде, 8 учурда жууш керек: дааратканага барганда,  чүчкүргөндө, жөтөлгөндө, '
        '\nчимкиргенде, тамак даярдаганда, таштандыларды чыгарганда, жаныбарларды сылаганда жана көчөдөн келгенде.',
        'Эгерде самын жок болсо, кир кол менен жүрбөстөн,  колду жууганы артык. Колду 20 секундадан бир мүнөтко чейинки убакытта жуугула. Эң негизи - андан аз болбосун.',
        'Колду кургак же кагаз сүлгү менен аарчыгыла. Кургаткычты колдонуу - колдонбогондон артык.',
        'Кол жууш убагы. Колду кийимге аарчыганы же такыр аарчыбаганы  ишти жокко чыгарат. '
        '\nКол жууган жай болбосо, антисептикти колдонгула.',
        'Кол жууш мезгили. Бактериялардын көбүнчөсү бармактын учунда жана тырмактардын астында жайгашат. '
        '\nКолду ичинен жана сыртынан, бармактардын ортосунан жууш керек, жана тырмак астында жууганга аракет кылыш керек.'
    ]
    return random.choice(text)


@bot.message_handler(commands=['start'])
def welcome(m):
    if m.chat.id in cfg.users:
        pass
    else:
        cfg.users[m.chat.id] = {'lang': 'eng', 'work': False, 'say': 0}
        bot.send_message(m.chat.id, 'Выберите язык', reply_markup=Langs)
        print('New user:', m.from_user.first_name, m.from_user.last_name, 'nick:', m.from_user.username)


@bot.message_handler(content_types=['text'])
def answers(m):
    def func_thread():
        if m.text == 'English 🇬🇧':
            cfg.users[m.chat.id]['lang'] = 'eng'
            bot.send_message(m.chat.id, 'Choose time', reply_markup=time_Eng)
        elif m.text == 'Русский 🇷🇺':
            cfg.users[m.chat.id]['lang'] = 'rus'
            bot.send_message(m.chat.id, 'Выберите время', reply_markup=time_Rus)
        elif m.text == 'Кыргызча 🇰🇬':
            cfg.users[m.chat.id]['lang'] = 'kgz'
            bot.send_message(m.chat.id, 'Убакытты тандаңыз', reply_markup=time_Kgz)
        if m.text == '30':
            cfg.users[m.chat.id]['say'] = 30
            cfg.users[m.chat.id]['work'] = True
        if m.text == '60':
            cfg.users[m.chat.id]['say'] = 60
            cfg.users[m.chat.id]['work'] = True
        if m.text == 'Stop' or m.text == 'Остановить' or m.text == 'Токтотуу':
            cfg.users[m.chat.id]['work'] = False
            if m.text == 'Stop':
                bot.send_message(m.chat.id, 'Stopped!', reply_markup=Langs)
            elif m.text == 'Остановить':
                bot.send_message(m.chat.id, 'Остановлено!', reply_markup=Langs)
            elif m.text == 'Токтотуу':
                bot.send_message(m.chat.id, 'Токтотулду!', reply_markup=Langs)
        if 22 <= int(time.strftime('%H')) <= 7:
            pass
        else:
            while cfg.users[m.chat.id]['work'] == True:
                if cfg.users[m.chat.id]['lang'] == 'rus':
                    if m.text == '30':
                        bot.send_message(m.chat.id, random_rus_30m())
                        time.sleep(1800)
                    elif m.text == '60':
                        bot.send_message(m.chat.id, random_rus_1h())
                        time.sleep(3600)
                elif cfg.users[m.chat.id]['lang'] == 'kgz':
                    if m.text == '30':
                        bot.send_message(m.chat.id, random_kgz_30m())
                        time.sleep(1800)
                    if m.text == '60':
                        bot.send_message(m.chat.id, random_kgz_30m())
                        time.sleep(3600)
                elif cfg.users[m.chat.id]['lang'] == 'eng':
                    if m.text == '30':
                        bot.send_message(m.chat.id, random_eng_30m())
                        time.sleep(1800)
                    if m.text == '60':
                        bot.send_message(m.chat.id, random_eng_1h())
                        time.sleep(3600)

    if __name__ == '__main__':
        Thread(target=func_thread).start()

try:
    bot.polling(none_stop=True, interval=0, timeout=60)
except Exception as E:
    print(E)