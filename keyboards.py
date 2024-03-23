from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


commands_markup = [
    [KeyboardButton(text='/help'), KeyboardButton(text='/description')],
    [KeyboardButton(text='/count'), KeyboardButton(text='/get_sticker')],
    [KeyboardButton(text='/get_orange'), KeyboardButton(text='/get_location')],
    [KeyboardButton(text='❤️'), KeyboardButton(text='/links')]
]

commands_keyboard = ReplyKeyboardMarkup(keyboard=commands_markup,
                               resize_keyboard=True,
                               input_field_placeholder='Выберите команду:')

links_markup = [
    [
        InlineKeyboardButton(text='GitHub', url='https://github.com/AlexTer59/schedule_reminder'),
        InlineKeyboardButton(text='VK', url='https://vk.com/id137053909')
    ]
]

links_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=links_markup)

vote_markup = [
    [
        InlineKeyboardButton(text='❤️', callback_data='like'),
        InlineKeyboardButton(text='👎', callback_data='dislike')
    ]
]

vote_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=vote_markup)
