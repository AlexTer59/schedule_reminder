'''
TASK 2 The bot must answer to user with a random letter from the alphabet;
You need to add /description command handler which returns the description of the bot;
You need to add /count command handler which returns number of own calls;
The bot nust answer 'YES' if user message includes the 0 number or 'NO' if it's not
'''

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio
import random
import string
import os
from dotenv import load_dotenv

# load .env variables
load_dotenv()

HELP = '''
/help - список команд;
/start - начать работу с ботом;
/description - описание бота;
/count - просто счетчик.
'''

count = 0

# Bot object
bot = Bot(token=os.getenv('TOKEN'))
# Dispatcher
dp = Dispatcher()


# Handler /start command
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer(text="Hi, I'm a Telegram bot, powered by aiogram! Let's start!")
    await message.delete()


# Handler /discription command
@dp.message(Command('description'))
async def cmd_description(message: types.Message):
    await message.answer(text='In future this bot can reminds you about your schedule')


# Handler /help command
@dp.message(Command('help'))
async def cmd_help(message: types.Message):
    await message.reply(text=HELP)


# Handler /count command
@dp.message(Command('count'))
async def cmd_cont(message: types.Message):
    global count
    count += 1
    await message.reply(text=f'Count: {count}')


# Handler any message
@dp.message()
async def is_null_here(message: types.Message):
    await message.reply('YES') if '0' in message.text else await message.reply('No')
    await message.answer(text=random.choice(string.ascii_uppercase))


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
