from telegram.ext import CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from db import DB

db = DB('db.json')

class Sub_Category:
    def sub_category_list(self, update: Update, context: CallbackContext):
        query = update.callback_query
        bot = context.bot
        chat_id = query.message.chat_id
        category_id = query.data.split("_")[1]
        data = db.get_subcategory_list(category_id)

        reply_markup = []
        
        for sub_category in data:
            reply_markup.append([
                InlineKeyboardButton(sub_category['name'], callback_data=f"sub_category_{category_id}_{sub_category['id']}")
            ])

        reply_markup = InlineKeyboardMarkup(reply_markup)
        query.edit_message_text(text="Sub Category List", reply_markup=reply_markup)

    def back_sub_category_list(self, update: Update, context: CallbackContext):
        query = update.callback_query
        bot = context.bot
        chat_id = query.message.chat_id
        category_id = query.data.split("_")[-1]
        data = db.get_subcategory_list(category_id)

        reply_markup = []
        
        for sub_category in data:
            reply_markup.append([
                InlineKeyboardButton(sub_category['name'], callback_data=f"sub_category_{category_id}_{sub_category['id']}")
            ])

        reply_markup = InlineKeyboardMarkup(reply_markup)
        query.bot.edit_message_reply_markup(reply_markup=None, chat_id=chat_id, message_id=query.message.message_id)
        bot.send_message(chat_id=chat_id, text="Sub Category List", reply_markup=reply_markup)

        