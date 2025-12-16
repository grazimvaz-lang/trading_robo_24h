import asyncio
from telegram_bot import iniciar_bot
from trader import iniciar_trader

if __name__ == "__main__":
    print("🔥 MAIN.PY CARREGADO COM SUCESSO")
    print("🚀 Robô 24h iniciado")

    iniciar_trader()

    asyncio.run(iniciar_bot())
