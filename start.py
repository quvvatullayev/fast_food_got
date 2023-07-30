from telegram.ext import CallbackContext, Updater
from telegram import ReplyKeyboardMarkup, KeyboardButton

class Start:

    def start(self, update: Updater, context: CallbackContext):
        bot = context.bot
        chat_id = update.message.chat_id
        text = "Welcome to the bot"
        keyboard = [
            [KeyboardButton("Category")]
        ]

        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        
        
        bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup)
