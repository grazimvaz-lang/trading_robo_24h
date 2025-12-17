import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

BOT_LIGADO = False
TOKEN = os.getenv("TELEGRAM_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Robô online!\n\n"
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


def loop_24h(context: ContextTypes.DEFAULT_TYPE):
    if BOT_LIGADO:
        print("🔁 Robô rodando 24h...")


def iniciar_bot():
    if not TOKEN:
        raise RuntimeError("TELEGRAM_TOKEN não definido")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ligar", ligar))
    app.add_handler(CommandHandler("desligar", desligar))
    app.add_handler(CommandHandler("status", status))

    # loop a cada 5 segundos
    app.job_queue.run_repeating(loop_24h, interval=5, first=5)

    print("🚀 Bot Telegram em polling 24h")

    # ⚠️ SEM await / SEM asyncio
    app.run_polling(drop_pending_updates=True)
