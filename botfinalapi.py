# -*- coding: utf-8 -*-
import telebot
from telebot import types
import random
from time import sleep
import requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

#getmes=[]
getmes={}
ungetmes={}
#admin = {}
contagem={}
animals={}
control=0
#content_types=["text", "sticker", "pinned_message", "photo", "audio"]

sobre = "This bot was developed and created by Danyel Clinário. It is still in the testing phase, any \
suggestion is welcome! Write me!"

bot = telebot.TeleBot("1147645813:AAHbIB78oyWUwz_JYT3pFaKgEjCPsOL2hhQ")

# Handles all text messages that contains the command '/start'
@bot.message_handler(commands=['start'])
def handle_start(message):
    if message.chat.type == "private":
        bot.send_message(message.chat.id, 'Hello, '+ message.chat.first_name +'. My name is Exodia. How can I help you?')
        handle_getme(message)
        bot.reply_to(message, "Would like to see the menu? You just need to click here: /menu")
    #print(message)
    else:
        bot.send_message(message.chat.id, 'Hello people from '+ message.chat.title +' group. My name is Exodia. How can I help you?')
        handle_getme(message)
        bot.reply_to(message, "Would like to see the menu? You just need to click here: /menu")

    
    

# Handles all text messages that contains the command '/help'.
@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.reply_to(message, "How can I help you?")
    sleep(2)
    bot.send_message(message.chat.id,
        '1) /menu - The list of all my 9 commands\n' +
        '2) /start - Get started about the game (under development)\n' +
        '3) /help - Questions and answers about the game (under development)\n' +
        '4) /getme - Subscribe to create your account and get some news!\n' +
        '5) /about - Contact my creator!\n'+
        "6) /play - Let's play some dices! \n" +
        '7) /score - I can show you our score \n' +
        '8) /stop - Delete your account (under development) \n' +
        '9) /myfriend - Details about your friend (under development)\n' +
        '10) Show me the Keyboard - not a command but something you should type\n'+
        'Future features:\n'+
        'Coming soon!\n')  



# xaveco
#@bot.message_handler(commands=['xaveco'])
#def handle_xaveco(message):
#    bot.send_message(1108257002, "eu tbm te amo ta")

# getting your chat id
@bot.message_handler(commands=['getme'])
def handle_getme(message):
    #bot.reply_to(message, "That's your chat id: "+ str(message.chat.id))
    #bot.forward_message(847307875,message.chat.id,message.id)

    if message.chat.type == "private":
        if message.chat.first_name in getmes:
            bot.reply_to(message, "I already have your chat id for further interactions")
        else:
            getmes[str(message.chat.first_name)]=str(message.chat.id)
            bot.send_message(847307875, "Someone just subscribed! "+message.chat.first_name+ " joined")
            bot.reply_to(message, "I just saved your chat id for further interactions")
    #getmes.append(message.chat.id)
    
    if message.chat.type == "group":
        if message.chat.title in getmes:
            bot.reply_to(message, "I already have your chat id for further interactions")
        else:
            getmes[str(message.chat.title)]=str(message.chat.id)
            bot.send_message(847307875, "Someone just subscribed! "+message.chat.title+ " joined")
            bot.reply_to(message, "I just saved your chat id for further interactions")
        #getmes.append(str(message.chat.title))
        #getmes.append(str(message.chat.first_name))
        #for x in getmes:
        #    bot.send_message(847307875,x)
            #bot.send_message(847307875, str(message))


# Handles all text messages that contains the command '/about'.
@bot.message_handler(commands=['about'])
def handle_about(message):
    #bot.reply_to(message, sobre)
    #keyboard = telebot.types.InlineKeyboardMarkup()
    #keyboard.add(telebot.types.InlineKeyboardButton('Message the developer', url='telegram.me/DanyelC'))
    #bot.send_message(message.chat.id,
    #    '1) To receive a list of available currencies press /exchange.\n' +
    #    '2) Click on the currency you are interested in.\n' +
    #    '3) You will receive a message containing information regarding the source and the target currencies, ' +
    #    'buying rates and selling rates.\n' +
    #    '4) Click “Update” to receive the current information regarding the request. ' +
    #    'The bot will also show the difference between the previous and the current exchange rates.\n' +
    #    '5) The bot supports inline. Type @<botusername> in any chat and the first letters of a currency.',
    #    reply_markup=keyboard)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Message the developer', url='telegram.me/DanyelC'))
    bot.send_message(message.chat.id,sobre,reply_markup=keyboard)
    
