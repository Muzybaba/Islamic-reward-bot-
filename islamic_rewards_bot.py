from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler
import random
import os

TOKEN = ''

duas = [
    "Allahumma ajirni minan-naar",
    "Rabbi ishrah li sadri",
    "Allahumma inni a'udhu bika minal hammi wal hazan"
]

hadiths = [
    "Actions are according to their intentions.",
    "The strong believer is better than the weak believer.",
    "Whoever says 'La ilaha illallah' will enter Paradise."
]

quiz_questions = {
    "What is the name of the first surah in the Quran?": {
        "A) Al-Fatihah": True,
        "B) Al-Baqarah": False,
        "C) Al-Imran": False
    },
    "Who is the last prophet sent by Allah?": {
        "A) Prophet Muhammad (PBUH)": True,
        "B) Prophet Jesus": False,
        "C) Prophet Moses": False
    }
}

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Assalamu alaykum! Welcome to Islamic Rewards Bot.')

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Use /dua for a random dua, /hadith for a random hadith, or /quiz to start a quiz.')

def dua(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(duas))

def hadith(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(hadiths))

def quiz(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Quiz started! Here\'s your first question:')
    question = random.choice(list(quiz_questions.keys()))
    context.bot.send_message(chat_id=update.effective_chat.id, text=question)
    for option, correct in quiz_questions[question].items():
        context.bot.send_message(chat_id=update.effective_chat.id, text=option)

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('dua', dua))
    dp.add_handler(CommandHandler('hadith', hadith))
    dp.add_handler(CommandHandler('quiz', quiz))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
