import telebot
from telebot import types
import random
from time import sleep
import requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import configparser
from player import Player
#import exodia
from smallgames import hangman

bot = telebot.TeleBot('1322322473:AAEqIreqjYCOaTzdXBUoxj8f_BB1FiteIVo')

#@bot.message_handler(commands=['start'])
#def start(message):
#    keyboard1 = [InlineKeyboardButton("Church", callback_data='Church')]
#    keyboard2 = [InlineKeyboardButton("Square", callback_data='Square')]
#    keyboard3 = [InlineKeyboardButton("Market", callback_data='Market')]
    
# create reply keyboard markup
#    reply_markup = InlineKeyboardMarkup([keyboard1, keyboard2, keyboard3])    # send message with text and appended inline keyboard
#    bot.send_message(message.chat.id,"Where would you like to go?",reply_markup=reply_markup)
#    query_handler(call)


#@bot.callback_query_handler(func=lambda call: True)
#def query_handler(call):
#    bot.answer_callback_query(callback_query_id=call.id, text='Moving to '+call.data)
#    
#    keyboard1 = [InlineKeyboardButton("Pray", callback_data='p')]
#    keyboard2 = [InlineKeyboardButton("Run", callback_data='r')]
#    keyboard3 = [InlineKeyboardButton("Sleep", callback_data='s')]
    
# create reply keyboard markup
#    reply_markup = InlineKeyboardMarkup([keyboard1, keyboard2, keyboard3])    # send message with text and appended inline keyboard
#    bot.send_message(call.message.chat.id,"What are going to do now?",reply_markup=reply_markup)
    #bot.send_message(call.message.chat.id, "teste")
#    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
#    query_handler2(call)

#def query_handler2(call):
#    bot.answer_callback_query(callback_query_id=call.id, text='Answer accepted!')
#    if call.data == 'p':
#        bot.send_message(call.message.chat.id, "Praying huh?")
#        print(call.message.message_id)
#        print(call.message.chat.id)
#        #bot.delete_message(call.message.chat.id, call.message.message_id)
#        print('passou')


oasis_getmes = {}
def get_the_file():
    a_file = open("/home/gta/Desktop/danyel/bot/arquivos-bot/getmes.txt")
    for line in a_file:
        key, value = line.split()
    #Split line into a tuple
        oasis_getmes[key] = value
    #Add tuple values to dictionary
    print(oasis_getmes)


@bot.message_handler(commands=['start'])
def start_main_menu(message):
    get_the_file()
    if message.chat.first_name in oasis_getmes:
        #for x, y in oasis_getmes.items():
        #            bot.send_message(message.chat.id, x)
        #            bot.send_message(message.chat.id, y)
        #            bot.send_message(message.chat.id, "----------------")
        main_keyboard = types.InlineKeyboardMarkup(row_width=1)
        first_button = types.InlineKeyboardButton(text="Church", callback_data="church")
        second_button = types.InlineKeyboardButton(text="Square", callback_data="square")
        third_button = types.InlineKeyboardButton(text="Market", callback_data="market")
        main_keyboard.add(first_button, second_button, third_button)
        bot.send_message(message.chat.id, "Where would you like to go?", reply_markup=main_keyboard)
    else:
        bot.send_message(message.chat.id, "Your entry to Oasis is prohibited.\n"+"_The future is Oasis_", parse_mode="Markdown")
        #for x, y in oasis_getmes.items():
        #            bot.send_message(message.chat.id, x)
        #            bot.send_message(message.chat.id, y)
        #            bot.send_message(message.chat.id, "----------------")
@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == "main_menu":
        bot.answer_callback_query(callback_query_id=call.id, text='Menu')
        main_keyboard = types.InlineKeyboardMarkup(row_width=1)
        first_button = types.InlineKeyboardButton(text="Church", callback_data="church")
        second_button = types.InlineKeyboardButton(text="Square", callback_data="square")
        third_button = types.InlineKeyboardButton(text="Market", callback_data="market")
        main_keyboard.add(first_button, second_button, third_button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Where would you like to go?",reply_markup=main_keyboard)

    if call.data == "church":
        bot.answer_callback_query(callback_query_id=call.id, text='You are in the Church!')
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        button1 = types.InlineKeyboardButton(text="Pray", callback_data="pray")
        button2 = types.InlineKeyboardButton(text="Beg for money", callback_data="beg")
        button3 = types.InlineKeyboardButton(text="Sleep", callback_data="sleep")
        back_button = types.InlineKeyboardButton(text="Back", callback_data="main_menu")
        keyboard.add(button1, button2, button3, back_button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="You are in the Church",reply_markup=keyboard)

    elif call.data == "square":
        bot.answer_callback_query(callback_query_id=call.id, text='You are in the Square!')
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        button1 = types.InlineKeyboardButton(text="Meet someone", callback_data="meet")
        button2 = types.InlineKeyboardButton(text="The Tournament", callback_data="tournament")
        button3 = types.InlineKeyboardButton(text="Relax", callback_data="relax")
        back_button = types.InlineKeyboardButton(text="Back", callback_data="main_menu")
        keyboard.add(button1, button2, button3, back_button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="You are in the Square",reply_markup=keyboard)



    elif call.data == "market":
        bot.answer_callback_query(callback_query_id=call.id, text='You are in the Market!')
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        button1 = types.InlineKeyboardButton(text="Buy new Gear", callback_data="buy")
        button2 = types.InlineKeyboardButton(text="Buy food", callback_data="food")
        button3 = types.InlineKeyboardButton(text="Stole somene", callback_data="stole")
        back_button = types.InlineKeyboardButton(text="Back", callback_data="main_menu")
        keyboard.add(button1, button2, button3, back_button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="You are in the Market",reply_markup=keyboard)


    elif call.data == "tournament":
        bot.send_message(call.message.chat.id, "_It's a simple tournament. Pay 500 gold and you may win 3000 gold if you kill everyone_", parse_mode="Markdown")
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        button1 = types.InlineKeyboardButton(text="Join", callback_data="join")
        button2 = types.InlineKeyboardButton(text="Deny", callback_data="deny")
        button3 = types.InlineKeyboardButton(text="Watch", callback_data="watch")
        back_button = types.InlineKeyboardButton(text="Back", callback_data="main_menu")
        keyboard.add(button1, button2, button3, back_button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="*You are reading the tournament rules*",reply_markup=keyboard,parse_mode="Markdown")


    elif call.data == "join":
        bot.answer_callback_query(callback_query_id=call.id, text='_You lost 500 gold_', show_alert=True)
        #bot.send_message(call.message.chat.id, "_You lost 500 gold_", parse_mode="Markdown") 
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="_You joined the tournament. Be sure you read the rules:_",parse_mode="Markdown",reply_markup=None)


    #elif call.data == "1" or call.data == "2" or call.data == "3":
    #    bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="alert")
    #    keyboard3 = types.InlineKeyboardMarkup()
    #    button = types.InlineKeyboardButton(text="lastlayer", callback_data="ll")
    #    keyboard3.add(button)
    #    bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="last layer",reply_markup=keyboard3)

    

#============================================================================================================

#============================================================================================================


print('The future is Oasis')
bot.polling()
