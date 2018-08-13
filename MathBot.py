from MathBotHandlers import createHandlers
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# logging
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(token='671411814:AAEvJ3pmx3ZkEmHoCDnnpeedB9i7NJnehZY')
dispatcher = updater.dispatcher
createHandlers(dispatcher)
updater.start_polling()
