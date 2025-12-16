import asyncio
import threading
from telegram_bot import iniciar_bot
from trader import iniciar_trader

print("🔥 MAIN.PY CARREGADO COM SUCESSO")

# Trader em thread
threading.Thread(
    target=iniciar_trader,
    daemon=True
).start()

print("📈 Trader iniciado (modo contínuo)")

# Telegram é o processo principal
asyncio.run(iniciar_bot())
