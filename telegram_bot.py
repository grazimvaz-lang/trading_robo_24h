import os
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

# ===============================
# CONFIGURAÇÃO DE LOG
# ===============================
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# ===============================
# TOKEN DO TELEGRAM
# ===============================
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TELEGRAM_TOKEN:
    raise RuntimeError("❌ TELEGRAM_TOKEN não encontrado nas variáveis de ambiente")

# ===============================
# COMANDOS DO BOT
# ===============================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Robô de negociação ONLINE!\n\n"
        "⏱️ Rodando 24h no Railway\n"
        "📡 Aguardando sinais..."
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Status OK\n"
        "🤖 Robô ativo\n"
        "⏳ Aguardando sinais"
    )

# ===============================
# INICIALIZAÇÃO DO BOT
# ===============================
async def iniciar_bot():
    logger.info("📲 Iniciando Bot do Telegram...")

    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("status", status))

    logger.info("🤖 Bot do Telegram iniciado com sucesso")

    await application.run_polling()
