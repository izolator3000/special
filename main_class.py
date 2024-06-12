import asyncio
from aiogram import Router
router = Router()


class Main:
    def __init__(self, dp, bot):
        self.dp = dp
        self.bot = bot
        self.messages = []

    def send_message(self, messages: list):
        self.messages = messages

    async def dp_polling(self):
        self.dp.include_router(router)
        await self.dp.start_polling(self.bot)

    async def my_send_messages(self):
        while True:
            for message in self.messages:
                await self.bot.send_message(**message)
            self.messages = []
            await asyncio.sleep(0.1)

    async def main(self):
        while True:
            task1 = asyncio.create_task(self.my_send_messages())
            task2 = asyncio.create_task(self.dp_polling())
            await task1
            await task2

