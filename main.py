from trader import iniciar_trader
from telegram_bot import iniciar_bot
import threading

print("🚀 Robô 24h iniciado")

# Inicia o trader em thread separada
thread_trader = threading.Thread(target=iniciar_trader, daemon=True)
thread_trader.start()

# Inicia o bot do Telegram (processo principal)
iniciar_bot()
