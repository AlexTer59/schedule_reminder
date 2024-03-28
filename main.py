from aiogram import Bot, Dispatcher, types, F
from aiogram.methods import DeleteWebhook
from aiogram.types import ReplyKeyboardRemove
from aiogram.filters.command import Command
from keyboards import main_menu_keyboard, links_inline_keyboard, vote_inline_keyboard, counter_inline_keyboard
import asyncio
import random
import os
from dotenv import load_dotenv

# load .env variables
load_dotenv()

HELP = '''
<b>/start</b> - <em>начать работу с ботом;</em>
<b>/help</b> - <em>список команд;</em>
<b>/description</b> - <em>описание бота;</em>
<b>/links</b> - <em>команда для вызова inline клавиатуры;</em>
<b>/count</b> - <em>команда - счетчик нажатий;</em>
<b>Рандомная фотография</b> - <em>команда для получения рандомной фотографии.</em>
'''

IMAGE_LINKS = [
    'https://myskillsconnect.com/uploads/posts/2023-06/1687341061_myskillsconnect-com-p-foto-bmv-m5-f90-kompetishn-na-oboi-13.jpg',
    'https://www.carpixel.net/w/edcd160538afd7041e352e24c748f589/mercedes-amg-e-63-s-car-wallpaper-65537.jpg',
    'https://kuznitsaspb.ru/wp-content/uploads/a/0/c/a0c8380c046f0f7b8ab4120e675e2956.jpeg',
    'https://sportishka.com/uploads/posts/2022-08/1660842408_4-sportishka-com-p-lada-priora-sedan-novaya-krasivo-foto-7.jpg',
    'http://audi.carwallpapers.ru/audi/rs7-sportback/2019/Audi-RS7-Sportback-2019-2560x1440-037.jpg'
]

IMAGE_DISCRIPTIONS = [
    'BMW M5 F90',
    'Mercedes-AMG E63S',
    'Alfa Romeo Giulia',
    'Lada Priora',
    'Audi RS7'
]

IMAGE_DICT = dict(zip(IMAGE_LINKS, IMAGE_DISCRIPTIONS))

HELLO_STICKERS = [
    'CAACAgIAAxkBAAELyDtmAAEw3aTt3gABkQHeaaKrAYV7nlj1AAIWAAOhtzMI5tw7vxW0t8U0BA',
    'CAACAgIAAxkBAAELyD1mAAExBgIlgqPsdOg_QhkCFYiwDe8AAiMAA8A2TxN7744rUwpfxjQE',
    'CAACAgIAAxkBAAELyD9mAAExeb3QaGDPf6m8y5Drk4P9j7MAAgUAA8A2TxP5al-agmtNdTQE',
    'CAACAgIAAxkBAAELyEFmAAExl_elj5PRTqlqFW1-VMZ_vzsAAgEBAAJWnb0KIr6fDrjC5jQ0BA',
    'CAACAgIAAxkBAAELyENmAAExuOfqECxY95ngbs67xRu1Y2cAAh4JAAIYQu4I-VjZ7h0hnCE0BA'
]

# Bot object
bot = Bot(token=os.getenv('TOKEN'))
# Dispatcher
dp = Dispatcher()

random_image = random.choice(list(IMAGE_DICT.keys()))

is_like = False
is_dislike = False

counter = 0

async def on_startup():
    print('Бот запущен!')


async def random_img(message: types.Message):
    global random_image
    random_image = random.choice(list(filter(lambda x: x != random_image, list(IMAGE_DICT.keys()))))
    await bot.send_photo(chat_id=message.chat.id,
                         photo=random_image,
                         caption=IMAGE_DICT.get(random_image),
                         reply_markup=vote_inline_keyboard())


# Handler /start command
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.delete()
    await bot.send_message(chat_id=message.chat.id,
                           text="<b>Добро пожаловать в наш бот!</b> 🖖",
                           parse_mode="HTML",
                           reply_markup=main_menu_keyboard())
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker=random.choice(HELLO_STICKERS))


# Handler /description command
@dp.message(Command('description'))
async def cmd_description(message: types.Message):
    await message.delete()
    await bot.send_message(chat_id=message.chat.id, text='Этот бот может отправлять рандомные картинки')


# Handler /help command
@dp.message(Command('help'))
async def cmd_help(message: types.Message):
    await message.delete()
    await bot.send_message(chat_id=message.chat.id,
                           text=HELP,
                           parse_mode='HTML')


# Handler /links command
@dp.message(Command('links'))
async def get_links(message: types.Message):
    await message.delete()
    await bot.send_message(chat_id=message.chat.id,
                           text='Вот ссылки на соц.сети моего разработчика',
                           reply_markup=links_inline_keyboard())


# Handler Рандомная фотография command
@dp.message(F.text == 'Рандомная фотография')
async def get_random_image(message: types.Message):
    await message.delete()
    await bot.send_message(chat_id=message.chat.id,
                           text='Рандомная фотография',
                           reply_markup=ReplyKeyboardRemove())
    await random_img(message)


@dp.message(Command('count'))
async def cmd_count(message: types.Message) -> None:
    await bot.send_message(chat_id=message.chat.id,
                           text=f'Количество нажатий равно: {counter}',
                           reply_markup=counter_inline_keyboard())


@dp.callback_query(lambda callback_query: callback_query.data.startswith('btn'))
async def count(callback: types.CallbackQuery) -> None:
    global counter
    if callback.data == 'btn_increase':
        counter += 1
        await callback.message.edit_text(text=f'Количество нажатий равно: {counter}',
                                         reply_markup=counter_inline_keyboard())
    elif callback.data == 'btn_decrease':
        counter -= 1
        await callback.message.edit_text(text=f'Количество нажатий равно: {counter}',
                                         reply_markup=counter_inline_keyboard())


@dp.callback_query()
async def vote_callback(callback: types.CallbackQuery):
    global random_image, is_like, is_dislike
    if callback.data == 'like':
        if not is_like or is_dislike:
            await callback.answer(text='Вам понравилась фотография!')
            is_like = True
            is_dislike = False
        else:
            await callback.answer(text='Вы уже лайкали!')
    elif callback.data == 'dislike':
        if is_like or not is_dislike:
            await callback.answer(text='Вам не понравилась фотография!')
            is_like = False
            is_dislike = True
        else:
            await callback.answer(text='Вы уже дизлайкали!')
    elif callback.data == 'next':
        random_image = random.choice(list(filter(lambda x: x != random_image, list(IMAGE_DICT.keys()))))
        await callback.message.edit_media(types.InputMediaPhoto(media=random_image,
                                                                caption=IMAGE_DICT.get(random_image)),
                                          reply_markup=vote_inline_keyboard())
        await callback.answer()
    else:
        await callback.message.answer(text='Вы в главном меню. Выберите команду:',
                                      reply_markup=main_menu_keyboard())
        await callback.answer()


# Handler /get_location command
@dp.message(Command('get_location'))
async def get_loc_cmd(message: types.Message):
    await message.delete()
    await bot.send_location(chat_id=message.chat.id,
                            latitude=random.randint(-50, 50),
                            longitude=random.randint(-100, 100))


async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))  # There is not skip_updates() in the aiogram 3.X
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
