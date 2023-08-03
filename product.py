import telegram.ext as tg
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from db import DB

db = DB('db.json')

class Product:
    def __init__(self) -> None:
        self.base_url = "https://fastfoodbackend.pythonanywhere.com"

    def product_detil(self, update: Update, context: tg.CallbackContext):
        query = update.callback_query
        bot = context.bot
        chat_id = query.message.chat_id
        sub_category_id = query.data.split('_')[2]
        db.add_product_to_db(sub_category_id, chat_id)
        data,n,max_n = db.get_product_detail(chat_id)

        reply_markup = [
            [
                InlineKeyboardButton(f'{n}/{max_n}', callback_data=f'n')
            ],
            [
                InlineKeyboardButton('Back', callback_data=f'back_{n}'),
                InlineKeyboardButton('Add to cart', callback_data=f'add_to_cart_{data["id"]}'),
                InlineKeyboardButton('Next', callback_data=f'next_{n}')
            ]
        ]

        image = self.base_url + data['img']
        caption = f"name:{data['name']}" + '\n' + '\n' + f"price:{str(data['price'])}"
        reply_markup = InlineKeyboardMarkup(reply_markup)
        bot.send_photo(chat_id=chat_id, photo=image, caption=caption, reply_markup=reply_markup)

    def nex_product(self, update: Update, context: tg.CallbackContext):
        query = update.callback_query
        bot = context.bot
        chat_id = query.message.chat_id
        n = query.data.split('_')[1]
        data,n,max_n = db.next_product(chat_id, n)
        query.bot.edit_message_reply_markup(reply_markup=None, chat_id=chat_id, message_id=query.message.message_id)
        reply_markup = [
            [
                InlineKeyboardButton(f'{n}/{max_n}', callback_data=f'n')
            ],
            [
                InlineKeyboardButton('Back', callback_data=f'back_{n}'),
                InlineKeyboardButton('Add to cart', callback_data=f'add_to_cart_{data["id"]}'),
                InlineKeyboardButton('Next', callback_data=f'next_{n}')
            ]
        ]

        image = self.base_url + data['img']
        caption = f"name:{data['name']}" + '\n' + '\n' + f"price:{str(data['price'])}"
        reply_markup = InlineKeyboardMarkup(reply_markup)
        bot.send_photo(chat_id=chat_id, photo=image, caption=caption, reply_markup=reply_markup)

    def back_product(self, update: Update, context: tg.CallbackContext):
        query = update.callback_query
        bot = context.bot
        chat_id = query.message.chat_id
        n = query.data.split('_')[1]
        data,n,max_n = db.back_product(chat_id, n)
        query.bot.edit_message_reply_markup(reply_markup=None, chat_id=chat_id, message_id=query.message.message_id)
        reply_markup = [
            [
                InlineKeyboardButton(f'{n}/{max_n}', callback_data=f'n')
            ],
            [
                InlineKeyboardButton('Back', callback_data=f'back_{n}'),
                InlineKeyboardButton('Add to cart', callback_data=f'add_to_cart_{data["id"]}'),
                InlineKeyboardButton('Next', callback_data=f'next_{n}')
            ]
        ]

        image = self.base_url + data['img']
        caption = f"name:{data['name']}" + '\n' + '\n' + f"price:{str(data['price'])}"
        reply_markup = InlineKeyboardMarkup(reply_markup)
        bot.send_photo(chat_id=chat_id, photo=image, caption=caption, reply_markup=reply_markup)