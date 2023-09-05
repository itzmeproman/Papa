# Import the required modules
import os
import telebot
from telebot import types

# Get the bot token and app name from environment variables
TOKEN = "6154222206:AAFxkaTRgMI52biIT3m4qAUDwsWIySnoY2c"
APP_NAME = "itzmeproman"

# Create a bot instance
bot = telebot.TeleBot(TOKEN)

# Define a handler for /start command
@bot.message_handler(commands=["start"])
def start(message):
    # Send a welcome message to the user
    bot.send_message(message.chat.id, "Hello, I am a bot that can add 'provided by @Anime_Compass' at the end of the file name. Send me any file and I will do it for you.")

# Define a handler for any file type
@bot.message_handler(content_types=["document", "audio", "video", "photo"])
def handle_file(message):
    # Get the file id and name from the message
    file_id = message.document.file_id if message.document else message.audio.file_id if message.audio else message.video.file_id if message.video else message.photo[-1].file_id if message.photo else None
    file_name = message.document.file_name if message.document else message.audio.title if message.audio else message.video.file_name if message.video else None

    # Check if the file id and name are valid
    if file_id and file_name:
        # Check if the file is in mp4 or mkv format
        file_extension = os.path.splitext(file_name)[1]
        if file_extension in [".mp4", ".mkv"]:
            # Add 'provided by @Anime_Compass' at the end of the file name
            new_file_name = file_name + " (provided by @Anime_Compass)"

            # Download the file from Telegram server
            file_info = bot.get_file(file_id)
            downloaded_file = bot.download_file(file_info.file_path)

            # Create a new file object with the new name
            new_file = types.InputFile(new_file_name, downloaded_file)

            # Send the new file to the user
            bot.send_document(message.chat.id, new_file)
        else:
            # Send an error message to the user
            bot.send_message(message.chat.id, "Sorry, I can only process files in mp4 or mkv format. Please send me a valid file.")
    else:
        # Send an error message to the user
        bot.send_message(message.chat.id, "Sorry, I could not process your file. Please make sure it has a valid name and type.")
        
# Run the bot on Heroku server
bot.polling()
            
