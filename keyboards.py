from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


main_menu_markup = [
    [KeyboardButton(text='/help'), KeyboardButton(text='/description')],
    [KeyboardButton(text='/get_location'), KeyboardButton(text='/links')],
    [KeyboardButton(text='Рандомная фотография')]
]

main_menu_keyboard = ReplyKeyboardMarkup(keyboard=main_menu_markup,
                               resize_keyboard=True,
                               input_field_placeholder='Выберите команду: ')

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
    ],
    [
        InlineKeyboardButton(text='Следующая фотография', callback_data='next')
    ],
    [
        InlineKeyboardButton(text='Главное меню', callback_data='main')
    ]

]

vote_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=vote_markup)
