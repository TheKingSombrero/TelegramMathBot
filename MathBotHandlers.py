from telegram.ext import CommandHandler, MessageHandler, Filters
import matplotlib.pyplot as plt
from numpy import linspace
import math
from os import remove


def createHandlers(dispatcher):
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    '''echo_handler = MessageHandler(Filters.text, echo)
    dispatcher.add_handler(echo_handler)
    caps_handler = CommandHandler('caps', caps, pass_args=True)
    dispatcher.add_handler(caps_handler)'''
    sin_handler = CommandHandler('sin', sinus, pass_args=True)
    dispatcher.add_handler(sin_handler)
    cos_handler = CommandHandler('cos', cosinus, pass_args=True)
    dispatcher.add_handler(cos_handler)
    quad_handler = CommandHandler('quad', quad, pass_args=True)
    dispatcher.add_handler(quad_handler)
    trig_handler = CommandHandler('trig', trig)
    dispatcher.add_handler(trig_handler)
    # LAST ENTRY
    dispatcher.add_handler(MessageHandler([Filters.command], unknown))


def start(bot, update):
    print("printing start")
    bot.send_message(chat_id=update.message.chat_id, text=startmessage)


def sinus(bot, update, args):
    try:
        val = float(args[0])
    except IndexError:
        bot.send_message(chat_id=update.message.chat_id, text='You must specify a value')
        return
    val = float(args[0])
    sinus = (math.sin(math.radians(val)))
    bot.send_message(chat_id=update.message.chat_id, text='sinus is {}'.format(sinus))


def cosinus(bot, update, args):
    try:
        val = float(args[0])
    except IndexError:
        bot.send_message(chat_id=update.message.chat_id, text='You must specify a value')
        return
    val = float(args[0])
    cosinus = (math.cos(math.radians(val)))
    bot.send_message(chat_id=update.message.chat_id, text='cosinus is {}'.format(cosinus))


def tangens(bot, update, args):
    try:
        val = float(args[0])
    except IndexError:
        bot.send_message(chat_id=update.message.chat_id, text='You must specify a value')
        return
    val = float(args[0])
    tangens = (math.tan(math.radians(val)))
    bot.send_message(chat_id=update.message.chat_id, text='tangens is {}'.format(tangens))


def quad(bot, update, args):
    try:
        a: float = float(args[0])
        b = float(args[1])
        c = float(args[2])
    except IndexError:
        bot.send_message(chat_id=update.message.chat_id, text='Must enter 3 coefficents')
        return
    a: float = float(args[0])
    b: float = float(args[1])
    c:float  = float(args[2])
    det = b ** 2 - (4 * a * c)

    if det < 0:
        bot.send_message(chat_id=update.message.chat_id, text='Solutions are complex!')
        return
    else:
        x1 = (-1 * b + math.sqrt(det)) / (2 * a)
        x2 = (-1 * b - math.sqrt(det)) / (2 * a)
        bot.send_message(chat_id=update.message.chat_id, text='X1={}, X2={}'.format(x1, x2))
    t = linspace(-20, 20, 100)
    markers_on = [x1, x2,c]
    ty = []
    for _ in t:
        y = a * (_) ** 2 + (b * _) + c
        ty.append((a * (_ ** 2) + (b * _) + c))
    fig, ax = plt.subplots()
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.plot(t,ty,'-gD')
    plt.savefig('plot.png') #Save plot of function to file
    bot.send_photo(chat_id=update.message.chat_id, photo=open('plot.png', 'rb')) #Send it
    remove("plot.png") #Delete file


def trig(bot, update):
    bot.send_photo(chat_id=update.message.chat_id, photo=open('trigonometry-laws-and-identities-1.png', 'rb'))


def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")


startmessage = "Welcome to the MathBot \n" \
               "Commands:\n" \
               "/sin α - sinus of degrees\n" \
               "/cos α - cosinus of degrees\n" \
               "/tan α - tangens of degrees\n" \
               "/quad a b c -Quadratic equation solver\n" \
               "/trig - Sends a picture of trigonometric identities"
