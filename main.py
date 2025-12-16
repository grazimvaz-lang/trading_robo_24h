import asyncio
import threading

from telegram_bot import iniciar_bot
from trader import iniciar_trader


def start_trader():
    print("⚙️ Iniciando Trader (loop contínuo)...")
    iniciar_trader()


async def start_telegram():
    print("📲 Iniciando Bot do Telegram...")
    await iniciar_bot()


if __name__ == "__main__":
    print("🚀 Robô 24h iniciado (Telegram + Trader)")

    # Inicia o trader em uma thread separada
    trader_thread = threading.Thread(target=start_trader, daemon=True)
    trader_thread.start()

    # Inicia o bot do Telegram no loop assíncrono
    asyncio.run(start_telegram())
