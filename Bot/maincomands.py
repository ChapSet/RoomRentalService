from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

from Bot.const import greeting_
from inline_keyboard import *

TOKEN = '5979303415:AAFX4X5qXuUqrJKX4w8kJ5PYtLEtz4zsFME'


async def greeting(message: Message, bot: Bot):
    name = message.from_user.first_name
    await message.answer(f'Привет, {message.from_user.first_name}! {greeting_}',
                         reply_markup=select_action)
    await message.delete()
    print(f'Пользователь {message.from_user.first_name} начал работу с ботом')


async def start():

    bot = Bot(TOKEN)

    dp = Dispatcher()
    dp.message.register(greeting, Command(commands=['start']))

    try:
        await dp.start_polling(bot)

    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
