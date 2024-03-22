'''
TASK 3:
1) Make a bot which will send a cat sticker as an answer on the /give command. But before send the sticker bot sends the
message: "Смотри какой смешной кот ❤️!"; +
2) Modify the bot by adding possible to send the common heart but get the black heart as answer; +
3) Modify the bot which will count ✅ in the user message and will return this quantity; +
4) Modify the /help command which will return the list of available commands but the command name must be a bold text
and description must be an italic; +
5) Make an on_sturtup() func which will print on the terminal "Я запустился!"; +
6) Make a func which will return the ID of sent sticker as reply of user message. +
'''


from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ContentType
from aiogram.filters.command import Command
import asyncio
import os
from dotenv import load_dotenv

# load .env variables
load_dotenv()

HELP = '''
<b>/help</b> - <em>список команд;</em>
<b>/start</b> - <em>начать работу с ботом;</em>
<b>/description</b> - <em>описание бота;</em>
<b>/count</b> - <em>просто счетчик;</em>
<b>/give</b> - <em>команда для получения стикера.</em>
'''

count = 0

# Bot object
bot = Bot(token=os.getenv('TOKEN'))
# Dispatcher
dp = Dispatcher()


async def on_startup():
    print('Я запустился!')


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
    await message.reply(text=HELP, parse_mode='HTML')


# Handler /count command
@dp.message(Command('count'))
async def cmd_cont(message: types.Message):
    global count
    count += 1
    await message.reply(text=f'Count: {count}')


# Handler /give command
@dp.message(Command('give'))
async def cmd_give(message: types.Message):
    await message.answer(text='Смотри какой смешной кот ❤️!')
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAELxX9l_WEo_sSMW3JO_RwhZTP9_EGD5gACwQ4AApq2SUhGy_Y9suGsBTQE')


# Handler sticker message
@dp.message(F.content_type == ContentType.STICKER)
async def get_sticker_id(message: types.Message):
    await message.reply(message.sticker.file_id)

# Handler any message
@dp.message()
async def any_msg(message: types.Message):
    if '♥' in message.text:
        msg_text = message.text.replace('♥', '🖤')
        await message.answer(msg_text)
    else:
        await message.answer(message.text)
    await message.answer(f'Всего в тексте галочек: {message.text.count("✅")}.')



async def main():
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
