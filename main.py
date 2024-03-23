from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ContentType, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.command import Command
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
'''

count = 0

# Bot object
bot = Bot(token=os.getenv('TOKEN'))
# Dispatcher
dp = Dispatcher()
kb = [
    [KeyboardButton(text='/help'), KeyboardButton(text='/description')],
    [KeyboardButton(text='/count'), KeyboardButton(text='/get_sticker')],
    [KeyboardButton(text='/get_orange'), KeyboardButton(text='/get_location')],
    [KeyboardButton(text='❤️')]
]
ikb = [
    [InlineKeyboardButton(text='GitHub', url='https://github.com/AlexTer59/schedule_reminder'),
     InlineKeyboardButton(text='VK', url='https://vk.com/id137053909')]
]

async def on_startup():
    print('Я запустился!')


# Handler /start command
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(keyboard=kb,
                                   resize_keyboard=True,
                                   input_field_placeholder='Выберите команду:')
    await bot.send_message(chat_id=message.chat.id, text="<b>Hi, I'm a Telegram bot, powered by <em>aiogram!</em> Let's start!</b>",
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
    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP,
                           parse_mode='HTML',
                           reply_markup=inline_keyboard)
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
                            latitude=random.randint(-90,90) + round(random.random(), 4),
                            longitude=random.randint(-180,180) + round(random.random(), 4))
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
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
