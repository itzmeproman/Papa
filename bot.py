import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "6154222206:AAFxkaTRgMI52biIT3m4qAUDwsWIySnoY2c"

def start(update, context):
    update.message.reply_text('Hello! I am a bot that adds "provided by @Anime_Compass" at the end of the file name.')

def handle_document(update, context):
    file = update.message.document
    new_file_name = file.file_name + ' provided by @Anime_Compass'
    file.download(custom_path=new_file_name)
    update.message.reply_document(open(new_file_name, 'rb'), filename=new_file_name)

updater = Updater(TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.document, handle_document))

updater.start_polling()
updater.idle()
