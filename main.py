import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

from handlers.intents import handle_intents
from handlers.basic import fallback_answer
from calculator import number

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    response = handle_intents(text)

    if not response:
        response = fallback_answer(text)

    await update.message.reply_text(response)
    
    random_number = number()
    print (random_number)
    await update.message.reply_text(f"Твой код: {random_number}")
    

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()