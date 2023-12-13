import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import types

import random

from aiogram.utils.keyboard import InlineKeyboardBuilder

TOKEN = ""

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
        [
            types.KeyboardButton(text="Qish"),
            types.KeyboardButton(text="Yoz"),
            types.KeyboardButton(text="Bahor"),
            types.KeyboardButton(text="Kuz")

        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("button choice", reply_markup=keyboard)

    @dp.message(F.text == "Qish")
    async def qish(message: Message):
        await message.answer_photo(photo="https://images.app.goo.gl/45uebf8ccm8fJnRv9",
                                   caption="Qish rasmi")

    @dp.message(F.text == "Yoz")
    async def qish(message: Message):
        await message.answer_photo(photo="https://images.app.goo.gl/bQvK746RyhFMchNa6",
                                   caption="Yoz rasmi")

    @dp.message(F.text == "Bahor")
    async def qish(message: Message):
        await message.answer_photo(photo="https://images.app.goo.gl/seeT6fkpDKYBVTXS7",
                                   caption="Bahor rasmi")

    @dp.message(F.text == "Kuz")
    async def qish(message: Message):
        await message.answer_photo(photo="https://images.app.goo.gl/yPCdZqbjDYS2xuSo7", caption="Kuz rasmi")


@dp.message(Command("music"))
async def audio(message: Message):
    await message.answer_audio(audio="https://dl.uzxit.net/2023-mp3/sakit-samedov-love-disco_(uzxit.net).mp3",
                               caption="🎸 @bot9c_bot bu bot sizga music lar yuklab beradi")


@dp.message(F.text == "info")
async def info(message: Message):
    kb = [
        [
            types.KeyboardButton(text="Contact", request_contact=True),
            types.KeyboardButton(text="Location", request_location=True),

        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("send location or contact", reply_markup=keyboard)


@dp.message(Command("info"))
async def cmd_info(message: Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Aiogram docs", url="https://docs.aiogram.dev/en/latest/"))
    await message.answer_photo(photo="https://images.app.goo.gl/LCDSYPs11Y4jDH9W8", reply_markup=builder.as_markup())


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
