import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# =========================
# COMANDO /start
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Robô 24h ONLINE!\n\n"
        "Comandos disponíveis:\n"
        "/start - status do robô\n"
        "/ping - testar conexão"
    )

# =========================
# COMANDO /ping
# =========================
async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏓 Pong! Robô está ativo.")

# =========================
# RESPOSTA PARA TEXTO LIVRE
# =========================
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📩 Mensagem recebida.\n"
        "Use /start ou /ping."
    )

# =========================
# INICIAR BOT
# =========================
async def iniciar_bot():
    print("🔍 Verificando TELEGRAM_TOKEN...")
    token = os.getenv("TELEGRAM_TOKEN")

    if not token:
        print("❌ TELEGRAM_TOKEN não encontrado")
        return

    print("✅ TELEGRAM_TOKEN encontrado")
    print("🚀 Iniciando Bot do Telegram...")

    app = ApplicationBuilder().token(token).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("✅ Bot do Telegram iniciado e aguardando mensagens")
    await app.run_polling()
