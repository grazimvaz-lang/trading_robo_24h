import os
import asyncio
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

BOT_LIGADO = False

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bot online!\n\n"
        "/ligar\n"
        "/desligar\n"
        "/status"
    )

async def ligar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global BOT_LIGADO
    BOT_LIGADO = True
    await update.message.reply_text("✅ Robô LIGADO")

async def desligar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global BOT_LIGADO
    BOT_LIGADO = False
    await update.message.reply_text("⛔ Robô DESLIGADO")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"📌 Status: {'LIGADO' if BOT_LIGADO else 'DESLIGADO'}"
    )

async def loop_24h():
    while True:
        if BOT_LIGADO:
            print("🔁 Robô rodando 24h...")
            # aqui entra depois sua lógica de trading
        await asyncio.sleep(5)

async def iniciar_bot():
    if not TOKEN:
        raise RuntimeError("TELEGRAM_TOKEN não definido no Railway")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ligar", ligar))
    app.add_handler(CommandHandler("desligar", desligar))
    app.add_handler(CommandHandler("status", status))

    asyncio.create_task(loop_24h())

    print("🚀 Bot Telegram em polling 24h")

    await app.initialize()
    await app.start()
    await app.updater.start_polling(drop_pending_updates=True)

    await asyncio.Event().wait()  # SEGURA O PROCESSO

