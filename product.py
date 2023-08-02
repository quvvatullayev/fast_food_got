from telegram.ext import CallbackContext, Updater
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from db import DB

db = DB('db.json')

class Product:
    def product_list(self, update: Updater, context: CallbackContext):
        query = update.callback_query
        bot = context.bot
        chat_id = query.message.chat_id
        category_id = query.data.split("_")[-1]
        data = db.get_product_list(category_id)

        reply_markup = []
        
        for product in data['products']:
            print(product)