# Handles all text messages that contains the command '/play'.
@bot.message_handler(commands=['play', 'score'])
def handle_play_score(message):
    if message.text == "/play":
        #contagem = [0,0]
        _1 = random.randint(1, 6)
        _2 = random.randint(1, 6)
        _3 = random.randint(1, 6)
        _4 = random.randint(1, 6)
        _5 = random.randint(1, 6)
        _6 = random.randint(1, 6)
        bot.reply_to(message, "OK! Let me roll the dice")
        bot.send_message(message.chat.id, 'You have ' + str(_1) + ' and ' + str(_2) + ' and ' + str(_3) + ' !\n Your result is ' + str(_1 + _2 + _3) + '!!!')
        sleep(1)
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
            sleep(1)
            bot.send_message(message.chat.id,torneio)
            sleep(1)
            if torneio!="Nobody won, sorry":
                bot.send_message(message.chat.id, "Your score is %d and mine is %d" % (contagem[str(message.chat.first_name)], contagem[str(message.chat.first_name)+'Exodia']))
            bot.send_message(message.chat.id, "Let's play again? /play")

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
            sleep(1)
            bot.send_message(message.chat.id,torneio)
            sleep(1)
            if torneio!="Nobody won, sorry":
                bot.send_message(message.chat.id, "Your score is %d and mine is %d" % (contagem[str(message.chat.title)], contagem[str(message.chat.title)+'Exodia']))
            bot.send_message(message.chat.id, "Let's play again? /play")            
    
        if message.text == "/score":
            if str(message.chat.first_name) in contagem:
                bot.reply_to(message, "Your score is %d and mine is %d" % (contagem[str(message.chat.first_name)], contagem[str(message.chat.first_name)+'Exodia']))
            else: 
                bot.reply_to(message, "We haven't played ... yet. Lets play now! Click here: /play")
        
    
# Handles all text messages that contains the command '/stop'.
@bot.message_handler(commands=['stop'])
def handle_stop(message):
    bot.reply_to(message, "Don't worry! I won't write you again (except if you write me hahaha)")
    if message.chat.type == "private":
        if str(message.chat.first_name) in getmes:
            ungetmes[str(message.chat.first_name)] = getmes[str(message.chat.first_name)]
            del getmes[str(message.chat.first_name)]
            bot.send_message(message.chat.id, "Your chat id was deleted")
        else:
            bot.send_message(message.chat.id, "Your chat id is not saved")
    elif message.chat.type == "group":
        if str(message.chat.title) in getmes:
            ungetmes[str(message.chat.title)]=getmes[str(message.chat.title)]
            del getmes[str(message.chat.title)]
            bot.send_message(message.chat.id, "Your chat id was deleted")
        else:
            bot.send_message(message.chat.id, "Your chat id is not saved")
#colocar o unsubscribe
    

# ADMIN STUFF BRO ---------------------------------------------------------------------------------------------------

#@bot.message_handler(commands=['iamyourfather'])
#def handle_admin(message):
#    if message.chat.id == 847307875:
#        if message.chat.first_name == 'Danyel':
#            bot.send_message(message.chat.id, "You sure? Prove it")
#            admin['admin1'] = 1

#@bot.message_handler(commands=['prove'])
#def handle_adminho(message):
#    if message.chat.id == 847307875:
#        if message.chat.first_name == 'Danyel':
#            bot.send_message(message.chat.id, "NOOOOOOOOOOOOOO")
#            admin['admin2'] = 1

