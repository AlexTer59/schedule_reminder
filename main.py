from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio
import os
from dotenv import load_dotenv
# load .env variables
load_dotenv()

# Telegram API token
TOKEN_API = os.getenv('TOKEN')

# Bot object
bot = Bot(token=TOKEN_API)
# Dispatcher
dp = Dispatcher()


# Handler any message
@dp.message()
async def cmd_start(message: types.Message):
    await message.answer(text=message.text)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
