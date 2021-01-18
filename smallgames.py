import telebot
import configparser
import random

config = configparser.ConfigParser()
config.sections()
config.read('exodia_bot.conf')
bot = telebot.TeleBot(config['DEFAULTS']['bot_token'])

def hangman(message):
    #markup = types.ReplyKeyboardMarkup(one_time_keyboard= True)
    #um = types.KeyboardButton('')
    #dois = types.KeyboardButton('')
    #tres = types.KeyboardButton('')
    #quatro = types.KeyboardButton('')
    #cinco = types.KeyboardButton('')
    #seis = types.KeyboardButton('')
    #sete = types.KeyboardButton('')
    #oito = types.KeyboardButton('')
    #nove = types.KeyboardButton('')
    #markup.row(um, dois, tres)
    #markup.row(quatro, cinco, seis)
    #markup.row(sete, oito, nove)
    #animal_keyboard = bot.send_message(message.chat.id, "It is dangerous to go alone, choose one :", reply_markup=markup)
    words = ["teste", "exodia", "alma", "amizade"]
    bot.send_message(message.chat.id, "lets play hangman!")
    x = words[random.randint(0, len(words)-1)]
    y=len(x)*"-"
    print(x,y)

    chute = bot.send_message(message.chat.id, "guess the word")
    bot.register_next_step_handler(chute , right_or_not, x)

    def right_or_not(message):
        if message.text in x:
            bot.send_message(message.chat.id, "boa")
    