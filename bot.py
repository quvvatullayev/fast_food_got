from telegram.ext import CallbackContext, CommandHandler, Updater, MessageHandler, Filters
from start import Start
from category import Category

start = Start()
category = Category()

token = '5677023630:AAHkbfD1-l1RWMw7Q56_wBQKR4XzHXunVjs'
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start.start))
dispatcher.add_handler(MessageHandler(Filters.text("Category"), category.category_list))

updater.start_polling()
updater.idle()