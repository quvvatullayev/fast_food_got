from telegram.ext import CallbackContext, CommandHandler, Updater
from start import Start

start = Start()

token = '5677023630:AAHkbfD1-l1RWMw7Q56_wBQKR4XzHXunVjs'
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start.start))

updater.start_polling()
updater.idle()