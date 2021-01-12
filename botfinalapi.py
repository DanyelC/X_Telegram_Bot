# -*- coding: utf-8 -*-
import telebot
from telebot import types
import random
from time import sleep
import requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

getmes={}
ungetmes={}
contagem={}
animals={}
Danyel= 847307875
sobre = "This bot was developed and created by Danyel Clinário. It is still in the testing phase, any \
suggestion is welcome! Write me!"

bot = telebot.TeleBot("1147645813:AAHbIB78oyWUwz_JYT3pFaKgEjCPsOL2hhQ")


# Handles all text messages that contains the command '/start'
@bot.message_handler(commands=['start'])
def handle_start(message):
    if message.chat.type == "private":
        bot.send_message(message.chat.id, 'Hello, '+ message.chat.first_name +'. My name is Exodia. How can I help you?')
        sleep(1)
        handle_getme(message)
        sleep(1)
        bot.send_message(message.chat.id, "Would like to see the menu? You just need to click here: /menu")
        sleep(1)
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
        sleep(1)
        handle_getme(message)
        sleep(1)
        bot.reply_to(message, "Would like to see the menu? You just need to click here: /menu")
        sleep(1)
        bot.send_message(message.chat.id, "But before starting...")
        handle_choose_animal(message)

    
    

# Handles all text messages that contains the command '/help'.
@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.reply_to(message, "How can I help you?")
    sleep(1)
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
        #'10) Show me the Keyboard - not a command but something you should type\n'+
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
            with open('/home/gta/Desktop/danyel/bot/arquivos-bot/getmes.txt','a') as new_file:
                new_file.write(str(message.chat.first_name)+": "+str(message.chat.id)+'\n')
            bot.send_message(Danyel, "XXX-ADMIM-MESSAGE-XXX: Someone just subscribed! "+message.chat.first_name+ " joined")
            bot.reply_to(message, "I just saved your chat id for further interactions")

    
    if message.chat.type == "group":
        if message.chat.title in getmes:
            bot.reply_to(message, "I already have your chat id for further interactions")
        else:
            getmes[str(message.chat.title)]=str(message.chat.id)
            with open('/home/gta/Desktop/danyel/bot/arquivos-bot/getmes.txt','a') as new_file:
                new_file.write('Group '+str(message.chat.title)+": "+str(message.chat.id)+'\n')
            bot.send_message(Danyel, "XXX-ADMIM-MESSAGE-XXX: Someone just subscribed! "+message.chat.title+ " joined")
            bot.reply_to(message, "I just saved your chat id for further interactions")



# Handles all text messages that contains the command '/about'.
@bot.message_handler(commands=['about'])
def handle_about(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Message the developer', url='telegram.me/DanyelC'))
    bot.send_message(message.chat.id,sobre,reply_markup=keyboard)
    


# Handles all text messages that contains the command '/play'.
@bot.message_handler(commands=['play', 'score'])
def handle_play_score(message):
    if message.text == "/score":
            if str(message.chat.first_name) in contagem:
                bot.reply_to(message, "Your score is %d and mine is %d" % (contagem[str(message.chat.first_name)], contagem[str(message.chat.first_name)+'Exodia']))
            else: 
                bot.reply_to(message, "We haven't played ... yet. Lets play now! Click here: /play")

    elif message.text == "/play":
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

    

@bot.message_handler(commands=['contagem'])
def handle_admin_contagem(message):
    if message.chat.id == Danyel:
        if message.chat.first_name == 'Danyel':
            if contagem:
                for x, y in contagem.items():
                    bot.send_message(message.chat.id, x)
                    bot.send_message(message.chat.id, y)
                    bot.send_message(message.chat.id, "----------------")
            else: bot.send_message(message.chat.id, "Nothing, Sir")



@bot.message_handler(commands=['animals'])
def handle_admin_animals(message):
    if message.chat.id == Danyel:
        if message.chat.first_name == 'Danyel':
            if animals:
                for x, y in animals.items():
                    bot.send_message(message.chat.id, x)
                    bot.send_message(message.chat.id, y)
                    bot.send_message(message.chat.id, "----------------")
            else: bot.send_message(message.chat.id, "Nothing, Sir")



@bot.message_handler(commands=['getmes'])
def handle_adminhozinho(message):
    if message.chat.id == Danyel:
        if message.chat.first_name == 'Danyel':
            if getmes:
                for x, y in getmes.items():
                    bot.send_message(message.chat.id, x)
                    bot.send_message(message.chat.id, y)
                    bot.send_message(message.chat.id, "----------------")
            else: bot.send_message(message.chat.id, "Nothing, Sir")


@bot.message_handler(commands=['ungetmes'])
def handle_adminhozinho(message):
    if message.chat.id == Danyel:
        if message.chat.first_name == 'Danyel':
            if ungetmes:
                for x, y in ungetmes.items():
                    bot.send_message(message.chat.id, x)
                    bot.send_message(message.chat.id, y)
                    bot.send_message(message.chat.id, "----------------")
            else: bot.send_message(message.chat.id, "Nothing, Sir")



# ADMIN STUFF BRO ---------------------------------------------------------------------------------------------------

# Handles all text messages that contains the command '/menu'.
@bot.message_handler(commands=['menu'])
def handle_menu(message):
    bot.send_message(message.chat.id, "A list of commands:")
    if message.chat.id == Danyel:
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
        #'10) Show me the Keyboard - not a command but something you should type\n'+
        'Future features:\n'+
        'Coming soon!\n')
    


