from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

select_action = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Забронировать товар',
            callback_data='бронь'
        ),
        InlineKeyboardButton(
            text='Выбрать набор',
            callback_data='набор'
        )
    ]
])