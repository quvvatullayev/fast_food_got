from telegram.ext import CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from db import DB

db = DB('db.json')

class Category:
    def category_list(self, update: Update, context: CallbackContext):
        bot = context.bot
        chat_id = update.message.chat_id
        data = db.get_category_list()

        reply_markup = []

        for category in data:
            reply_markup.append([
                InlineKeyboardButton(category['name'], callback_data=f"category_{category['id']}")
            ])

        reply_markup = InlineKeyboardMarkup(reply_markup)
        bot.send_message(chat_id=chat_id, text="Category List", reply_markup=reply_markup)
        
        