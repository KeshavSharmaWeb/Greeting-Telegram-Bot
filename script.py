# pip install pyTelegramBotAPI

import json
from telebot import types
import telebot
token = "ENTER-YOUR-ACCESS-TOKEN-HERE"

bot = telebot.TeleBot(token)

def greet_user(messages):
    for message in messages:
        for new_member in message.new_chat_members:
            bot.send_message(message.chat.id, f'Welcome {new_member.first_name} to the group!')
			
			
bot.set_update_listener(greet_user)
if __name__ == '__main__':
	bot.infinity_polling()
	
