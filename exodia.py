# -*- coding: utf-8 -*-
import telebot
from telebot import types
import random
from time import sleep
import requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import configparser
from player import Player
from smallgames import hangman

from secrets import TOKEN
import dropbox
dbx = dropbox.Dropbox(TOKEN)

    
#para usar outros arquivos, chamar com import
config = configparser.ConfigParser()
config.sections()
config.read('exodia_bot.conf')
bot = telebot.TeleBot(config['DEFAULTS']['bot_token'])


getmes={}
ungetmes={}
contagem={}
animals={}
players={}
#personalites={} esta no player.py
Danyel= 847307875
sobre = "This bot was developed and created by Danyel Clinário. It is still in the testing phase, any \
suggestion is welcome! Write me!"
#path = '/home/gta/Desktop/danyel/bot/' EXCLUIDO PARA RODAR NO HEROKU


#========================================= Dropbox =========================================
file="/app/arquivos-bot/getmes.txt"
file_location = "/xexodiabot/example.txt"
file_location2 = "/xexodiabot/data/"
fgetmes=file_location2+"getmes.txt"
fungetmes=file_location2+"ungetmes.txt"
fanimals=file_location2+"animals.txt"
fplayers=file_location2+"players.txt"
fpersonalities=file_location2+"personalities.txt"


def upload_file(dbx, file_location,file):
    with open(file,"rb") as f:
        dbx.files_upload(f.read(),file_location,mode=dropbox.files.WriteMode.overwrite)

#upload_file(dbx,file_location,file)


def create_file(dbx, file_location,file,anything):
    with open(file,"rb") as f:
        dbx.files_upload(anything,file_location,mode=dropbox.files.WriteMode("overwrite"))


def create_file_dict(dbx,file_location,dicio):
  arrayo=""
  for x, y in dicio.items():
    arrayo+=(str(x)+" "+ str(y)+'\n')
  arrayo = arrayo.encode()
  #with open(file,"rb") as f:
  dbx.files_upload(arrayo,file_location,mode=dropbox.files.WriteMode("overwrite"))


def create_file_data(dbx,file_location,data):
  #with open(file,"rb") as f:
  dbx.files_upload(data,file_location,mode=dropbox.files.WriteMode("overwrite"))

def download_file(filename):
    """
    Get file from Dropbox
    :param filename: full path of the file
    :return:
    """
    print(f"filename {filename}")

    f, r = dbx.files_download(filename)

    content = r.content

    return content

#=============================================================================================

# Handles all text messages that contains the command '/start'
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, 'Hey! '+"\U0001F601")

    if message.chat.type == "private":
        bot.send_message(message.chat.id, 'Hello, '+ message.chat.first_name +'. My name is Exodia. How can I help you?')
        bot.send_chat_action(message.chat.id, "typing")
        bot.send_chat_action(message.chat.id, "typing")
        handle_getme(message)
        bot.send_chat_action(message.chat.id, "typing")
        bot.send_chat_action(message.chat.id, "typing")
        bot.send_message(message.chat.id, "Would like to see the menu? You just need to click here: /menu")
        bot.send_chat_action(message.chat.id, "typing")
        bot.send_chat_action(message.chat.id, "typing")
        if message.chat.type == "group":
            if str('Group: '+message.chat.title) in animals:
                bot.send_message(message.chat.id, "You already have your friend")
        elif str(message.chat.first_name) in animals:
                bot.send_message(message.chat.id, "You already have your friend")
        else:
            bot.send_message(message.chat.id, "But before starting...")
            handle_choose_animal(message)
            

    else:   
        bot.send_message(message.chat.id, 'Hello people from '+ message.chat.title +' group. My name is Exodia. How can I help you?')
        bot.send_chat_action(message.chat.id, "typing")
        bot.send_chat_action(message.chat.id, "typing")
        handle_getme(message)
        bot.send_chat_action(message.chat.id, "typing")
        bot.send_chat_action(message.chat.id, "typing")
        bot.reply_to(message, "Would like to see the menu? You just need to click here: /menu")
        bot.send_chat_action(message.chat.id, "typing")
        bot.send_chat_action(message.chat.id, "typing")
        bot.send_message(message.chat.id, "But before starting...")
        handle_choose_animal(message)

    
    

# Handles all text messages that contains the command '/help'.
@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.reply_to(message, "How can I help you?")
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id,
        '1) /menu - The list of all my 10 commands\n' +
        '2) /start - Get started about the game (under development)\n' +
        '3) /help - Questions and answers about the game (under development)\n' +
        #'4) /getme - Subscribe to create your account and get some news!\n' +
        '4) /about - Contact my creator!\n'+
        "5) /play - Let's play some dices! \n" +
        '6) /score - I can show you our score \n' +
        '7) /stop - Delete your account (under development) \n' +
        '8) /myfriend - Details about your friend (under development)\n' +
        '9) /status - Your status\n'+
        '10) /rank - Are you the Chosen One?\n'+
        #'10) Show me the Keyboard - not a command but something you should type\n'+
        'Future features:\n'+
        'Coming soon!\n')  



# Getting your chat id
#@bot.message_handler(commands=['getme'])
def handle_getme(message):
    if message.chat.type == "private":
        if message.chat.first_name in getmes:
            bot.reply_to(message, "I already have your chat id for further interactions")
        else:
            getmes[str(message.chat.first_name)]=str(message.chat.id)
            with open('arquivos-bot/getmes.txt','a') as new_file:
            #with open(path+'arquivos-bot/getmes.txt','a') as new_file:
                new_file.write(str(message.chat.first_name)+" "+str(message.chat.id)+'\n')
                create_file_dict(dbx,fgetmes,getmes)#######################################################################
            bot.send_message(Danyel, "XXX-ADMIM-MESSAGE-XXX: Someone just subscribed! "+message.chat.first_name+ " joined")
            bot.reply_to(message, "I just saved your chat id for further interactions")

    
    if message.chat.type == "group":
        if message.chat.title in getmes:
            bot.reply_to(message, "I already have your chat id for further interactions")
        else:
            getmes[str(message.chat.title)]=str(message.chat.id)
            with open('arquivos-bot/getmes.txt','a') as new_file:
            #with open(path+'arquivos-bot/getmes.txt','a') as new_file:
                new_file.write('Group '+str(message.chat.title)+" "+str(message.chat.id)+'\n')
            bot.send_message(Danyel, "*XXX-ADMIM-MESSAGE-XXX*: Someone just subscribed! "+message.chat.title+ " joined", parse_mode= 'Markdown')
            bot.reply_to(message, "I just saved your chat id for further interactions")



