import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Robô 24h ONLINE!")

async def iniciar_bot():
    print("🚀 Iniciando Telegram (v20 puro)")

    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_TOKEN não encontrado")

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))

    print("🟢 Bot rodando em polling (processo vivo)")
    await app.run_polling()