@bot.message_handler(commands=['myfriend'])
def handle_aboutme(message):
    if str(message.chat.first_name) in animals:
        bot.reply_to(message, "Your friend is: "+ animals[message.chat.first_name])
    else:
        bot.send_message(message.chat.id, "You should choose a friend first. Type \start again")

# Handles all photos received
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    if message.chat.type == "private":
        bot.reply_to(message, "Nice! I'm going to upload your photo now. Do you want to see some cards?")
        _10 = random.randint(1, 10)
        _10 = str(_10)
        foto= "index"+_10+".jpeg"
        photox = open('/home/gta/Desktop/danyel/bot/fotos-aleatorias/'+foto, 'rb')
        bot.send_photo(message.chat.id, photox)
        _10 = random.randint(1, 5)
        _10 = str(_10)
        foto= "index"+_10+".jpeg"
        raw = message.photo[1].file_id
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
        _10 = random.randint(1, 5)
        _10 = str(_10)
        foto= "index"+_10+".jpeg"
        photox = open('/home/gta/Desktop/danyel/bot/fotos-aleatorias/'+foto, 'rb')
        bot.send_photo(message.chat.id, photox)
        _10 = random.randint(1, 5)
        _10 = str(_10)
        foto= "index"+_10+".jpeg"
        raw = message.document.file_id
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        nome_arq = str(raw)
        with open('/home/gta/Desktop/danyel/bot/arquivos-bot/'+message.chat.first_name+nome_arq,'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_message(message.chat.id,"Done! I've just downloaded your file, "+message.chat.first_name)

# Handles all videos and audio files
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

def handle_choose_animal(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard= True)
    catx = types.KeyboardButton('Cat')
    dogx = types.KeyboardButton('Dog')
    parrotx = types.KeyboardButton('Parrot')
    duckx = types.KeyboardButton('Duck')
    geckox = types.KeyboardButton('Gecko')
    chameleonx = types.KeyboardButton('Chameleon')
    markup.row(catx, dogx, chameleonx)
    markup.row(parrotx, duckx, geckox)

    if message.chat.type == "group":
        bot.send_message(message.chat.id, "You are going to choose a friend to the group chat, not only for you")
        sleep(2)
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
    bot.send_message(message.chat.id, str(the_animal))

    if the_animal == 'Chameleon':
        photox = open('/home/gta/Desktop/danyel/bot/fotos-aleatorias/chameleon.jpg', 'rb')
        bot.send_photo(message.chat.id, photox)

        confirm_animal = bot.send_message(message.chat.id, "Would you like to have this buddy as your friend?", reply_markup=markup)

        bot.register_next_step_handler(confirm_animal , step_animal_confirmation, "Chameleon")
       
        

    if the_animal == 'Cat':
        photox = open('/home/gta/Desktop/danyel/bot/fotos-aleatorias/cat.jpg', 'rb')
        bot.send_photo(message.chat.id, photox)

        confirm_animal = bot.send_message(message.chat.id, "Would you like to have this buddy as your friend?", reply_markup=markup)

        bot.register_next_step_handler(confirm_animal , step_animal_confirmation, "Cat")

        
        
    if the_animal == 'Dog':
        photox = open('/home/gta/Desktop/danyel/bot/fotos-aleatorias/dog.jpg', 'rb')
        bot.send_photo(message.chat.id, photox)

        confirm_animal = bot.send_message(message.chat.id, "Would you like to have this buddy as your friend?", reply_markup=markup)

        bot.register_next_step_handler(confirm_animal , step_animal_confirmation, "Dog")

        
        
    if the_animal == 'Parrot':
        photox = open('/home/gta/Desktop/danyel/bot/fotos-aleatorias/parrot.jpg', 'rb')
        bot.send_photo(message.chat.id, photox)

        confirm_animal = bot.send_message(message.chat.id, "Would you like to have this buddy as your friend?", reply_markup=markup)

        bot.register_next_step_handler(confirm_animal , step_animal_confirmation, "Parrot")

        
        
    if the_animal == 'Duck':
        photox = open('/home/gta/Desktop/danyel/bot/fotos-aleatorias/duck.jpeg', 'rb')
        bot.send_photo(message.chat.id, photox)

        confirm_animal = bot.send_message(message.chat.id, "Would you like to have this buddy as your friend?", reply_markup=markup)

        bot.register_next_step_handler(confirm_animal , step_animal_confirmation, "Duck")

        
        
    if the_animal == 'Gecko':
        photox = open('/home/gta/Desktop/danyel/bot/fotos-aleatorias/gecko.jpg', 'rb')
        bot.send_photo(message.chat.id, photox)

        confirm_animal = bot.send_message(message.chat.id, "Would you like to have this buddy as your friend?", reply_markup=markup)

        bot.register_next_step_handler(confirm_animal , step_animal_confirmation, "Gecko")
        
    #if message.text.lower() == 'thanks' or 'thank you' or 'ty' or if 'than' in message.text.lower():
    #if 'thank' in message.text.lower() or message.text.lower() =='ty':
    #    bot.send_message(message.chat.id, ":)")


#confirm your friend (or not)
def step_animal_confirmation(message, animal):
    confirm_animal = message.text
    if confirm_animal == "YES!":
        if animal == "Chameleon":
            if message.chat.type == "group":
                if str('Group: '+message.chat.title) in animals:
                    bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
                else:
                    animals[str('Group: '+message.chat.title)]= 'Chameleon'
                    with open('/home/gta/Desktop/danyel/bot/arquivos-bot/animals.txt','a') as new_file:
                        new_file.write('Group '+str(message.chat.title)+": "+'Chameleon\n')
                    bot.send_message(message.chat.id, "Nice!! Take 2")
                    bot.send_message(message.chat.id, "Now you are ready to start your journey :)")
            else:       
                if str(message.chat.first_name) in animals:
                    bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
                else:
                    animals[str(message.chat.first_name)]= 'Chameleon'
                    with open('/home/gta/Desktop/danyel/bot/arquivos-bot/animals.txt','a') as new_file:
                        new_file.write('Group '+str(message.chat.first_name)+": "+'Chameleon\n')
                    bot.send_message(message.chat.id, "Nice!! Take 2")
                    bot.send_message(message.chat.id, "Now you are ready to start your journey :)")
        
        if animal == "Cat":
            if message.chat.type == "group":
                if str('Group: '+message.chat.title) in animals:
                    bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
                else:
                    animals[str('Group: '+message.chat.title)]= 'Cat'
                    with open('/home/gta/Desktop/danyel/bot/arquivos-bot/animals.txt','a') as new_file:
                        new_file.write('Group '+str(message.chat.title)+": "+'Cat\n')
                    bot.send_message(message.chat.id, "Nice!")
                    bot.send_message(message.chat.id, "Now you are ready to start your journey :)")
            else:
                if str(message.chat.first_name) in animals:
                    bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
                else:
                    animals[str(message.chat.first_name)]= 'Cat'
                    with open('/home/gta/Desktop/danyel/bot/arquivos-bot/animals.txt','a') as new_file:
                        new_file.write('Group '+str(message.chat.first_name)+": "+'Dog\n')
                    bot.send_message(message.chat.id, "Nice!")
                    bot.send_message(message.chat.id, "Now you are ready to start your journey :)")


        if animal == "Dog":
            if message.chat.type == "group":
                if str('Group: '+message.chat.title) in animals:
                    bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
                else:
                    animals[str('Group: '+message.chat.title)]= 'Dog'
                    with open('/home/gta/Desktop/danyel/bot/arquivos-bot/animals.txt','a') as new_file:
                        new_file.write('Group '+str(message.chat.title)+": "+'Dog\n')
                    bot.send_message(message.chat.id, "Nice!! Take 6, you have an army now haha")
                    bot.send_message(message.chat.id, "Now you are ready to start your journey :)")
            else:
                if str(message.chat.first_name) in animals:
                    bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
                else:
                    animals[str(message.chat.first_name)]= 'Dog'
                    with open('/home/gta/Desktop/danyel/bot/arquivos-bot/animals.txt','a') as new_file:
                        new_file.write('Group '+str(message.chat.first_name)+": "+'Dog\n')
                    bot.send_message(message.chat.id, "Nice!! Take 6, you have an army now haha")
                    bot.send_message(message.chat.id, "Now you are ready to start your journey :)")

        if animal == "Parrot":
            if message.chat.type == "group":
                if str('Group: '+message.chat.title) in animals:
                    bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
                else:
                    animals[str('Group: '+message.chat.title)]= 'Parrot'
                    with open('/home/gta/Desktop/danyel/bot/arquivos-bot/animals.txt','a') as new_file:
                        new_file.write('Group '+str(message.chat.title)+": "+'Parrot\n')
                    bot.send_message(message.chat.id, "Nice!!!")
                    bot.send_message(message.chat.id, "Now you are ready to start your journey :)")
            else:
                if str(message.chat.first_name) in animals:
                    bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
                else:
                    animals[str(message.chat.first_name)]= 'Parrot'
                    with open('/home/gta/Desktop/danyel/bot/arquivos-bot/animals.txt','a') as new_file:
                        new_file.write('Group '+str(message.chat.first_name)+": "+'Parrot\n')
                    bot.send_message(message.chat.id, "Nice!!!")
                    bot.send_message(message.chat.id, "Now you are ready to start your journey :)")

        if animal == "Duck":
            if message.chat.type == "group":
                if str('Group: '+message.chat.title) in animals:
                    bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
                else:
                    animals[str('Group: '+message.chat.title)]= 'Duck'
                    with open('/home/gta/Desktop/danyel/bot/arquivos-bot/animals.txt','a') as new_file:
                        new_file.write('Group '+str(message.chat.title)+": "+'Duck\n')
                    bot.send_message(message.chat.id, "WTF...")
                    bot.send_message(message.chat.id, "Now you are ready to start your journey :)")
            else:
                if str(message.chat.first_name) in animals:
                    bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
                else:
                    animals[str(message.chat.first_name)]= 'Duck'
                    with open('/home/gta/Desktop/danyel/bot/arquivos-bot/animals.txt','a') as new_file:
                        new_file.write('Group '+str(message.chat.first_name)+": "+'Duck\n')
                    bot.send_message(message.chat.id, "WTF...")
                    bot.send_message(message.chat.id, "Now you are ready to start your journey :)")

        if animal == "Gecko":
            if message.chat.type == "group":
                if str('Group: '+message.chat.title) in animals:
                    bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
                else:
                    animals[str('Group: '+message.chat.title)]= 'Gecko'
                    with open('/home/gta/Desktop/danyel/bot/arquivos-bot/animals.txt','a') as new_file:
                        new_file.write('Group '+str(message.chat.title)+": "+'Gecko\n')
                    bot.send_message(message.chat.id, "How cute!")
                    bot.send_message(message.chat.id, "Now you are ready to start your journey :)")
            else:
                if str(message.chat.first_name) in animals:
                    bot.send_message(message.chat.id, "You already have your friend, but you can take a look:")
                else:
                    animals[str(message.chat.first_name)]= 'Gecko'
                    with open('/home/gta/Desktop/danyel/bot/arquivos-bot/animals.txt','a') as new_file:
                        new_file.write('Group '+str(message.chat.first_name)+": "+'Gecko\n')
                    bot.send_message(message.chat.id, "How cute!")
                    bot.send_message(message.chat.id, "Now you are ready to start your journey :)")
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

print('Exodia, Obliterate!')
bot.polling()