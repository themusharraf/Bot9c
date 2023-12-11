import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import types

import random

TOKEN = "6768144687:AAFHY5y4o4Uyjr7aeNKZD78kA9jNpNuYKyY"

logging.basicConfig(level=logging.INFO)

dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(f"Assalomu alekum {message.from_user.first_name}")
    await message.answer(f"id: {message.from_user.id}")
    await message.answer(f"username: {message.from_user.username}")


@dp.message(Command("image"))
async def image(message: Message):
    s1 = "https://images.app.goo.gl/Eyqxzb9udsHZuakm8"
    s2 = "https://images.app.goo.gl/9i3Q1V2BXPgitTDSA"
    s3 = "https://images.app.goo.gl/U8MP5N8YxbBSNxWJ8"
    s4 = "https://images.app.goo.gl/8kGEBJ2mYwQN92mq9"
    s5 = "https://images.app.goo.gl/r32B8RpGjgJQw9Vw9"
    s6 = "https://images.app.goo.gl/8U1h3pZQAAsMt4Xz6"

    img_list = [s1, s2, s3, s4, s5, s6]

    s = random.choice(img_list)

    await message.answer_photo(photo=f"{s}",
                               caption=f"{message.from_user.first_name}")


@dp.message(Command("button"))
async def button(message: Message):
    kb = [
        [types.KeyboardButton(text="Qish")],
        [types.KeyboardButton(text="Yoz")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("button choice", reply_markup=keyboard)

    @dp.message(F.text == "Qish")
    async def qish(message: Message):
        await message.answer_photo(photo="https://images.app.goo.gl/45uebf8ccm8fJnRv9", caption="Qish rasmi")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
