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

    def back_category_list(self, update: Update, context: CallbackContext):
        query = update.callback_query
        bot = context.bot
        chat_id = query.message.chat_id
        data = db.get_category_list()

        reply_markup = []

        for category in data:
            reply_markup.append([
                InlineKeyboardButton(category['name'], callback_data=f"category_{category['id']}")
            ])

        reply_markup = InlineKeyboardMarkup(reply_markup)
        query.bot.edit_message_reply_markup(reply_markup=None, chat_id=chat_id, message_id=query.message.message_id)
        bot.send_message(chat_id=chat_id, text="Category List", reply_markup=reply_markup)
        
        