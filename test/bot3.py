from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import File
import sys

def start(update, context):
	update.message.reply_text("Hello, my name is Exodia. How can I help you?")


def message(update,context):
	update.message.reply_text(f'Command:{update.message.text}')

def receive_image(update,context):
	try:
		obj = context.bot.getFile(file_id=update.message.document.file_id)
		obj.download()
		update.message.reply_text("I've just downloaded your file, Sir")
	except Exception as e:
		print(str(e))


#def receive_audio(update,context):
#    try:
#		audio_obj = context.bot.getFile(file_id=update.message.audio.file_id)
#		audio_obj.download()
#		update.message.reply_text("I've just downloaded your audio, Sir")
#	except Exception as ER:
#		print(str(ER))tete


def main(): #starting bot...
	updater = Updater("1147645813:AAHbIB78oyWUwz_JYT3pFaKgEjCPsOL2hhQ", use_context=True)
	dp.add_handler(CommandHandler("start",start))
	dp.add_handler(MessageHandler(Filters.text,message))
	dp.add_handler(MessageHandler(Filters.command,command_handler))
	dp.add_handler(MessageHandler(Filters.audio,receive_audio))
	dp.add_handler(MessageHandler(Filters.document.jpg,receive_image))
	dp.add_handler(MessageHandler(Filters.document.png,receive_image))
	updater.start_polling()
	updater.idle()


if __name__ == "__main__":
	main()


#def command_handling_fn(update,context): #update é a mensagem, context é o que voce  vai f$
#   context.bot.send_message(chat_id=update.effective_chat.id, text="Nice to see you here")

#if __name__ == "__main__":
#    updater = Updater(token = "1147645813:AAHbIB78oyWUwz_JYT3pFaKgEjCPsOL2hhQ", use_contex$
#    dispatcher = updater.dispatcher
#
#    handler = CommandHandler("start",command_handling_fn)
#
#    dispatcher.add_handler(handler)
#
#    updater.start_polling()

