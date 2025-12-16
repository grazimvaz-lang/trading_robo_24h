import threading
from trader import iniciar_trader
from telegram_bot import iniciar_bot

def main():
    print("🚀 Robô 24h iniciado")

    trader_thread = threading.Thread(target=iniciar_trader, daemon=True)
    trader_thread.start()

    iniciar_bot()

if __name__ == "__main__":
    main()
