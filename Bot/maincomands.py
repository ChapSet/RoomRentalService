from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
import asyncio

from Bot.const import greeting_
from inline_keyboard import *
from TOKEN import TOKEN


async def greeting(message: Message, bot: Bot):
    name = message.from_user.first_name
    await message.answer(f'Привет, {name}! {greeting_}',
                         reply_markup=select_action)
    await message.delete()
    print(f'Пользователь {name} начал работу с ботом')


async def book_product(query: CallbackQuery, bot: Bot):
    await query.answer(query.from_user.first_name)


async def start():
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.message.register(greeting, Command(commands=['start']))
    dp.callback_query.register(book_product, F.data.startswitch("booking"))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
