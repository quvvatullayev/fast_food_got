from telegram.ext import CallbackContext, Updater
from telegram import ReplyKeyboardMarkup, KeyboardButton
from db import DB

db = DB('db.json')

class Category:
    def category_list(self, update: Updater, context: CallbackContext):
        bot = context.bot
        chat_id = update.message.chat_id
        data = db.get_category_list()
        text = ''
        for category in data:
            text += f"{category['id']}. {category['name']}\n"
        bot.send_message(chat_id=chat_id, text=text)