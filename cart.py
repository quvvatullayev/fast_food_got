from telegram.ext import CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from db import DB

db = DB('db.json')

class Cart:
    def add_cart(self, update: Update, context: CallbackContext):
        query = update.callback_query
        bot = context.bot
        chat_id = query.message.chat_id
        product_id = int(query.data.split("_")[-1])
        n = db.add_cart(chat_id, product_id)
        reply_markup = [
            [
                InlineKeyboardButton('-', callback_data=f"minus_{product_id}"),
                InlineKeyboardButton(f'{n}', callback_data=f"n"),
                InlineKeyboardButton('+', callback_data=f"plus_{product_id}")
            ],
            [
                InlineKeyboardButton('add to cart', callback_data=f"to")
            ]
        ]

        reply_markup = InlineKeyboardMarkup(reply_markup)

        bot.edit_message_reply_markup(reply_markup=reply_markup, chat_id=chat_id, message_id=query.message.message_id)