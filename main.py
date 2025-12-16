import asyncio
from telegram_bot import iniciar_bot
from trader import iniciar_trader

print("🔥 MAIN.PY CARREGADO COM SUCESSO")
print("🚀 Robô 24h iniciado")

# Trader em loop (thread ou síncrono, como já está)
iniciar_trader()

# Telegram (async)
asyncio.run(iniciar_bot())
