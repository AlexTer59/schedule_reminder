from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio
import os
from dotenv import load_dotenv
# load .env variables
load_dotenv()

HELP = '''
/help - список команд;
/start - начать работу с ботом;
'''

# Bot object
bot = Bot(token=os.getenv('TOKEN'))
# Dispatcher
dp = Dispatcher()


# Handler /start command
@dp.message(Command('start'))
async def help_command(message: types.Message):
    await message.answer(text="Hi, I'm a Telegram bot, powered by aiogram! Let's start!")
    await message.delete()


# Handler /help command
@dp.message(Command('help'))
async def help_command(message: types.Message):
    await message.reply(text=HELP)


# Handler any message
@dp.message()
async def cmd_start(message: types.Message):
    if message.text.count(' ') > 2:
        await message.answer(text=message.text.upper())
    else:
        await message.reply(f'Too short message, {message.from_user.first_name}')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