# Handles all text messages that contains the command '/about'.
@bot.message_handler(commands=['about'])
def handle_about(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_chat_action(message.chat.id, "typing")
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Message the developer', url ='telegram.me/X_Oasis_Bot')) #url='telegram.me/DanyelC'))
    bot.send_message(message.chat.id,sobre,reply_markup=keyboard)
    


# Handles all text messages that contains the command '/play', '/score'. '/hangman is not activated'.
@bot.message_handler(commands=['play', 'score','hangman'])
def handle_play_score(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_chat_action(message.chat.id, "typing")
    if message.text == "/score":
            if str(message.chat.first_name) in contagem:
                bot.reply_to(message, "Your score is %d and mine is %d" % (contagem[str(message.chat.first_name)], contagem[str(message.chat.first_name)+'Exodia']))
            else: 
                bot.reply_to(message, "We haven't played ... yet. Lets play now! Click here: /play")
    
    #elif message.text == "/hangman":
    #    tictactoe[str(message.chat.first_name)]= hangman(message)


    elif message.text == "/play":
        _1 = random.randint(1, 6)
        _2 = random.randint(1, 6)
        _3 = random.randint(1, 6)
        _4 = random.randint(1, 6)
        _5 = random.randint(1, 6)
        _6 = random.randint(1, 6)
        bot.reply_to(message, "OK! Let me roll the dice")
        bot.send_chat_action(message.chat.id, "typing")
        bot.send_message(message.chat.id, 'You have ' + str(_1) + ' and ' + str(_2) + ' and ' + str(_3) + ' !\n Your result is ' + str(_1 + _2 + _3) + '!!!')
        bot.send_chat_action(message.chat.id, "typing")
        bot.send_chat_action(message.chat.id, "typing")
        bot.send_message(message.chat.id, 'I have ' + str(_4) + ' and ' + str(_5) + ' and ' + str(_6) + ' !\n My result is ' + str(_4 + _5 + _6) + '!!!')
        if message.chat.type == "private": 
            if _1 + _2 + _3 == _4 + _5 + _6: torneio= "Nobody won, sorry"
            if _1 + _2 + _3 > _4 + _5 + _6: 
                torneio = "You won...shit"
                if str(message.chat.first_name) in contagem:
                    contagem[str(message.chat.first_name)]+=1
                else:
                    contagem[str(message.chat.first_name)]=1
                    contagem[str(message.chat.first_name)+'Exodia'] = 0
            if _1 + _2 + _3 < _4 + _5 + _6: 
                torneio = "I won!!!"
                if str(message.chat.first_name)+'Exodia' in contagem:
                    contagem[str(message.chat.first_name)+'Exodia']+=1
                else: 
                    contagem[str(message.chat.first_name)+'Exodia'] = 1
                    contagem[str(message.chat.first_name)]=0
            bot.send_chat_action(message.chat.id, "typing")
            bot.send_chat_action(message.chat.id, "typing")
            bot.send_message(message.chat.id,torneio)
            bot.send_chat_action(message.chat.id, "typing")
            bot.send_chat_action(message.chat.id, "typing")
            if torneio!="Nobody won, sorry":
                bot.send_chat_action(message.chat.id, "typing")
                bot.send_message(message.chat.id, "Your score is %d and mine is %d" % (contagem[str(message.chat.first_name)], contagem[str(message.chat.first_name)+'Exodia']))
            bot.send_message(message.chat.id, "Let's play again? /play")
            #atualizando o score:
            if players[str(message.chat.id)]:
                score = int(contagem[str(message.chat.first_name)]) - int(contagem[str(message.chat.first_name)+'Exodia'])
                players[str(message.chat.id)].Score = score 

        elif message.chat.type == "group":
            if _1 + _2 + _3 == _4 + _5 + _6: torneio= "Nobody won, sorry"
            if _1 + _2 + _3 > _4 + _5 + _6: 
                torneio = "You won...shit"
                if str(message.chat.title) in contagem:
                    contagem[str(message.chat.title)]+=1
                else:
                    contagem[str(message.chat.title)]=1
                    contagem[str(message.chat.title)+'Exodia'] = 0
            if _1 + _2 + _3 < _4 + _5 + _6: 
                torneio = "I won!!!"
                if str(message.chat.title)+'Exodia' in contagem:
                    contagem[str(message.chat.title)+'Exodia']+=1
                else: 
                    contagem[str(message.chat.title)+'Exodia'] = 1
                    contagem[str(message.chat.title)]=0
            bot.send_chat_action(message.chat.id, "typing")
            bot.send_chat_action(message.chat.id, "typing")
            bot.send_message(message.chat.id,torneio)
            bot.send_chat_action(message.chat.id, "typing")
            bot.send_chat_action(message.chat.id, "typing")
            if torneio!="Nobody won, sorry":
                bot.send_message(message.chat.id, "Your score is %d and mine is %d" % (contagem[str(message.chat.title)], contagem[str(message.chat.title)+'Exodia']))
            bot.send_message(message.chat.id, "Let's play again? /play")
            #atualizando o score:
            if players[str(message.chat.id)]:
                score = int(contagem[str(message.chat.title)]) - int(contagem[str(message.chat.title)+'Exodia'])
                players[str(message.chat.id)].Score = score 

            
    
        
        
    
# Handles all text messages that contains the command '/stop'.
@bot.message_handler(commands=['stop'])
def handle_stop(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_chat_action(message.chat.id, "typing")
    bot.reply_to(message, "Don't worry! I won't write you again (except if you write me hahaha)")
    if message.chat.type == "private":
        if str(message.chat.first_name) in getmes:
            ungetmes[str(message.chat.first_name)] = getmes[str(message.chat.first_name)]
            name = str(message.chat.first_name)
            cid = str(message.chat.id)
            with open('arquivos-bot/ungetmes.txt','a') as new_file: 
            #with open(path+'arquivos-bot/ungetmes.txt','a') as new_file: 
                new_file.write(name+': '+ cid+'\n')
            del getmes[str(message.chat.first_name)]
            bot.send_chat_action(message.chat.id, "typing")
            bot.send_message(message.chat.id, "Your chat id was deleted, but your friend still here, waiting for you \U0001F97A")
            bot.send_message(message.chat.id, "To change your friend, type /myfriend")

        else:
            bot.send_message(message.chat.id, "Your chat id is not saved")
    elif message.chat.type == "group":
        if str(message.chat.title) in getmes:
            ungetmes[str(message.chat.title)]=getmes[str(message.chat.title)]
            title = str(message.chat.title)
            cid = str(message.chat.id)
            with open('arquivos-bot/ungetmes.txt','a') as new_file:
            #with open(path+'arquivos-bot/ungetmes.txt','a') as new_file:
                new_file.write('Group '+title+": "+cid+'\n')
            del getmes[str(message.chat.title)]
            bot.send_chat_action(message.chat.id, "typing")
            bot.send_message(message.chat.id, "Your chat id was deleted, but your friend still here, waiting for you \U0001F97A")
        else:
            bot.send_chat_action(message.chat.id, "typing")
            bot.send_message(message.chat.id, "Your chat id is not saved")


#======================================ADMIN======================================== 

@bot.message_handler(commands=['contagem'])
def handle_admin_contagem(message):
    f = open('arquivos-bot/ungetmes.txt','w')
    #f = open(path+'arquivos-bot/ungetmes.txt','w')
    if message.chat.id == Danyel:
        if message.chat.first_name == 'Danyel' or 'Xaxaxa':
            if contagem:
                for x, y in contagem.items():
                    bot.send_message(message.chat.id, str(x)+": "+str(y))
                    bot.send_message(message.chat.id, "----------------")
                    f.write(str(x)+": "+str(y)+'\n')
                    f.write('----------------\n')
            else: bot.send_message(message.chat.id, "Nothing, Sir")



@bot.message_handler(commands=['animals'])
def handle_admin_animals(message):
    if message.chat.id == Danyel:
        if message.chat.first_name == 'Danyel' or 'Xaxaxa':
            if animals:
                for x, y in animals.items():
                    bot.send_message(message.chat.id, x)
                    bot.send_message(message.chat.id, y)
                    bot.send_message(message.chat.id, "----------------")
            else: bot.send_message(message.chat.id, "Nothing, Sir")



@bot.message_handler(commands=['getmes'])
def handle_adminhozinho(message):
    if message.chat.id == Danyel:
        if message.chat.first_name == 'Danyel' or 'Xaxaxa':
            if getmes:
                for x, y in getmes.items():
                    bot.send_message(message.chat.id, x)
                    bot.send_message(message.chat.id, y)
                    bot.send_message(message.chat.id, "----------------")
            else: bot.send_message(message.chat.id, "Nothing, Sir")


@bot.message_handler(commands=['ungetmes'])
def handle_adminhozinho(message):
    if message.chat.id == Danyel:
        if message.chat.first_name == 'Danyel' or 'Xaxaxa':
            if ungetmes:
                for x, y in ungetmes.items():
                    bot.send_message(message.chat.id, x)
                    bot.send_message(message.chat.id, y)
                    bot.send_message(message.chat.id, "----------------")
            else: bot.send_message(message.chat.id, "Nothing, Sir")



@bot.message_handler(commands=['players'])
def handle_player(message):
    if message.chat.id == Danyel:
        if message.chat.first_name == 'Danyel' or 'Xaxaxa':
            if players:
                #for y,x in players:
                #    bot.send_message(Danyel,
                #    x.id +'\n'+
                #    x.score +'\n' +
                #    x.personalidade+'\n'+
                #    #'4) /getme - Subscribe to create your account and get some news!\n' +
                #    x.hp+'\n'+
                #    x.ataque+'\n' +
                #    x.defesa+'\n' +
                #    x.equipamento+'\n' +
                #    x.magia+'\n')
                for jogadores in players:
                    x= players[jogadores].send_all_list()
                    print(x)
                    print(x[0]) # x[0] é "id = xxxx" logo
                    id = x[0].split(" ")
                    id = id[2]
                    print(id)
                    bot.send_message(Danyel, "=========================") 
                    for y in x:
                        bot.send_message(Danyel, y)  


#======================================ADMIN======================================== 

# Handles all text messages that contains the command '/menu'.
@bot.message_handler(commands=['menu'])
def handle_menu(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "A list of commands:")
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_chat_action(message.chat.id, "typing")
    if message.chat.id == Danyel:
        if message.chat.first_name == 'Danyel' or 'Xaxaxa':
            bot.send_message(message.chat.id,
            '1) /menu - The list of all my 10 commands\n' +
            '2) /start - Get started about the game (under development)\n' +
            '3) /help - Questions and answers about the game (under development)\n' +
            #'4) /getme - Subscribe to create your account and get some news!\n' +
            '4) /about - Contact my creator!\n'+
            "5) /play - Let's play some dices! \n" +
            '6) /score - I can show you our score \n' +
            '7) /stop - Delete your account (under development) \n' +
            '8) /myfriend - Details about your friend (under development)\n' +
            '9) /status - Your status\n'+
            '10) /rank - Are you the Chosen One?\n'+
            #'10) Show me the Keyboard - not a command but something you should type\n'+
            'Future features:\n'+
            'Coming soon!\n\n'
            'XXXXX-ADMIN MODE-XXXXX \n\n'+
            #'1) /xaveco\n' +
            #'2) /iamyourfather\n' +
            #'3) /prove\n' +
            '1) /getmes\n' +
            '2) /contagem\n'+
            '3) /animals\n'+
            '4) /ungetmes\n'+
            '5) /players')
    else: bot.send_message(message.chat.id,
        '1) /menu - The list of all my 10 commands\n' +
        '2) /start - Get started about the game (under development)\n' +
        '3) /help - Questions and answers about the game (under development)\n' +
        #'4) /getme - Subscribe to create your account and get some news!\n' +
        '4) /about - Contact my creator!\n'+
        "5) /play - Let's play some dices! \n" +
        '6) /score - I can show you our score \n' +
        '7) /stop - Delete your account (under development) \n' +
        '8) /myfriend - Details about your friend (under development)\n' +
        '9) /status - Your status\n'+
        '10) /rank - Are you the Chosen One?\n'+
        #'10) Show me the Keyboard - not a command but something you should type\n'+
        'Future features:\n'+
        'Coming soon!\n') 
    
#Gets your global ranking
@bot.message_handler(commands=['rank'])
def handle_rank(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id,'*XXXX - UNDER DEVELOPMENT - XXXX*',parse_mode= 'Markdown')
    bot.send_message(message.chat.id, "Wanna see the Global Ranking? I'm not sure if you are strong enough...")
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Are you ready? (Travel to Oasis)', url='telegram.me/X_Oasis_Bot'))
    bot.send_message(message.chat.id,'Go to Oasis and then go to the square, you gonna find what you want (or not)',reply_markup=keyboard)
    #bot.send_message(message.chat.id, "Go to Oasis and then go to the square, you gonna find what you want (or not).")


#Shows your friend and the possibility to change it
@bot.message_handler(commands=['myfriend'])
def handle_myfriend(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_chat_action(message.chat.id, "typing")
    if message.chat.type == "private":
        if str(message.chat.first_name) in animals:
            x = bot.reply_to(message, "Your friend is: "+ animals[message.chat.id])
            
            markup = types.ReplyKeyboardMarkup(one_time_keyboard= True)
            yes = types.KeyboardButton('Yes')
            no = types.KeyboardButton('Obviously no!')
            markup.row( yes, no)

            confirm_change = bot.reply_to(x, "Would you like to choose another one? You are going to spend 1k gold and lose 10 HP ( your friend is going to kick you)", reply_markup=markup)

            bot.register_next_step_handler(confirm_change , step_animal_change)
        else:
            bot.send_message(message.chat.id, "You should choose a friend first. Type /start again")
    elif message.chat.type == "group":
        if str(message.chat.title) in animals:
            x = bot.reply_to(message, "Your friend is: "+ animals[message.chat.title])
            
            markup = types.ReplyKeyboardMarkup(one_time_keyboard= True)
            yes = types.KeyboardButton('Yes')
            no = types.KeyboardButton('Obviously no!')
            markup.row( yes, no)

            confirm_change = bot.reply_to(x, "Would you like to choose another one? You are going to spend 1k gold and lose 10 HP ( your friend is going to kick you)", reply_markup=markup)

            bot.register_next_step_handler(confirm_change , step_animal_change)
        else:
            bot.send_message(message.chat.id, "You should choose a friend first. Type /start again")


def step_animal_change(message):
    answer = message.text
    if answer == "Yes":
        bot.send_chat_action(message.chat.id, "typing")
        bot.send_message(message.chat.id, "kick this idiot!")
        players[str(message.chat.id)].Hp-=10
        sleep(1)
        bot.send_message(message.chat.id, "_"+animals[str(message.chat.first_name)]+" kicked you\n"+"you lost 10 HP_", parse_mode = 'Markdown')
        sleep(1)
        bot.send_message(message.chat.id, "_Exodia grabs your gold_", parse_mode = 'Markdown')
        sleep(1)
        players[str(message.chat.id)].Gold-=1000
        bot.send_message(message.chat.id, "_you lost 1k gold_", parse_mode = 'Markdown')
        bot.send_chat_action(message.chat.id, "typing")
        del animals[str(message.chat.first_name)]
        bot.send_message(message.chat.id, "Ok so, I'm going to take your friend to a new home...")
        bot.send_chat_action(message.chat.id, "typing")
        bot.send_message(message.chat.id, "But first, take this...")
        sleep(1)
        bot.send_message(message.chat.id, "_Exodia punches you_", parse_mode = 'Markdown')
        players[str(message.chat.id)].Hp-=50
        sleep(1)
        bot.send_message(message.chat.id, "_you lost 50 HP_", parse_mode = 'Markdown')
        sleep(1)
        bot.send_message(message.chat.id, "*GIVE ME MORE MONEY!*", parse_mode = 'Markdown')
        players[str(message.chat.id)].Gold-=1000
        sleep(1)
        bot.send_message(message.chat.id, "_you lost 1k gold again_", parse_mode = 'Markdown')
        handle_choose_animal(message)
    else: bot.send_message(message.chat.id, "Ok")



@bot.message_handler(commands=['status'])
def handle_status(message):
    if str(message.chat.id) in players:
        bot.send_message(message.chat.id, "_Thats all you have..._", parse_mode = 'Markdown')
        x = players[str(message.chat.id)].send_all_list()
        del(x[0])
        for y in x:
            bot.send_message(message.chat.id, y )
    else: bot.send_message(message.chat.id, "You don't have anything")



# Handles all photos received
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "*UPLOAD DISABLED*", parse_mode= 'Markdown')
    if message.chat.type == "private":
        bot.reply_to(message, "Nice! I'm going to upload your photo now. Do you want to see some cards?")
        _10 = random.randint(1, 10)
        _10 = str(_10)
        foto= "index"+_10+".jpeg"
        photox = open('fotos-aleatorias/'+foto, 'rb')
        #photox = open(path+'fotos-aleatorias/'+foto, 'rb')
        bot.send_photo(message.chat.id, photox)
        _10 = random.randint(1, 5)
        _10 = str(_10)
        foto= "index"+_10+".jpeg"
        raw = message.photo[1].file_id
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        nome_arq = str(raw)
        with open('arquivos-bot/'+message.chat.first_name+nome_arq,'wb') as new_file:
        #with open(path+'arquivos-bot/'+message.chat.first_name+nome_arq,'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_message(message.chat.id,"Done! I've just downloaded your file, "+message.chat.first_name)



@bot.message_handler(content_types=['document'])
def handle_photo(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "*UPLOAD DISABLED*", parse_mode= 'Markdown')
    if message.chat.type == "private":
        bot.reply_to(message, "Nice! I'm going to upload your document now. Do you want to see some cards?")
        _10 = random.randint(1, 5)
        _10 = str(_10)
        foto= "index"+_10+".jpeg"
        photox = open('fotos-aleatorias/'+foto, 'rb')
        #photox = open(path+'fotos-aleatorias/'+foto, 'rb')
        bot.send_photo(message.chat.id, photox)
        _10 = random.randint(1, 5)
        _10 = str(_10)
        foto= "index"+_10+".jpeg"
        raw = message.document.file_id
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        nome_arq = str(raw)
        with open('arquivos-bot/'+message.chat.first_name+nome_arq,'wb') as new_file:
        #with open(path+'arquivos-bot/'+message.chat.first_name+nome_arq,'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_message(message.chat.id,"Done! I've just downloaded your file, "+message.chat.first_name)

# Handles all videos and audio files
@bot.message_handler(content_types=['audio', 'video'])
def handle_video_audio(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id,"I will ignore it, "+message.chat.first_name)
    #markup = types.InlineKeyboardMarkup()
    #itembtna = types.KeyboardButton('gato')
    #itembtnv = types.KeyboardButton('cachorro')
    #itembtnc = types.KeyboardButton('papagaio')
    #itembtnd = types.KeyboardButton('pato')
    #itembtne = types.KeyboardButton('lagartixa')
    #itembtnkk = types.KeyboardButton('camaleao')
    #markup.row(itembtna, itembtnv, itembtnkk)
    #markup.row(itembtnc, itembtnd, itembtne)
    #bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)
    #sleep(10)
    #if OnCallbackQuery.text == "camaleao":
    #    bot.send_message(message.chat.id, "Nice one")
    #else: print(OnCallbackQuery)


#def get_group(message):
#    bot.send_message(message.chat.id, "hello my dear. write your age:")
#    sleep(5)
#    age = message.text
#    bot.send_message(message.chat.id, "ok")
#    bot.send_message(message.chat.id, "your age is: "+str(age))

#Display the options 
def handle_choose_animal(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard= True)
    catx = types.KeyboardButton('Cat \U0001F408')
    dogx = types.KeyboardButton('Dog \U0001F415')
    parrotx = types.KeyboardButton('Parrot \U0001F99C')
    duckx = types.KeyboardButton('Duck \U0001F986')
    geckox = types.KeyboardButton('Gecko \U0001F98E')
    snakex = types.KeyboardButton('Snake \U0001F40D')
    markup.row(catx, dogx, snakex)
    markup.row(parrotx, duckx, geckox)

    if message.chat.type == "group":
        bot.send_chat_action(message.chat.id, "typing")
        bot.send_message(message.chat.id, "You are going to choose a friend to the group chat, not only for you")
        bot.send_chat_action(message.chat.id, "typing")
        bot.send_chat_action(message.chat.id, "typing")
    animal_keyboard = bot.send_message(message.chat.id, "It is dangerous to go alone, choose one :", reply_markup=markup)
    bot.register_next_step_handler(animal_keyboard , step_choose_animal)



#@bot.message_handler(content_types=['text'])
#def teste(message):
#    age = bot.send_message(message.chat.id, "How old are you?")
#    bot.register_next_step_handler(age , step_set_age)

#def step_set_age(message):
#    age2 = message.text
#    bot.send_message(message.chat.id, "Your age is "+str(age2))
#    year = bot.send_message(message.chat.id,'When were you born?')
#    bot.register_next_step_handler(year, step_set_year)

#def step_set_year(message):
#    year2= message.text
#    bot.send_message(message.chat.id, "You was born in "+str(year2))





#Handle the animal and sends it to confirmation
def step_choose_animal(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard= True)
    yes = types.KeyboardButton('YES!')
    another = types.KeyboardButton('I wanna look another one')
    markup.row( yes, another)
    
    the_animal = message.text
    bot.send_message(message.chat.id, str(the_animal)+"... OK.")

    if the_animal == 'Snake \U0001F40D':
        photox = open('fotos-aleatorias/snake.jpg', 'rb')
        #photox = open(path+'fotos-aleatorias/snake.jpg', 'rb')
        bot.send_photo(message.chat.id, photox)
        bot.send_chat_action(message.chat.id, "typing")
        confirm_animal = bot.send_message(message.chat.id, "Would you like to have this buddy as your friend?", reply_markup=markup)

        bot.register_next_step_handler(confirm_animal , step_animal_confirmation, "Snake")
       
        

    if the_animal == 'Cat \U0001F408':
        photox = open('fotos-aleatorias/cat.jpg', 'rb')
        #photox = open(path+'fotos-aleatorias/cat.jpg', 'rb')
        bot.send_photo(message.chat.id, photox)
        bot.send_chat_action(message.chat.id, "typing")
        confirm_animal = bot.send_message(message.chat.id, "Would you like to have this buddy as your friend?", reply_markup=markup)

        bot.register_next_step_handler(confirm_animal , step_animal_confirmation, "Cat")

        
        
    if the_animal == 'Dog \U0001F415':
        photox = open('fotos-aleatorias/dog.jpg', 'rb')
        #photox = open(path+'fotos-aleatorias/dog.jpg', 'rb')
        bot.send_photo(message.chat.id, photox)
        bot.send_chat_action(message.chat.id, "typing")
        confirm_animal = bot.send_message(message.chat.id, "Would you like to have this buddy as your friend?", reply_markup=markup)

        bot.register_next_step_handler(confirm_animal , step_animal_confirmation, "Dog")

        
        
    if the_animal == 'Parrot \U0001F99C':
        photox = open('fotos-aleatorias/parrot.jpg', 'rb')
        #photox = open(path+'fotos-aleatorias/parrot.jpg', 'rb')
        bot.send_photo(message.chat.id, photox)
        bot.send_chat_action(message.chat.id, "typing")
        confirm_animal = bot.send_message(message.chat.id, "Would you like to have this buddy as your friend?", reply_markup=markup)

        bot.register_next_step_handler(confirm_animal , step_animal_confirmation, "Parrot")

        
        
    if the_animal == 'Duck \U0001F986':
        photox = open('fotos-aleatorias/duck.jpeg', 'rb')
        #photox = open(path+'fotos-aleatorias/duck.jpeg', 'rb')
        bot.send_photo(message.chat.id, photox)
        bot.send_chat_action(message.chat.id, "typing")
        confirm_animal = bot.send_message(message.chat.id, "Would you like to have this buddy as your friend?", reply_markup=markup)

        bot.register_next_step_handler(confirm_animal , step_animal_confirmation, "Duck")

        
        
    if the_animal == 'Gecko \U0001F98E':
        photox = open('fotos-aleatorias/gecko.jpg', 'rb')
        #photox = open(path+'fotos-aleatorias/gecko.jpg', 'rb')
        bot.send_photo(message.chat.id, photox)
        bot.send_chat_action(message.chat.id, "typing")
        confirm_animal = bot.send_message(message.chat.id, "Would you like to have this buddy as your friend?", reply_markup=markup)

        bot.register_next_step_handler(confirm_animal , step_animal_confirmation, "Gecko")



#confirm your friend (or not)
def step_animal_confirmation(message, animal):
    confirm_animal = message.text
    if confirm_animal == "YES!":
        if animal == "Snake":
            if message.chat.type == "group":
                if str('Group: '+message.chat.title) in animals:
                    bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
                else:
                    animals[str('Group: '+message.chat.title)]= 'Snake'
                    with open('arquivos-bot/animals.txt','a') as new_file:
                    #with open(path+'arquivos-bot/animals.txt','a') as new_file:
                        new_file.write('Group '+str(message.chat.title)+": "+'Snake\n')
                    bot.send_message(message.chat.id, "WOW, take care")
                    bot.send_message(message.chat.id, "Now you are ready to start your journey :)")

                    #Player(id,animal,personalidade):
                    if str(message.chat.id) in players:
                        pass
                    else: players[str(message.chat.id)]= Player(message.chat.id,animals[str(message.chat.title)], "Repugnant")
                    if players[str(message.chat.id)].Hp==100:
                        bot.send_message(message.chat.id, "I always think human lives are repugnants, so I described you like this. Take this simple quiz, let's see if you have something good")
                        quiz(message)
            else:       
                if str(message.chat.id) in animals:
                    bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
                else:
                    animals[str(message.chat.id)]= 'Snake'
                    with open('arquivos-bot/animals.txt','a') as new_file:
                    #with open(path+'arquivos-bot/animals.txt','a') as new_file:
                        new_file.write(str(message.chat.id)+": "+'Snake\n')
                        #arr = bytes(str(message.chat.first_name)+": "+"Snake"" "+str(message.chat.id)+'\n', 'utf-8')
                        create_file_dict(dbx,fanimals,animals)#######################################################################
                    bot.send_message(message.chat.id, "WOW, take care")
                    bot.send_message(message.chat.id, "Now you are ready to start your journey :)")
                    
                    #Player(id,animal,personalidade):
                    if str(message.chat.id) in players:
                        pass
                    else: players[str(message.chat.id)]= Player(message.chat.id,animals[str(message.chat.id)], "Repugnant")
                    if players[str(message.chat.id)].Hp==100:
                        bot.send_message(message.chat.id, "I always think human lives are repugnants, so I described you like this. Take this simple quiz, let's see if you have something good")
                    #print(players[str(message.chat.id)].id)
                    #print(players[str(message.chat.id)].animal)
                    #print(players[str(message.chat.id)].personality)
                    quiz(message)
        
        if animal == "Cat":
            if message.chat.type == "group":
                if str('Group: '+message.chat.title) in animals:
                    bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
                else:
                    animals[str('Group: '+message.chat.title)]= 'Cat'
                    with open('arquivos-bot/animals.txt','a') as new_file:
                    #with open(path+'arquivos-bot/animals.txt','a') as new_file:
                        new_file.write('Group '+str(message.chat.title)+": "+'Cat\n')
                    bot.send_message(message.chat.id, "Nice!")
                    bot.send_message(message.chat.id, "Now you are ready to start your journey :)")

                    #Player(id,animal,personalidade):
                    if str(message.chat.id) in players:
                        pass
                    else: players[str(message.chat.id)]= Player(message.chat.id,animals[str(message.chat.title)], "Repugnant")
                    if players[str(message.chat.id)].Hp==100:
                        bot.send_message(message.chat.id, "I always think human lives are repugnants, so I described you like this. Take this simple quiz, let's see if you have something good")
                        quiz(message)
            else:
                if str(message.chat.id) in animals:
                    bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
                else:
                    animals[str(message.chat.id)]= 'Cat'
                    with open('arquivos-bot/animals.txt','a') as new_file:
                    #with open(path+'arquivos-bot/animals.txt','a') as new_file:
                        new_file.write(str(message.chat.id)+": "+'Cat\n')
                        #arr = bytes(str(message.chat.first_name)+": "+"Cat"" "+str(message.chat.id)+'\n', 'utf-8')
                        create_file_dict(dbx,fanimals,animals)#######################################################################
                    bot.send_message(message.chat.id, "Nice!")
                    bot.send_message(message.chat.id, "Now you are ready to start your journey :)")

                    #Player(id,animal,personalidade):
                    if str(message.chat.id) in players:
                        pass
                    else: players[str(message.chat.id)]= Player(message.chat.id,animals[str(message.chat.id)], "Repugnant")
                    if players[str(message.chat.id)].Hp==100:
                        bot.send_message(message.chat.id, "I always think human lives are repugnants, so I described you like this. Take this simple quiz, let's see if you have something good")
                        quiz(message)

        if animal == "Dog":
            if message.chat.type == "group":
                if str('Group: '+message.chat.title) in animals:
                    bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
                else:
                    animals[str('Group: '+message.chat.title)]= 'Dog'
                    with open('arquivos-bot/animals.txt','a') as new_file:
                    #with open(path+'arquivos-bot/animals.txt','a') as new_file:
                        new_file.write('Group '+str(message.chat.title)+": "+'Dog\n')
                    bot.send_message(message.chat.id, "Nice!! Take 6, you have an army now haha")
                    bot.send_message(message.chat.id, "Now you are ready to start your journey :)")

                    #Player(id,animal,personalidade):
                    if str(message.chat.id) in players:
                        pass
                    else: players[str(message.chat.id)]= Player(message.chat.id,animals[str(message.chat.title)], "Repugnant")
                    if players[str(message.chat.id)].Hp==100:
                        bot.send_message(message.chat.id, "I always think human lives are repugnants, so I described you like this. Take this simple quiz, let's see if you have something good")
                        quiz(message)
            
            else:
                if str(message.chat.id) in animals:
                    bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
                else:
                    animals[str(message.chat.id)]= 'Dog'
                    with open('arquivos-bot/animals.txt','a') as new_file:
                    #with open(path+'arquivos-bot/animals.txt','a') as new_file:
                        new_file.write(str(message.chat.first_name)+": "+'Dog\n')
                        #arr = bytes(str(message.chat.first_name)+": "+"Dog"" "+str(message.chat.id)+'\n', 'utf-8')
                        create_file_dict(dbx,fanimals,animals)#######################################################################
                    bot.send_message(message.chat.id, "Nice!! Take 6, you have an army now haha")
                    bot.send_message(message.chat.id, "Now you are ready to start your journey :)")

                    #Player(id,animal,personalidade):
                    if str(message.chat.id) in players:
                        pass
                    else: players[str(message.chat.id)]= Player(message.chat.id,animals[str(message.chat.id)], "Repugnant")
                    if players[str(message.chat.id)].Hp==100:
                        bot.send_message(message.chat.id, "I always think human lives are repugnants, so I described you like this. Take this simple quiz, let's see if you have something good")
                        quiz(message)

        if animal == "Parrot":
            if message.chat.type == "group":
                if str('Group: '+message.chat.title) in animals:
                    bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
                else:
                    animals[str('Group: '+message.chat.title)]= 'Parrot'
                    with open('arquivos-bot/animals.txt','a') as new_file:
                    #with open(path+'arquivos-bot/animals.txt','a') as new_file:
                        new_file.write('Group '+str(message.chat.title)+": "+'Parrot\n')
                    bot.send_message(message.chat.id, "Nice!!!")
                    bot.send_message(message.chat.id, "Now you are ready to start your journey :)")

                    #Player(id,animal,personalidade):
                    if str(message.chat.id) in players:
                        pass
                    else: players[str(message.chat.id)]= Player(message.chat.id,animals[str(message.chat.title)], "Repugnant")
                    if players[str(message.chat.id)].Hp==100:
                        bot.send_message(message.chat.id, "I always think human lives are repugnants, so I described you like this. Take this simple quiz, let's see if you have something good")
                        quiz(message)
            
            else:
                if str(message.chat.id) in animals:
                    bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
                else:
                    animals[str(message.chat.id)]= 'Parrot'
                    with open('arquivos-bot/animals.txt','a') as new_file:
                    #with open(path+'arquivos-bot/animals.txt','a') as new_file:
                        new_file.write(str(message.chat.first_name)+": "+'Parrot\n')
                        #arr = bytes(str(message.chat.first_name)+": "+"Parrot"" "+str(message.chat.id)+'\n', 'utf-8')
                        create_file_dict(dbx,fanimals,animals)#######################################################################
                    bot.send_message(message.chat.id, "Nice!!!")
                    bot.send_message(message.chat.id, "Now you are ready to start your journey :)")

                    #Player(id,animal,personalidade):
                    if str(message.chat.id) in players:
                        pass
                    else: players[str(message.chat.id)]= Player(message.chat.id,animals[str(message.chat.id)], "Repugnant")
                    if players[str(message.chat.id)].Hp==100:
                        bot.send_message(message.chat.id, "I always think human lives are repugnants, so I described you like this. Take this simple quiz, let's see if you have something good")
                        quiz(message)

        if animal == "Duck":
            if message.chat.type == "group":
                if str('Group: '+message.chat.title) in animals:
                    bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
                else:
                    animals[str('Group: '+message.chat.title)]= 'Duck'
                    with open('arquivos-bot/animals.txt','a') as new_file:
                    #with open(path+'arquivos-bot/animals.txt','a') as new_file:
                        new_file.write('Group '+str(message.chat.title)+": "+'Duck\n')
                    bot.send_message(message.chat.id, "WTF...")
                    bot.send_message(message.chat.id, "Now you are ready to start your journey :)")

                    #Player(id,animal,personalidade):
                    if str(message.chat.id) in players:
                        pass
                    else: players[str(message.chat.id)]= Player(message.chat.id,animals[str(message.chat.title)], "Repugnant")
                    if players[str(message.chat.id)].Hp==100:
                        bot.send_message(message.chat.id, "I always think human lives are repugnants, so I described you like this. Take this simple quiz, let's see if you have something good")
                        quiz(message)
            else:
                if str(message.chat.id) in animals:
                    bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
                else:
                    animals[str(message.chat.id)]= 'Duck'
                    with open('arquivos-bot/animals.txt','a') as new_file:
                    #with open(path+'arquivos-bot/animals.txt','a') as new_file:
                        new_file.write(str(message.chat.first_name)+": "+'Duck\n')
                        #arr = bytes(str(message.chat.first_name)+": "+"Duck"" "+str(message.chat.id)+'\n', 'utf-8')
                        create_file_dict(dbx,fanimals,animals)#######################################################################
                    bot.send_message(message.chat.id, "WTF...")
                    bot.send_message(message.chat.id, "Now you are ready to start your journey :)")

                    #Player(id,animal,personalidade):
                    if str(message.chat.id) in players:
                        pass
                    else: players[str(message.chat.id)]= Player(message.chat.id,animals[str(message.chat.id)], "Repugnant")
                    if players[str(message.chat.id)].Hp==100:
                        bot.send_message(message.chat.id, "I always think human lives are repugnants, so I described you like this. Take this simple quiz, let's see if you have something good")
                        quiz(message)

        if animal == "Gecko":
            if message.chat.type == "group":
                if str('Group: '+message.chat.title) in animals:
                    bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
                else:
                    animals[str('Group: '+message.chat.title)]= 'Gecko'
                    with open('arquivos-bot/animals.txt','a') as new_file:
                    #with open(path+'arquivos-bot/animals.txt','a') as new_file:
                        new_file.write('Group '+str(message.chat.title)+": "+'Gecko\n')
                    bot.send_message(message.chat.id, "How cute!")
                    bot.send_message(message.chat.id, "Now you are ready to start your journey :)")

                    #Player(id,animal,personalidade):
                    if str(message.chat.id) in players:
                        pass
                    else: players[str(message.chat.id)]= Player(message.chat.id,animals[str(message.chat.title)], "Repugnant")
                    if players[str(message.chat.id)].Hp==100:
                        bot.send_message(message.chat.id, "I always think human lives are repugnants, so I described you like this. Take this simple quiz, let's see if you have something good")
                        quiz(message)
            else:
                if str(message.chat.id) in animals:
                    bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
                else:
                    animals[str(message.chat.id)]= 'Gecko'
                    with open('arquivos-bot/animals.txt','a') as new_file:
                    #with open(path+'arquivos-bot/animals.txt','a') as new_file:
                        new_file.write(str(message.chat.first_name)+": "+'Gecko\n')
                        #arr = bytes(str(message.chat.first_name)+": "+"Gecko"" "+str(message.chat.id)+'\n', 'utf-8')
                        create_file_dict(dbx,fanimals,animals)#######################################################################
                    bot.send_message(message.chat.id, "How cute!")
                    bot.send_message(message.chat.id, "Now you are ready to start your journey :)")

                    #Player(id,animal,personalidade):
                    if str(message.chat.id) in players:
                        pass
                    else: 
                        players[str(message.chat.id)]= Player(message.chat.id,animals[str(message.chat.id)], "Repugnant")
                        #arr = bytes(str(message.chat.first_name)+": "+"Repugnant"" "+str(message.chat.id)+'\n', 'utf-8')
                    if players[str(message.chat.id)].Hp==100:
                        bot.send_message(message.chat.id, "I always think human lives are repugnants, so I described you like this. Take this simple quiz, let's see if you have something good")
                        quiz(message)

    else: handle_choose_animal(message)



#================ TESTANDO CRIAÇÃO DE CONVERSAS ========================

#@bot.message_handler(content_types=['text'])
#def teste(message):
#    age = bot.send_message(message.chat.id, "How old are you?")
#    bot.register_next_step_handler(age , step_set_age)

#def step_set_age(message):
#    age2 = message.text
#    bot.send_message(message.chat.id, "Your age is "+str(age2))
#    year = bot.send_message(message.chat.id,'When were you born?')
#    bot.register_next_step_handler(year, step_set_year)

#def step_set_year(message):
#    year2= message.text
#    bot.send_message(message.chat.id, "You was born in "+str(year2))

#================ TESTANDO CRIAÇÃO DE CONVERSAS ========================



@bot.message_handler(content_types=['text'])
def quiz(message):
    if message.text.lower() == "quiz":
    #bot.forward_message(847307875,message.chat.id,message.id)

    # Build inline keyboard
        keyboard1 = [InlineKeyboardButton("Yes", callback_data='y')]
        keyboard2 = [InlineKeyboardButton("No", callback_data='n')]
    
    # create reply keyboard markup
        reply_markup = InlineKeyboardMarkup([keyboard1, keyboard2])    # send message with text and appended inline keyboard
        bot.send_message(message.chat.id,"Do you know how to fly?",reply_markup=reply_markup)
    
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Answer accepted!')
    answer = 'You sure?'
    if call.data == 'y':
        answer = 'Prove it!'
#    else:
#        keyboard1 = [InlineKeyboardButton("maybe", callback_data='maybe')]
#        keyboard2 = [InlineKeyboardButton("ok", callback_data='ok')]
    
        # create reply keyboard markup
#        reply_markup = InlineKeyboardMarkup([keyboard1, keyboard2])    # send message with text and appended inline keyboard
#        bot.send_message(message.chat.id,"teste",reply_markup=reply_markup)
    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    #flow_yes(call,message)

#def flow_yes(call:True ,message:True):
#    if call.data =='y':
#        keyboard1 = [InlineKeyboardButton("maybe", callback_data='maybe')]
#        keyboard2 = [InlineKeyboardButton("ok", callback_data='ok')]
    
        # create reply keyboard markup
#        reply_markup = InlineKeyboardMarkup([keyboard1, keyboard2])    # send message with text and appended inline keyboard
#        bot.send_message(message.chat.id,"teste",reply_markup=reply_markup)
#    else:
#        keyboard1 = [InlineKeyboardButton("wa", callback_data='wa')]
#        keyboard2 = [InlineKeyboardButton("wo", callback_data='wo')]
    
        # create reply keyboard markup
#        reply_markup = InlineKeyboardMarkup([keyboard1, keyboard2])    # send message with text and appended inline keyboard
#        bot.send_message(message.chat.id,"teste",reply_markup=reply_markup)

#    if call.data == 'maybe' or 'wa':
#        answer = 'Prove it!'
#    else: answer = "falho7u"

#    bot.send_message(call.message.chat.id,answer)
#    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id) 


#=======================================QUIZ======================================================================
def quiz(message):
    personality={}
    markup = types.ReplyKeyboardMarkup(one_time_keyboard= True)
    Morning = types.KeyboardButton('Morning')
    Afternoon = types.KeyboardButton('Afternoon')
    Night = types.KeyboardButton('Night')
    markup.row( Morning, Afternoon, Night)
    
    bot.send_message(message.chat.id, "Let's start the quiz")

    answer1= bot.send_message(message.chat.id, "Do you prefer morning, afternoon or evening?", reply_markup=markup)
    bot.register_next_step_handler(answer1, step_quiz2, personality)


def step_quiz2(message,personality): #Do you believe in God? Yes, no , -1, 3"
    if message.text == "Night":
        personality[str(message.chat.id)]= 2
    else:
        personality[str(message.chat.id)]= 1

    markup = types.ReplyKeyboardMarkup(one_time_keyboard= True)
    Yes = types.KeyboardButton('Yes')
    No = types.KeyboardButton('No')
    markup.row( Yes,No)

    answer1= bot.send_message(message.chat.id, "Do you believe in God?", reply_markup=markup)
    bot.register_next_step_handler(answer1, step_quiz3, personality)

def step_quiz3(message,personality):# 3 - "If you were a God, who would you be? God of War, God of Nature, God of Wisdom. -5 , 1 , 4"
    if message.text == "Yes":
        personality[str(message.chat.id)]+= -1
    else:
        personality[str(message.chat.id)]+= 3
    
    markup = types.ReplyKeyboardMarkup(one_time_keyboard= True)
    War = types.KeyboardButton('God of War')
    Nature = types.KeyboardButton('God of Nature')
    Wisdom = types.KeyboardButton('God of Wisdom')
    markup.row( War, Nature, Wisdom)

    answer1= bot.send_message(message.chat.id, "If you were a God, who would you be?", reply_markup=markup)
    bot.register_next_step_handler(answer1, step_quiz4, personality)

def step_quiz4(message,personality):# 4 - "If you could master an element, what would it be? Water, fire, wind, earth. 1, -5, 1, 0 "
    if message.text == "God of War":
        personality[str(message.chat.id)]+= -5
    elif message.text == "God of Nature":
        personality[str(message.chat.id)]+= 1
    else: 
        personality[str(message.chat.id)]+= 4
        
    markup = types.ReplyKeyboardMarkup(one_time_keyboard= True)
    Water = types.KeyboardButton('Water')
    Fire = types.KeyboardButton('Fire')
    Wind = types.KeyboardButton('Wind')
    Earth = types.KeyboardButton('Earth')
    markup.row( Water,Fire,Wind,Earth)

    answer1= bot.send_message(message.chat.id, "If you could master an element, what would it be?", reply_markup=markup)
    bot.register_next_step_handler(answer1, step_quiz5, personality)

def step_quiz5(message,personality):# 5 - "Are you happy? Yes, no. 1 , -3"
    if message.text == "Fire":
        personality[str(message.chat.id)]+= -5
    elif message.text == "Earth":
        personality[str(message.chat.id)]+= 0
    else: 
        personality[str(message.chat.id)]+= 1
        
    markup = types.ReplyKeyboardMarkup(one_time_keyboard= True)
    Yes = types.KeyboardButton('Yes')
    No = types.KeyboardButton('No')
    markup.row( Yes,No)

    answer1= bot.send_message(message.chat.id, "Are you happy?", reply_markup=markup)
    bot.register_next_step_handler(answer1, step_quiz6, personality)

def step_quiz6(message,personality):# 6 - "How often do you lie? None, low, medium, high. 0, -1, -2, -4"
    if message.text == "Yes":
        personality[str(message.chat.id)]+= 1
    else:
        personality[str(message.chat.id)]+= -3

    markup = types.ReplyKeyboardMarkup(one_time_keyboard= True)
    Nonex = types.KeyboardButton('None')
    Low = types.KeyboardButton('Low')
    Medium = types.KeyboardButton('Medium')
    High = types.KeyboardButton('High')
    markup.row( Nonex,Low,Medium,High)

    answer1= bot.send_message(message.chat.id, "How often do you lie?", reply_markup=markup)
    bot.register_next_step_handler(answer1, step_quiz7, personality)

def step_quiz7(message,personality): # 7 - "Are you a stressed person? Yes, no. -2, 2"
    if message.text == "None":
        personality[str(message.chat.id)]+= 0
    elif message.text == "Low":
        personality[str(message.chat.id)]+= -1
    elif message.text == "Medium":
        personality[str(message.chat.id)]+= -2
    else:
        personality[str(message.chat.id)]+= -4
        
    markup = types.ReplyKeyboardMarkup(one_time_keyboard= True)
    Yes = types.KeyboardButton('Yes')
    No = types.KeyboardButton('No')
    markup.row( Yes,No)

    answer1= bot.send_message(message.chat.id, "Are you a stressed person?", reply_markup=markup)
    bot.register_next_step_handler(answer1, step_quiz8, personality)


def step_quiz8(message,personality): # 8 - "Are you an ambitious person? Yes, no, -3, 2"
    if message.text == "Yes":
        personality[str(message.chat.id)]+= -2
    else:
        personality[str(message.chat.id)]+= 2
        
    markup = types.ReplyKeyboardMarkup(one_time_keyboard= True)
    Yes = types.KeyboardButton('Yes')
    No = types.KeyboardButton('No')
    markup.row( Yes,No)
        
    answer1= bot.send_message(message.chat.id, "Are you an ambitious person?", reply_markup=markup)
    bot.register_next_step_handler(answer1, step_quiz9, personality)


def step_quiz9(message,personality): # 9 - ""Would you kill for money?"? Truth, lie. -4, 2"
    if message.text == "Yes":
        personality[str(message.chat.id)]+= -3
    else:
        personality[str(message.chat.id)]+= 2
        
    markup = types.ReplyKeyboardMarkup(one_time_keyboard= True)
    Yes = types.KeyboardButton('Yes')
    No = types.KeyboardButton('No')
    markup.row( Yes,No)
    
    answer1= bot.send_message(message.chat.id, "Would you kill for money?", reply_markup=markup)
    bot.register_next_step_handler(answer1, step_quiz10, personality)

    
def step_quiz10(message,personality): # 10 - "Power, happiness or peace? Power, happiness, peace. -2, -1, 1"
    if message.text == "Yes":
        personality[str(message.chat.id)]+= -4
    else:
        personality[str(message.chat.id)]+= 2

    markup = types.ReplyKeyboardMarkup(one_time_keyboard= True)
    Power = types.KeyboardButton('Power')
    Happiness = types.KeyboardButton('Happiness')
    Peace = types.KeyboardButton('Peace')
    markup.row( Power, Happiness, Peace)

    answer1= bot.send_message(message.chat.id,"Power, happiness or peace?", reply_markup=markup)
    bot.register_next_step_handler(answer1, step_quiz_score, personality)

    
def step_quiz_score(message,personality):
    if message.text == "Power":
        personality[str(message.chat.id)]+= -2
    elif message.text == "Peace":
        personality[str(message.chat.id)]+= 1
    else:
        personality[str(message.chat.id)]+= -1
    thepersonality(message,personality)


def thepersonality(message,personality):
    if personality[str(message.chat.id)] >= 0 and personality[str(message.chat.id)] <= 5:
        players[str(message.chat.id)].Personality = "The Chosen One"
        personality[str(message.chat.id)]= "The Chosen One"
        players[str(message.chat.id)].Power+=10000
    elif personality[str(message.chat.id)] >= 6 and personality[str(message.chat.id)] <= 10:   
        players[str(message.chat.id)].Personality = "The Knight"
        personality[str(message.chat.id)]= "The Knight"
        players[str(message.chat.id)].Power+=3000
    elif personality[str(message.chat.id)] > 10 and personality[str(message.chat.id)] <= 15:   
        players[str(message.chat.id)].Personality = "The Peasant"
        personality[str(message.chat.id)]= "The Peasant"
        players[str(message.chat.id)].Power+=1000
    elif personality[str(message.chat.id)] > 15 and personality[str(message.chat.id)] <= 18:   
        players[str(message.chat.id)].Personality = "The Repugnant"
        players[str(message.chat.id)].Power-=1000
        personality[str(message.chat.id)]= "The Repugnant"
    elif personality[str(message.chat.id)] >= -28 and personality[str(message.chat.id)] <= -10:   
        players[str(message.chat.id)].Personality = "The Cambion"
        players[str(message.chat.id)].Power+=9999
        personality[str(message.chat.id)]= "The Cambion"
    bot.send_message(message.chat.id, "You seems to be "+players[str(message.chat.id)].Personality)
    #arr = bytes(str(message.chat.first_name)+": "+str(players[str(message.chat.id)].Personality)+" "+str(message.chat.id)+'\n', 'utf-8')
    create_file_dict(dbx,fpersonalities,personality)#########################################
    x = players[str(message.chat.id)].send_all_list()
    del(x[0])
    data=""
    for y in x:
        data+=y+"\n"
    data=data.encode()
                        
    create_file_data(dbx,fplayers,data)#######################################################################

#=======================================QUIZ======================================================================

#if __name__ == "__main__":
print('Exodia, Obliterate!')
bot.polling()
