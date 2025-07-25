import telebot
from bot_logic import gen_pass, gen_emodji, flip_coin
from model2 import get_class

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("7812854680:AAHvmQHc_lyPJ3OpVMna-JX_Jzsv8jIlEmE")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши команду /hello, /bye, /pass, /emodji или /coin /donlo ")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['pass'])
def send_password(message):
    password = gen_pass(10)  # Устанавливаем длину пароля, например, 10 символов
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")

@bot.message_handler(commands=['emodji'])
def send_emodji(message):
    emodji = gen_emodji()
    bot.reply_to(message, f"Вот эмоджи': {emodji}")

@bot.message_handler(commands=['coin'])
def send_coin(message):
    coin = flip_coin()
    bot.reply_to(message, f"Монетка выпала так: {coin}")

@bot.message_handler(content_types=["photo"])  # Исправлено "donlo" на "photo"
def send_donlo(message):
    if not message.photo:
        return bot.send_message(message.chat.id, "Вы не загрузили картинку")  # Добавлен .chat.id
    
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1] 

    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    result = get_class(file_name)
    if result == 'minecraft':
        bot.send_message(message, 'Значит ты в маин играешь, попробуй поиграть с друзьями, так будет веселее')  # Добавлен .chat.id и форматирование текста

    if result == 'age of history':  # Исправлено опечатку в "age os history"
        bot.send_message(message, 'О, ты играешь, получается. В это советую создать там СССР за Приднестровье')  # Добавлен .chat.id и форматирование

    if result == 'roblox':
        bot.send_message(message, 'Ты играешь в Роблокс? Если да и любишь хойку, то заходи в режим Control Europe')  # Добавлен .chat.id и форматирование
    
    bot.send_message(message, result)  # Добавлен .chat.id

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Запускаем бота
bot.polling()
