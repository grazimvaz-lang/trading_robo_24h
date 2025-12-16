from telegram_bot import iniciar_bot
from trader import iniciar_trader

if __name__ == "__main__":
    print("🚀 Robô 24h iniciado (Telegram + Trader)")
    iniciar_trader()
    iniciar_bot()
