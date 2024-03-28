from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def main_menu_keyboard() -> ReplyKeyboardMarkup:
    main_menu_markup = [
        [KeyboardButton(text='/help'), KeyboardButton(text='/description')],
        [KeyboardButton(text='/get_location'), KeyboardButton(text='/links')],
        [KeyboardButton(text='Рандомная фотография'), KeyboardButton(text='/count')]
    ]

    return ReplyKeyboardMarkup(keyboard=main_menu_markup,
                               resize_keyboard=True,
                               input_field_placeholder='Выберите команду: ')


def links_inline_keyboard() -> InlineKeyboardMarkup:
    links_markup = [
        [
            InlineKeyboardButton(text='GitHub', url='https://github.com/AlexTer59/schedule_reminder'),
            InlineKeyboardButton(text='VK', url='https://vk.com/id137053909')
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=links_markup)


def vote_inline_keyboard() -> InlineKeyboardMarkup:
    vote_markup = [
        [
            InlineKeyboardButton(text='❤️', callback_data='like'),
            InlineKeyboardButton(text='👎', callback_data='dislike')
        ],
        [
            InlineKeyboardButton(text='Следующая фотография', callback_data='next')
        ],
        [
            InlineKeyboardButton(text='Главное меню', callback_data='main')
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=vote_markup)


def counter_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Increase', callback_data='btn_increase'),
            InlineKeyboardButton(text='Decrease', callback_data='btn_decrease')
        ]
    ])
