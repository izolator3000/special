import logging
from aiogram import Bot, Dispatcher
from bot.config import API_TOKEN
# API_TOKEN = '7158667149:AAHqtZLmR5NCahie8tAEpJj3BkuG6Am6Nso'
# Configure logging
logging.basicConfig(level=logging.INFO)

# prerequisites
if not API_TOKEN:
    exit("No token provided")

# init
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
