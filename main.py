'''
Task 5
1) Create the bot containing the inline keyboard which will opens by /links command; +
2) Modify the bot so that every button of the inline keyboard contains a custom link; +
3) Create the usual keyboard which will calls the /link command; +
4) Crate the on_startup method which will print 'Я был запущен!' after run server and set the value of
skip_updates = True; +
5) Try to move the inline keyboard in a separate module. +
'''


from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ContentType
from aiogram.methods import DeleteWebhook
from aiogram.filters.command import Command
from keyboards import keyboard, inline_keyboard
import asyncio
import random
import os
from dotenv import load_dotenv

# load .env variables
load_dotenv()

HELP = '''
<b>/help</b> - <em>список команд;</em>
<b>/start</b> - <em>начать работу с ботом;</em>
<b>/description</b> - <em>описание бота;</em>
<b>/count</b> - <em>просто счетчик;</em>
<b>/get_sticker</b> - <em>команда для получения стикера;</em>
<b>/get_orange</b> - <em>команда для получения картинки апельсина;</em>
<b>/get_location</b> - <em>команда для местоположения;</em>
<b>/links</b> - <em>команда для вызова inline клавиатуры.</em>
'''

count = 0

# Bot object
bot = Bot(token=os.getenv('TOKEN'))
# Dispatcher
dp = Dispatcher()


async def on_startup():
    print('Я был запущен!')


# Handler /start command
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text="<b>Hi, I'm a Telegram bot, powered by <em>aiogram!</em> Let's start!</b>",
                           parse_mode="HTML",
                           reply_markup=keyboard)

    await message.delete()


# Handler /discription command
@dp.message(Command('description'))
async def cmd_description(message: types.Message):
    await message.answer(text='In future this bot can reminds you about your schedule')


# Handler /help command
@dp.message(Command('help'))
async def cmd_help(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP,
                           parse_mode='HTML')
    await message.delete()


# Handler /get_picture command
@dp.message(Command('get_orange'))
async def get_pic_cmd(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://proprikol.ru/wp-content/uploads/2019/10/kartinki-apelsina-8.jpg')
    await message.delete()


# Handler /get_location command
@dp.message(Command('get_location'))
async def get_loc_cmd(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            latitude=random.randint(-90, 90) + round(random.random(), 4),
                            longitude=random.randint(-180, 180) + round(random.random(), 4))
    await message.delete()


# Handler /count command
@dp.message(Command('count'))
async def cmd_cont(message: types.Message):
    global count
    count += 1
    await message.reply(text=f'Count: {count}')


# Handler /give command
@dp.message(Command('get_sticker'))
async def get_sticker_cmd(message: types.Message):
    await message.answer(text='Смотри какой смешной кот ❤️!')
    await bot.send_sticker(message.chat.id,
                           sticker='CAACAgIAAxkBAAELxX9l_WEo_sSMW3JO_RwhZTP9_EGD5gACwQ4AApq2SUhGy_Y9suGsBTQE')


# Handler sticker message
@dp.message(F.content_type == ContentType.STICKER)
async def get_sticker_id(message: types.Message):
    await message.reply(message.sticker.file_id)


@dp.message(F.text == '❤️')
async def get_cat_sticker(message: types.Message):
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker='CAACAgIAAxkBAAELxnxl_oNPVyP2v04UJkGBXR9rfhcqVwAC3gkAAqe9wEvo_3MQ5y3rrDQE')


# Handler /links command
@dp.message(Command('links'))
async def get_links(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Вот ссылки на соц.сети моего разработчика',
                           reply_markup=inline_keyboard)


# Handler any message
@dp.message()
async def any_msg(message: types.Message):
    if '❤️' in message.text:
        msg_text = message.text.replace('❤️', '🖤')
        await message.answer(msg_text)
    else:
        await message.answer(message.text)
    await message.answer(f'Всего в тексте галочек: {message.text.count("✅")}.')


async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))  # There is not skip_updates() in the aiogram 3.X
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
