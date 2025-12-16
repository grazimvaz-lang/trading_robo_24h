import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Robô 24h online e funcionando!")

def iniciar_bot():
    token = os.getenv("TELEGRAM_TOKEN")

    if not token:
        print("⚠️ TELEGRAM_TOKEN não configurado. Bot Telegram desativado.")
        return

    print("📲 Iniciando Bot do Telegram...")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
