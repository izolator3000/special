import asyncio


from bot.handlers import main
"""
Не знаю, как сделать:
TODO: перенести создание объекта main сюда, при этом оставить возможность бот.хендлеру отлавливать сообщения

Можно, наверное и хендлер перенести куда-нибудь, но кажется логичным, чтобы для отлавливания было отдельное место
"""

if __name__ == '__main__':
    asyncio.run(main.run())
