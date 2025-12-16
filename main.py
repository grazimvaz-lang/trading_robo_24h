import asyncio
from telegram_bot import iniciar_bot
from trader import iniciar_trader


async def main():
    print("🔥 MAIN.PY CARREGADO COM SUCESSO")
    print("🚀 Robô 24h iniciado")

    # Trader em background (não trava o Telegram)
    asyncio.create_task(asyncio.to_thread(iniciar_trader))

    # Telegram é o processo principal (obrigatório)
    await iniciar_bot()


if __name__ == "__main__":
    asyncio.run(main())
