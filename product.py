from telegram.ext import CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from db import DB

db = DB('db.json')

class Product:
    def __init__(self) -> None:
        self.base_url = "http://127.0.0.1:8000"
    def product_detil(self, update: Update, context: CallbackContext):
        query = update.callback_query
        bot = context.bot
        chat_id = query.message.chat_id
        sub_category_id = query.data.split("_")[2]
        db.add_product_to_db(sub_category_id, chat_id)
        data = db.get_product_detail(chat_id)

        reply_markup = []
        reply_markup.append([
            InlineKeyboardButton(data['name'], callback_data=f"product_{data['id']}")
        ])

        imge = self.base_url+data['img']
        reply_markup = InlineKeyboardMarkup(reply_markup)
        query.bot.send_photo(chat_id=chat_id, photo=imge, caption=data['name'], reply_markup=reply_markup)