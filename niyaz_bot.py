import telebot, os 
from telebot import types 
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))

 
@bot.message_handler(commands=['start']) 
def send_welcome(message): 
    markup = types.ReplyKeyboardMarkup(row_width=2) 
    itembtn1 = types.KeyboardButton('iPhone') 
    itembtn2 = types.KeyboardButton('Samsung') 
    markup.add(itembtn1, itembtn2) 
     
    bot.send_message(message.chat.id, "Выберите марку телефона:", reply_markup=markup) 
 
@bot.message_handler(func=lambda message: True) 
def echo_all(message): 
    if message.text == 'iPhone': 
        bot.send_message(message.chat.id, "Вы выбрали iPhone") 
    elif message.text == 'Samsung': 
        bot.send_message(message.chat.id, "Вы выбрали Samsung") 
    else: 
        bot.send_message(message.chat.id, "Пожалуйста, воспользуйтесь кнопками для выбора марки телефона") 
 
bot.polling(none_stop = True, interval = 0)