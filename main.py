import threading
import time

from trader import iniciar_trader
from telegram_bot import iniciar_bot

print("🔥 MAIN.PY CARREGADO COM SUCESSO")
print("🚀 Robô 24h iniciado")

# Trader
threading.Thread(target=iniciar_trader, daemon=True).start()

# Telegram
threading.Thread(target=iniciar_bot, daemon=True).start()

print("🧠 Threads do Trader e Telegram disparadas")

# Mantém o processo vivo
while True:
    time.sleep(60)
