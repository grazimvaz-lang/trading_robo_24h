import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

# =========================
# Comando /start
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Robô de negociação 24h ONLINE e funcionando!"
    )

# =========================
# Inicialização do Bot
# =========================
def iniciar_bot():
    print("🔥 ENTREI NA FUNÇÃO iniciar_bot()")
    print("🔍 Verificando TELEGRAM_TOKEN...")

    token = os.getenv("TELEGRAM_TOKEN")

    if not token:
        print("❌ TELEGRAM_TOKEN NÃO encontrado nas variáveis de ambiente")
        return

    print("📲 TELEGRAM_TOKEN encontrado")
    print("🚀 Iniciando Bot do Telegram...")

    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler("start", start))

    print("✅ Bot do Telegram iniciado e aguardando comandos")
    application.run_polling()
