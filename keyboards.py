from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


kb = [
    [KeyboardButton(text='/help'), KeyboardButton(text='/description')],
    [KeyboardButton(text='/count'), KeyboardButton(text='/get_sticker')],
    [KeyboardButton(text='/get_orange'), KeyboardButton(text='/get_location')],
    [KeyboardButton(text='❤️'), KeyboardButton(text='/links')]
]
ikb = [
    [InlineKeyboardButton(text='GitHub', url='https://github.com/AlexTer59/schedule_reminder'),
     InlineKeyboardButton(text='VK', url='https://vk.com/id137053909')]
]

keyboard = ReplyKeyboardMarkup(keyboard=kb,
                               resize_keyboard=True,
                               input_field_placeholder='Выберите команду:')

inline_keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)