@bot.message_handler(commands=['contagem'])
def handle_adminhozinho(message):
    if message.chat.id == 847307875:
        if message.chat.first_name == 'Danyel':
#            if 'admin1' in admin and 'admin2' in admin:
            if contagem:
                for x, y in contagem.items():
                    bot.send_message(message.chat.id, x)
                    bot.send_message(message.chat.id, y)
                    bot.send_message(message.chat.id, "----------------")
            else: bot.send_message(message.chat.id, "nothing")
#                del admin['admin1']
#                del admin['admin2']



@bot.message_handler(commands=['animals'])
def handle_adminhozinho(message):
    if message.chat.id == 847307875:
        if message.chat.first_name == 'Danyel':
#            if 'admin1' in admin and 'admin2' in admin:
            if animals:
                for x, y in animals.items():
                    bot.send_message(message.chat.id, x)
                    bot.send_message(message.chat.id, y)
                    bot.send_message(message.chat.id, "----------------")
            else: bot.send_message(message.chat.id, "nothing")
#                del admin['admin1']
#                del admin['admin2']


@bot.message_handler(commands=['getmes'])
def handle_adminhozinho(message):
    if message.chat.id == 847307875:
        if message.chat.first_name == 'Danyel':
            if getmes:
                for x, y in getmes.items():
                    bot.send_message(message.chat.id, x)
                    bot.send_message(message.chat.id, y)
                    bot.send_message(message.chat.id, "----------------")
            else: bot.send_message(message.chat.id, "nothing")


@bot.message_handler(commands=['ungetmes'])
def handle_adminhozinho(message):
    if message.chat.id == 847307875:
        if message.chat.first_name == 'Danyel':
            if ungetmes:
                for x, y in ungetmes.items():
                    bot.send_message(message.chat.id, x)
                    bot.send_message(message.chat.id, y)
                    bot.send_message(message.chat.id, "----------------")
            else: bot.send_message(message.chat.id, "nothing")

# ADMIN STUFF BRO ---------------------------------------------------------------------------------------------------



# Handles all text messages that contains the command '/menu'.
@bot.message_handler(commands=['menu'])
def handle_menu(message):
    bot.send_message(message.chat.id, "A list of commands:")
    if message.chat.id == 847307875:
        if message.chat.first_name == 'Danyel':
            bot.send_message(message.chat.id,
            '1) /menu - The list of all my 9 commands\n' +
            '2) /start - Get started about the game (under development)\n' +
            '3) /help - Questions and answers about the game (under development)\n' +
            '4) /getme - Subscribe to create your account and get some news!\n' +
            '5) /about - Contact my creator!\n'+
            "6) /play - Let's play some dices! \n" +
            '7) /score - I can show you our score \n' +
            '8) /stop - Delete your account (under development) \n' +
            '9) /myfriend - Details about your friend (under development)\n' +
            '10) Show me the Keyboard - not a command but something you should type\n'+
            'Future features:\n'+
            'Coming soon!\n\n'
            'XXXXX-ADMIN MODE-XXXXX \n\n'+
            #'1) /xaveco\n' +
            #'2) /iamyourfather\n' +
            #'3) /prove\n' +
            '1) /getmes\n' +
            '2) /contagem\n'+
            '3) /animals\n'+
            '4) /ungetmes')
    else: bot.send_message(message.chat.id,
        '1) /menu - The list of all my 9 commands\n' +
        '2) /start - Get started about the game (under development)\n' +
        '3) /help - Questions and answers about the game (under development)\n' +
        '4) /getme - Subscribe to create your account and get some news!\n' +
        '5) /about - Contact my creator!\n'+
        "6) /play - Let's play some dices! \n" +
        '7) /score - I can show you our score \n' +
        '8) /stop - Delete your account (under development) \n' +
        '9) /myfriend - Details about your friend (under development)\n' +
        '10) Show me the Keyboard - not a command but something you should type\n'+
        'Future features:\n'+
        'Coming soon!\n')
    


