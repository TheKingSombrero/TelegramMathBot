from MathBotHandlers import createHandlers
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# logging
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(token='Token')
dispatcher = updater.dispatcher
createHandlers(dispatcher)
updater.start_polling()
