import telebot
from telebot import types
import time
import random
import misc

token = misc.token
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        '''Добро пожаловать.\nПолезные команды для навигации:\nДля выхода в главное меню напишите /end или /start
        ''',
        reply_markup=start_keyboard())


@bot.message_handler(content_types=["text"])
def send_anytext(message):
    chat_id = message.chat.id
    if message.text == 'English':
        bot.send_message(chat_id, 'Вы выбрали язык English', reply_markup=eng_lang())
    elif message.text == 'Русский':
        bot.send_message(chat_id, 'Вы выбрали язык Русский', reply_markup=rus_lang())
    elif message.text == 'Кыргызча':
        bot.send_message(chat_id, 'Вы выбрали язык Кыргызча', reply_markup=kgz_lang())
    elif message.text == '🔙':
        bot.send_message(chat_id, 'Вы вышли в меню выбора', reply_markup=start_keyboard())
    elif message.text == '/end':
        bot.send_message(chat_id, 'Вы вышли в главное меню', reply_markup=start_keyboard())

    # if message.text == 'Остановить':
    #     s = start_timer_30m + 1
    #     # break
    #     return s

    # i = True
    # if message.text == 'Напомни через 30 минут':
    #     while i:
    #         time.sleep(5)
    #         bot.send_message(chat_id, '{}'.format(random_rus_30m()), reply_markup=start_stop_button_rus())
    #         if message.text == 'Остановить':
    #             return bot.send_message(chat_id, 'Вы остановили бот', reply_markup=rus_lang())

    while True:
        if message.text == 'Напомни через 30 минут':
            time.sleep(5)
            bot.send_message(chat_id, '{}'.format(random_rus_30m()), reply_markup=start_stop_button_rus())
        elif message.text == 'Остановить':
            break
    # if message.text == 'Остановить':
    #     return bot.send_message(chat_id, 'Вы остановили бот', reply_markup=rus_lang())

    # while message.text == 'Напомни через 1 час':
    #     time.sleep(9)
    #     return bot.send_message(chat_id, '{}'.format(random_rus_1h()), reply_markup=start_stop_button_rus())
    # if message.text != 'Напомни через 1 час':
    #     break
    # if message.text == 'Остановить':
    #     return i + 5, bot.send_message(chat_id, 'Вы остановили бот', reply_markup=rus_lang())


def start_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True, resize_keyboard=True)
    markup.add('English', 'Русский', 'Кыргызча')
    return markup


def rus_lang():
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=False, resize_keyboard=True)
    markup.add('Напомни через 30 минут', 'Напомни через 1 час', '🔙')
    return markup


def kgz_lang():
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=False, resize_keyboard=True)
    markup.add('30 мүнөттөн кийин эскерт', '1 сааттан кийин эскерт', '🔙')
    return markup


def eng_lang():
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=False, resize_keyboard=True)
    markup.add('Remind after 30 minutes', 'Remind after 1 hour', '🔙')
    return markup


def start_stop_button_eng():
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=False, resize_keyboard=True)
    markup.add('Stop', '🔙')
    return markup


def start_stop_button_rus():
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=False, resize_keyboard=True)
    markup.add('Остановить', '🔙')
    return markup


def start_stop_button_kgz():
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=False, resize_keyboard=True)
    markup.add('Токтотуу', '🔙')
    return markup


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


if __name__ == "__main__":
    bot.polling(none_stop=True)
