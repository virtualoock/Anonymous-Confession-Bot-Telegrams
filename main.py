import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
bot = Updater(token=TOKEN, use_context=True).bot

confessions = []

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome to the Anonymous Confession Bot! Share your confessions with the group.")

def confess(update: Update, context: CallbackContext) -> None:
    confession_text = update.message.text
    confessions.append(confession_text)

    update.message.reply_text("Your confession has been submitted anonymously.")

def view_confessions(update: Update, context: CallbackContext) -> None:
    if confessions:
        random.shuffle(confessions)
        confessions_text = "\n".join([f"{index + 1}. {confession}" for index, confession in enumerate(confessions)])
        update.message.reply_text(f"Anonymous Confessions (Randomized):\n{confessions_text}")
    else:
        update.message.reply_text("No confessions yet. Share yours!")

if __name__ == "__main__":
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, confess))
    dp.add_handler(CommandHandler("view_confessions", view_confessions))

    updater.start_polling()
    updater.idle()
