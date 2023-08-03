from telegram.ext import CallbackContext, CommandHandler, Updater, MessageHandler, Filters, CallbackQueryHandler
from start import Start
from category import Category
from sub_category import Sub_Category
from product import Product
from cart import Cart

start = Start()
category = Category()
sub_category = Sub_Category()
product = Product()
cart = Cart()


token = '5677023630:AAHkbfD1-l1RWMw7Q56_wBQKR4XzHXunVjs'
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start.start))
dispatcher.add_handler(MessageHandler(Filters.text("Category"), category.category_list))
dispatcher.add_handler(CallbackQueryHandler(sub_category.sub_category_list, pattern='category_'))
dispatcher.add_handler(CallbackQueryHandler(product.product_detil, pattern='sub_category_'))
dispatcher.add_handler(CallbackQueryHandler(product.nex_product, pattern='next_'))
dispatcher.add_handler(CallbackQueryHandler(product.back_product, pattern='back_'))
dispatcher.add_handler(CallbackQueryHandler(sub_category.back_sub_category_list, pattern='sub_back_category_'))
dispatcher.add_handler(CallbackQueryHandler(category.back_category_list, pattern='list_category_back'))
dispatcher.add_handler(CallbackQueryHandler(cart.add_cart, pattern='add_to_cart_'))
dispatcher.add_handler(CallbackQueryHandler(cart.add_plus, pattern='plus_'))
dispatcher.add_handler(CallbackQueryHandler(cart.add_minus, pattern='minus_'))


updater.start_polling()
updater.idle()