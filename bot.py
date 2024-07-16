from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Ganti 'YOUR_API_TOKEN' dengan token API dari BotFather
TOKEN = 'YOUR_API_TOKEN'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot.')

def main():
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
