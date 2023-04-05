#1739013133:AAH0gFLM5zUy7JH1CQmvewE1tIH7R07xUCk
from telegram import *
from telegram.ext import *
from chatterbot import ChatBot
import analyser.reply_generator as ds

BOT_TOKEN = 6212580248:AAFxVPGRDgz0k4vYbSkE_bwv7E5id0D6YqU

bot = Bot(BOT_TOKEN)
updater = Updater(BOT_TOKEN,use_context = True)
dispatcher = updater.dispatcher

chatbot = ChatBot('Quotes Bot',read_only = True, logic_adapters=[
        "chatterbot.logic.BestMatch","chatterbot.logic.MathematicalEvaluation"
    ])


def test_function(update:Update,context:CallbackContext):
    texts = str(ds.get_response(update.message.text))
    print(texts)
    bot.send_message(
        chat_id = update.effective_chat.id,
        text = texts
    )



start_value = MessageHandler(filters=Filters.all, callback=test_function)
dispatcher.add_handler(start_value)
updater.start_polling()


