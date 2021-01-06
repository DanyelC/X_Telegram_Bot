# -*- coding: utf-8 -*-
import requests as requests
import random

url = "https://api.telegram.org/bot1147645813:AAHbIB78oyWUwz_JYT3pFaKgEjCPsOL2hhQ/"


# create func that get chat id
def get_chat_id(update):
    chat_id = update['message']["chat"]["id"]
    return chat_id

# create func that get chat id query
#def get_chat_id2(update):
#    chat_id = update["inline_query_id"]
#    return chat_id

# create function that get message text
def get_message_text(update):
    message_text = update["message"]["text"]
    return message_text
    

# create function that get message text in query
#def get_message_text_query(update):
#    message_text_query = update["inline_query_id"]["query"]
#    return message_text_query    

# create function that get last_update
def last_update(req):
    response = requests.get(req + "getUpdates")
    response = response.json()
    result = response["result"]
    total_updates = len(result) - 1
    return result[total_updates]  # get last record message update


# create function that let bot send message to user
def send_message(chat_id, message_text):
    params = {"chat_id": chat_id, "text": message_text}
    response = requests.post(url + "sendMessage", data=params)
    return response

# create function that let bot send message to user (query)
#def send_message2(chat_id, message_text_query):
#    params = {"inline_query_id": chat_id, "text": message_text_query}
#    response = requests.post(url + "sendMessage", data=params)
#   return response


# create main function for navigate or reply message back
def main():
    update_id = last_update(url)["update_id"]
    while True:
        update = last_update(url)
        if update_id == update["update_id"]:
            if get_message_text(update).lower() == "oi" or get_message_text(update).lower() == "ola" or "xodia" in get_message_text(update).lower():
                send_message(get_chat_id(update), 'Hello, '+ update['message']['chat']['first_name'] +'. My name is Exodia. How can I help you? We can roll some dices! Type "Play" to roll the dice!')
            elif get_message_text(update).lower() == "play":
                _1 = random.randint(1, 6)
                _2 = random.randint(1, 6)
                _3 = random.randint(1, 6)
                _4 = random.randint(1, 6)
                _5 = random.randint(1, 6)
                _6 = random.randint(1, 6)
                send_message(get_chat_id(update),
                             'You have ' + str(_1) + ' and ' + str(_2) + ' and ' + str(_3) + ' !\n Your result is ' +
                             str(_1 + _2 + _3) + '!!!')

                send_message(get_chat_id(update),
                             'I have ' + str(_4) + ' and ' + str(_5) + ' and ' + str(_6) + ' !\n My result is ' +
                             str(_4 + _5 + _6) + '!!!')

                if _1 + _2 + _3 == _4 + _5 + _6: torneio = "nobody won, sorry"
                if _1 + _2 + _3 > _4 + _5 + _6: torneio = "You won...shit"
                if _1 + _2 + _3 < _4 + _5 + _6: torneio = "I won!!!"

                send_message(get_chat_id(update),
                             'Well...'+ torneio)
            else:
                send_message(get_chat_id(update), "Sorry Not Understand what you inputted :(")

#            if get_message_text_query: send_message2(get_chat_id2(update),"message_text_query")
            update_id += 1


# call the function to make it reply
main()