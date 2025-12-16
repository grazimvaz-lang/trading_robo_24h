import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Robô 24h online e funcionando!")


async def iniciar_bot():
    print("🔍 Verificando TELEGRAM_TOKEN...")

    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        print("❌ TELEGRAM_TOKEN NÃO encontrado")
        return

    print("📲 TELEGRAM_TOKEN encontrado")
    print("🚀 Iniciando Bot do Telegram...")

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))

    print("✅ Bot do Telegram iniciado e aguardando comandos")
    app.run_polling()   # ⬅️ SEM await
