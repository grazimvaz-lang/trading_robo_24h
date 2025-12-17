import os
import asyncio
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

# ===============================
# ESTADO GLOBAL DO ROBÔ
# ===============================
BOT_LIGADO = False

# Token vem das variáveis de ambiente (Railway / Windows)
TOKEN = os.getenv("TELEGRAM_TOKEN")


# ===============================
# COMANDOS DO TELEGRAM
# ===============================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Robô online!\n\n"
        "Comandos disponíveis:\n"
        "/ligar - liga o robô\n"
        "/desligar - desliga o robô\n"
        "/status - ver status"
    )


async def ligar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global BOT_LIGADO
    BOT_LIGADO = True
    await update.message.reply_text("✅ Robô LIGADO.")


async def desligar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global BOT_LIGADO
    BOT_LIGADO = False
    await update.message.reply_text("⛔ Robô DESLIGADO.")


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"📌 Status atual: {'LIGADO' if BOT_LIGADO else 'DESLIGADO'}"
    )


# ===============================
# LOOP 24H DO ROBÔ
# ===============================
async def loop_24h():
    while True:
        try:
            if BOT_LIGADO:
                # 🔁 AQUI ENTRA SUA LÓGICA DE TRADING
                # (análise, sinais, ordens, etc.)
                print("🔁 Robô rodando 24h...")
            await asyncio.sleep(5)
        except Exception as e:
            print(f"❌ Erro no loop do robô: {e}")
            await asyncio.sleep(5)


# ===============================
# INICIALIZAÇÃO DO BOT
# ===============================
async def iniciar_bot():
    if not TOKEN:
        raise RuntimeError("TELEGRAM_TOKEN não definido")

    app = ApplicationBuilder().token(TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ligar", ligar))
    app.add_handler(CommandHandler("desligar", desligar))
    app.add_handler(CommandHandler("status", status))

    # Loop do robô em background
    asyncio.create_task(loop_24h())

    print("🚀 Bot Telegram em polling 24h")

    # ✅ ÚNICO polling (SEM DUPLICAÇÃO)
    await app.run_polling(drop_pending_updates=True)
