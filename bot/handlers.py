import asyncio

from aiogram.types import Message
from dialog.dialog_router import DialogList
from main_class import Main, router
from bot.dispatcher import bot, dp


main = Main(dp, bot)
dialog = DialogList(main)


@router.message()
async def get_messages(message: Message):
    await asyncio.sleep(0.1)
    dialog.message_arrived(message)
