from telegram.ext import Updater, CommandHandler
from config import TELEGRAM_TOKEN
from state import set_robot_on, set_robot_off, is_robot_on

def start(update, context):
    update.message.reply_text(
        "🤖 Robô online.\n\n"
        "Comandos disponíveis:\n"
        "/on - ligar robô\n"
        "/off - desligar robô\n"
        "/status - ver status"
    )

def ligar(update, context):
    set_robot_on()
    update.message.reply_text("✅ Robô LIGADO (24h).")

def desligar(update, context):
    set_robot_off()
    update.message.reply_text("⏸️ Robô DESLIGADO.")

def status(update, context):
    estado = "LIGADO" if is_robot_on() else "DESLIGADO"
    update.message.reply_text(f"📊 Status atual: {estado}")

def iniciar_bot():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("on", ligar))
    dp.add_handler(CommandHandler("off", desligar))
    dp.add_handler(CommandHandler("status", status))

    updater.start_polling()
    updater.idle()
