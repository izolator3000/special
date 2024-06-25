import asyncio
from bot.dispatcher import bot, dp
from dialogs.dialog_router import DialogList
from dialogs.service.adapter import message2user


class Main:
    def __init__(self):
        self.dp = dp
        self.bot = bot
        self.dialogs = DialogList(self)
        self.messages4send = []

    def message_arrived(self, message, social_network):
        self.dialogs.message_arrived(message2user(message, social_network))

    def send_message(self, messages: list):
        self.messages4send = messages

    async def dp_polling(self):
        await self.dp.start_polling(self.bot)

    async def my_send_messages(self):
        while True:
            for message in self.messages4send:
                await self.bot.send_message(**message)
            self.messages4send = []
            await asyncio.sleep(0.1)

    async def run(self):
        while True:
            task1 = asyncio.create_task(self.my_send_messages())
            task2 = asyncio.create_task(self.dp_polling())
            await task1
            await task2

