import telebot
from bot_logic import gen_pass, gen_emodji, flip_coin
from model2 import get_class

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("7812854680:AAHq8gMVLTenXYpZhbxW_b4yTXOl4o7mOdE")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message.chat.id, "Привет! Я твой Telegram бот. Напиши команду /hello, /bye, /pass, /emodji или /coin  ")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message.chat.id, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message.chat.id, "Пока! Удачи!")

@bot.message_handler(commands=['pass'])
def send_password(message):
    password = gen_pass(10)  # Устанавливаем длину пароля, например, 10 символов
    bot.reply_to(message.chat.id, "Вот твой сгенерированный пароль: {password}")

@bot.message_handler(commands=['emodji'])
def send_emodji(message):
    emodji = gen_emodji()
    bot.reply_to(message.chat.id, "Вот эмоджи': {emodji}")

@bot.message_handler(commands=['coin'])
def send_coin(message):
    coin = flip_coin()
    bot.reply_to(message.chat.id, f"Монетка выпала так: {coin}")

@bot.message.photo(commands=['donlo'])
def send_donlo(message):
    if not message.photo:
        return bot.send_message(message.chat.id, "Вы не загрузили картинку")
    
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1] 

    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    result = get_class(file_name)
    if result == 'minecraft':
        print('Значит ты в маин играешь попробуй поиграть с друзьями так будет веселее')

    if result == 'age os history':
        print('О ты играешь получается в это советаю создать там ссср за приднестровье')

    if result == 'roblox':
        print('Ты играешь в роблокс? Если да и любишь хойку то заходи в режим Control Erope')
    bot.send_message(message.chat.id, result)

# Запускаем бота
bot.polling()