import asyncio
from aiogram.types import Message
from main_class import Main

main = Main()

@main.dp.message()
async def get_messages(message: Message):
    await asyncio.sleep(0.1)
    main.message_arrived(message, "telegram")