@bot.message_handler(commands=['myfriend'])
def handle_aboutme(message):
    if str(message.chat.first_name) in animals:
        bot.reply_to(message, "Your friend is: "+ animals[message.chat.first_name])
    else:
        bot.send_message(message.chat.id, "You should choose a friend first. Type 'show me the keyboard'")

# Handles all photos sent
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    if message.chat.type == "private":
        bot.reply_to(message, "Nice! I'm going to upload your photo now. Do you want to see some cards?")
        #bot.send_chat_action(message.chat.id, 'upload_photo')
        _10 = random.randint(1, 10)
        _10 = str(_10)
        #foto= str("index"+"%s"+".jpeg" % (_10))
        foto= "index"+_10+".jpeg"
        #print(foto)
        photox = open('/home/gta/Desktop/danyel/bot/fotos-aleatorias/'+foto, 'rb')
        bot.send_photo(message.chat.id, photox)
        _10 = random.randint(1, 5)
        _10 = str(_10)
        #foto= str("index"+"%s"+".jpeg" % (_10))
        foto= "index"+_10+".jpeg"
        #obj = message.photo[0].file_id
        #print(obj)
        #obj.download()
        raw = message.photo[1].file_id
        #path = raw+".jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        nome_arq = str(raw)
        with open('/home/gta/Desktop/danyel/bot/arquivos-bot/'+message.chat.first_name+nome_arq,'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_message(message.chat.id,"Done! I've just downloaded your file, "+message.chat.first_name)

@bot.message_handler(content_types=['document'])
def handle_photo(message):
    if message.chat.type == "private":
        bot.reply_to(message, "Nice! I'm going to upload your document now. Do you want to see some cards?")
        #bot.send_chat_action(message.chat.id, 'upload_photo')
        _10 = random.randint(1, 5)
        _10 = str(_10)
        #foto= str("index"+"%s"+".jpeg" % (_10))
        foto= "index"+_10+".jpeg"
        photox = open('/home/gta/Desktop/danyel/bot/fotos-aleatorias/'+foto, 'rb')
        bot.send_photo(message.chat.id, photox)
        _10 = random.randint(1, 5)
        _10 = str(_10)
        #foto= str("index"+"%s"+".jpeg" % (_10))
        foto= "index"+_10+".jpeg"

        raw = message.document.file_id
        #path = raw+".jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        nome_arq = str(raw)
        with open('/home/gta/Desktop/danyel/bot/arquivos-bot/'+message.chat.first_name+nome_arq,'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_message(message.chat.id,"Done! I've just downloaded your file, "+message.chat.first_name)

# Handles all sent documents and audio files
@bot.message_handler(content_types=['audio', 'video'])
def handle_video_audio(message):
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


#@bot.message_handler(commands=['group'])
#def handle_group(message):
#    if message.chat.type == "group":
#        get_group(message)



@bot.message_handler(content_types=['text'])
def handle_text(message):
    #teste(message)
    #quiz(message)
    if message.text.lower() == 'show me the keyboard':
        global control
        control=1
        markup = types.ReplyKeyboardMarkup(one_time_keyboard= True)
        itembtna = types.KeyboardButton('cat')
        itembtnv = types.KeyboardButton('dog')
        itembtnc = types.KeyboardButton('parrot')
        itembtnd = types.KeyboardButton('duck')
        itembtne = types.KeyboardButton('gecko')
        itembtnkk = types.KeyboardButton('chameleon')
        markup.row(itembtna, itembtnv, itembtnkk)
        markup.row(itembtnc, itembtnd, itembtne)
        if message.chat.type == "group":
            bot.send_message(message.chat.id, "You are going to choose a friend to the group chat, not only for you")
            sleep(2)
        bot.send_message(message.chat.id, "It is dangerous to go alone, choose one :", reply_markup=markup)
        #check_control(message,control)
    #else: bot.forward_message(847307875,message.chat.id,message.id)


    #def check_control(message,control):
        #if control == 1:
    if message.text == 'chameleon':
        if message.chat.type == "group":
            if str('Group: '+message.chat.title) in animals:
                bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
            else:
                animals[str('Group: '+message.chat.title)]= 'chameleon'
                bot.send_message(message.chat.id, "Nice!! Take 2")
        else:       
            if str(message.chat.first_name) in animals:
                bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
            else:
                animals[str(message.chat.first_name)]= 'chameleon'
                bot.send_message(message.chat.id, "Nice!! Take 2")
        photox = open('/home/gta/Desktop/danyel/bot/fotos-aleatorias/chameleon.jpg', 'rb')
        bot.send_photo(message.chat.id, photox)
        

    if message.text == 'cat':
        if message.chat.type == "group":
            if str('Group: '+message.chat.title) in animals:
                bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
            else:
                animals[str('Group: '+message.chat.title)]= 'cat'
                bot.send_message(message.chat.id, "Nice!")
        else:
            if str(message.chat.first_name) in animals:
                bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
            else:
                animals[str(message.chat.first_name)]= 'cat'
                bot.send_message(message.chat.id, "Nice!")
        photox = open('/home/gta/Desktop/danyel/bot/fotos-aleatorias/cat.jpg', 'rb')
        bot.send_photo(message.chat.id, photox)
    
    if message.text == 'dog':
        if message.chat.type == "group":
            if str('Group: '+message.chat.title) in animals:
                bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
            else:
                animals[str('Group: '+message.chat.title)]= 'dog'
                bot.send_message(message.chat.id, "Nice!! Take 6, you have an army now haha")
        else:
            if str(message.chat.first_name) in animals:
                bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
            else:
                animals[str(message.chat.first_name)]= 'dog'
                bot.send_message(message.chat.id, "Nice!! Take 6, you have an army now haha")
        photox = open('/home/gta/Desktop/danyel/bot/fotos-aleatorias/dog.jpg', 'rb')
        bot.send_photo(message.chat.id, photox)

    if message.text == 'parrot':
        if message.chat.type == "group":
            if str('Group: '+message.chat.title) in animals:
                bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
            else:
                animals[str('Group: '+message.chat.title)]= 'parrot'
                bot.send_message(message.chat.id, "Nice!!!")
        else:
            if str(message.chat.first_name) in animals:
                bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
            else:
                animals[str(message.chat.first_name)]= 'parrot'
                bot.send_message(message.chat.id, "Nice!!!")
        photox = open('/home/gta/Desktop/danyel/bot/fotos-aleatorias/parrot.jpg', 'rb')
        bot.send_photo(message.chat.id, photox)

    if message.text == 'duck':
        if message.chat.type == "group":
            if str('Group: '+message.chat.title) in animals:
                bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
            else:
                animals[str('Group: '+message.chat.title)]= 'duck'
                bot.send_message(message.chat.id, "WTF")
        else:
            if str(message.chat.first_name) in animals:
                bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
            else:
                animals[str(message.chat.first_name)]= 'duck'
                bot.send_message(message.chat.id, "WTF")
        photox = open('/home/gta/Desktop/danyel/bot/fotos-aleatorias/duck.jpeg', 'rb')
        bot.send_photo(message.chat.id, photox)

    if message.text == 'gecko':
        if message.chat.type == "group":
            if str('Group: '+message.chat.title) in animals:
                bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
            else:
                animals[str('Group: '+message.chat.title)]= 'gecko'
                bot.send_message(message.chat.id, "How cute!")
        else:
            if str(message.chat.first_name) in animals:
                bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
            else:
                animals[str(message.chat.first_name)]= 'gecko'
                bot.send_message(message.chat.id, "How cute!")
        photox = open('/home/gta/Desktop/danyel/bot/fotos-aleatorias/gecko.jpg', 'rb')
        bot.send_photo(message.chat.id, photox)
    #if message.text.lower() == 'thanks' or 'thank you' or 'ty' or if 'than' in message.text.lower():
    if 'thank' in message.text.lower() or message.text.lower() =='ty':
        bot.send_message(message.chat.id, ":)")


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

    

print('Exodia, Obliterate!')
bot.polling()