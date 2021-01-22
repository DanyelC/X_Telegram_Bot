import telebot
from telebot import types
import random
from time import sleep
import requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import configparser
from player import Player
from smallgames import hangman

bot = telebot.TeleBot('1322322473:AAEqIreqjYCOaTzdXBUoxj8f_BB1FiteIVo')

@bot.message_handler(commands=['start'])
def start(message):
    keyboard1 = [InlineKeyboardButton("Church", callback_data='Church')]
    keyboard2 = [InlineKeyboardButton("Square", callback_data='Square')]
    keyboard3 = [InlineKeyboardButton("Market", callback_data='Market')]
    
# create reply keyboard markup
    reply_markup = InlineKeyboardMarkup([keyboard1, keyboard2, keyboard3])    # send message with text and appended inline keyboard
    bot.send_message(message.chat.id,"Where would you like to go?",reply_markup=reply_markup)
    query_handler(call\)


#@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Moving to '+call.data)
    
    keyboard1 = [InlineKeyboardButton("Pray", callback_data='p')]
    keyboard2 = [InlineKeyboardButton("Run", callback_data='r')]
    keyboard3 = [InlineKeyboardButton("Sleep", callback_data='s')]
    
# create reply keyboard markup
    reply_markup = InlineKeyboardMarkup([keyboard1, keyboard2, keyboard3])    # send message with text and appended inline keyboard
    bot.send_message(call.message.chat.id,"What are going to do now?",reply_markup=reply_markup)
    #bot.send_message(call.message.chat.id, "teste")
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    query_handler2(call)

def query_handler2(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Answer accepted!')
    if call.data == 'p':
        bot.send_message(call.message.chat.id, "Praying huh?")
        print(call.message.message_id)
        print(call.message.chat.id)
        #bot.delete_message(call.message.chat.id, call.message.message_id)
        print('passou')


#============================================================================================================

#============================================================================================================

@bot.message_handler(content_types=["text"])
def any_msg(message):
    keyboardmain = types.InlineKeyboardMarkup(row_width=2)
    first_button = types.InlineKeyboardButton(text="1button", callback_data="first")
    second_button = types.InlineKeyboardButton(text="2button", callback_data="second")
    keyboardmain.add(first_button, second_button)
    bot.send_message(message.chat.id, "testing kb", reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == "mainmenu":

        keyboardmain = types.InlineKeyboardMarkup(row_width=2)
        first_button = types.InlineKeyboardButton(text="1button", callback_data="first")
        second_button = types.InlineKeyboardButton(text="2button", callback_data="second")
        keyboardmain.add(first_button, second_button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="menu",reply_markup=keyboardmain)

    if call.data == "first":
        keyboard = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="1t", callback_data="1")
        rele2 = types.InlineKeyboardButton(text="2t", callback_data="2")
        rele3 = types.InlineKeyboardButton(text="3t", callback_data="3")
        backbutton = types.InlineKeyboardButton(text="back", callback_data="mainmenu")
        keyboard.add(rele1, rele2, rele3, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="replaced text",reply_markup=keyboard)

    elif call.data == "second":
        keyboard = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="another layer", callback_data="gg")
        backbutton = types.InlineKeyboardButton(text="back", callback_data="mainmenu")
        keyboard.add(rele1,backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="replaced text",reply_markup=keyboard)

    elif call.data == "1" or call.data == "2" or call.data == "3":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="alert")
        keyboard3 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="lastlayer", callback_data="ll")
        keyboard3.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="last layer",reply_markup=keyboard3)


#============================================================================================================

#============================================================================================================


print('The future is Oasis')
bot.polling()