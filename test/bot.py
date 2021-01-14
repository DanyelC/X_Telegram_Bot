# -*- coding: utf-8 -*-
import json
import requests
from time import sleep
from threading import Thread, Lock
import re

global config
config = {'url': 'https://api.telegram.org/bot1147645813:AAHbIB78oyWUwz_JYT3pFaKgEjCPsOL2hhQ/', 'lock': Lock(), 'url_file':'https://api.telegram.org/file/bot1147645813:AAHbIB78oyWUwz_JYT3pFaKgEjCPsOL2hhQ/'}


def del_update(data):
	global config	
	
	config['lock'].acquire()
	requests.post(config['url'] + 'getUpdates', {'offset': data['update_id']+1})
	config['lock'].release()

def send_message(data, msg):
	global config
	
	config['lock'].acquire()
	requests.post(config['url'] + 'sendMessage', {'chat_id': data['message']['chat']['id'], 'text': str(msg)})
	config['lock'].release()

def get_file(file_path):
	global config
	
	return requests.get(config['url_file'] + str(file_path)).content

def upload_file(data, file):
	global config	
	
	formatos = {'png': {'metodo': 'sendPhoto', 'send': 'photo'},
				'text': {'metodo': 'sendphoto', 'send': 'photo'} }
	
	return requests.post(config['url'] + formatos['text' if '.txt' in file else 'png']['metodo'], {'chat_id': data['message']['chat']['id']}, files={formatos['text' if '.txt' in file else 'png']['send']: open(file, 'rb')}).text

while True:
	
	x = ''
	while 'result' not in x:
		try:
			x = json.loads(requests.get(config['url'] + 'getUpdates').text)
		except Exception as e:
			x = ''
			if 'Failed to establish a new connection' in str(e):
				print('Falha na conexão com o servidor, tente novamente mais tarde')
			else:
				print('Erro desconhecido: ' + str(e))
	
	
	if len(x['result']) > 0:
		for data in x['result']:
			Thread(target=del_update, args=(data, )).start()
			
			
			if 'photo' in data['message']:
			
				print(json.dumps(data['message'], indent=1))
				
				#file = get_file(json.loads(requests.post(config['url'] + 'getFile?file_id=' + data['message']['photo']['file_id']).text)['result']['file_path'])
				#open(data['message']['photo']['file_name'], 'wb').write(file)
			
			#elif data['message']['text']== 'foto':
			#	print(upload_file(data, 'logo_canal.png'))
				
				
			#elif data['message']['text'] == 'texto':
			#	print(upload_file(data, 'photo_exemplo.txt'))		
			
			
			#else:			
			#	print(json.dumps(data, indent=1))

			if (data['message']):
				if "xodia" in (data['message']['text']).lower():
					Thread(target=send_message, args=(data, 'Ola, '+ data['message']['chat']['first_name'] +'. tudo bem? Como posso ajuda-lo?')).start()
		
		
		sleep(1.5)
