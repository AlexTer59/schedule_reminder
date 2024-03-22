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
/count - просто счетчик;
/give - команда для получения стикера.
'''

count = 0

# Bot object
bot = Bot(token=os.getenv('TOKEN'))
# Dispatcher
dp = Dispatcher()


async def on_startup():
    print('Бот успешно запущен!')


# Handler /start command
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer(text="<b>Hi, I'm a Telegram bot, powered by <em>aiogram!</em> Let's start!</b>",
                         parse_mode="HTML")
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


# Handler /give command
@dp.message(Command('give'))
async def cmd_give(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker=f'''
                        {random.choice(["CAACAgIAAxkBAAELxXVl_VjV8lHilA5_OAUn3pR4KjM6yQAC0AwAAsO7wUtQyA2abxmZdjQE",
                        "CAACAgIAAxkBAAELxXdl_VlMB0hA1wSbtkAHOPGyPlHfCAACNAADwDZPE_GCwMy0CI7UNAQ"])}''')


# Handler any message
@dp.message()
async def any_msg(message: types.Message):
    await message.reply('YES') if '0' in message.text else await message.reply('No')
    await message.answer(text=(random.choice(string.ascii_uppercase) + "❤️"))


async def main():
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
