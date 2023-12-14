import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from keyboards import *

TOKEN = ""

logging.basicConfig(level=logging.INFO)

dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(f"Assalomu alekum {message.from_user.first_name}")


@dp.message(F.text == "info")
async def info(message: Message):
    await message.answer("send location or contact", reply_markup=keyboard)


@dp.message(F.text == "shop")
async def shop(message: Message):
    await message.answer("Shopping choice", reply_markup=shopping)

    @dp.message(F.text == "Telefonlar")
    async def shop(message: Message):
        await message.answer_photo(photo="https://images.uzum.uz/clfkjlnn7c6qm23k45qg/original.jpg",
                                   caption="Smartfon Xiaomi Redmi 13C\n 4GB+128GB I 8GB+256GB \n 6.74 90Hz, 5000mAh \n Dual SIM, 4G LTE",
                                   reply_markup=builder.as_markup())
        await message.answer_photo(photo="https://images.uzum.uz/cjqn39kjvf2hdh3ejor0/original.jpg",
                                   caption="Smartfon Honor X8a 6/128 Gb \n Operatsion tizim: Android 12, MagicUI 6.1 \n Asosiy kamera: 100 Mp + 5 Mp + 2 Mp, frontal kamera: 16 Mp",
                                   reply_markup=builder1.as_markup())
        await message.answer_photo(photo="https://images.uzum.uz/cjhj5rjk9fq53ftenlm0/original.jpg",
                                   caption="Smartfon Xiaomi Redmi 12C\n 4GB+128GB I 8GB+256GB \n Dual SIM, 4G LTE",
                                   reply_markup=builder2.as_markup())
        await message.answer_photo(photo="https://images.uzum.uz/clpurqps99oopol185cg/original.jpg",
                                   caption="Samsung Galaxy A14 4/64 \n 4GB+128GB I 8GB+256GB \n 6.74 90Hz, 5000mAh \n Dual SIM, 4G LTE",
                                   reply_markup=builder3.as_markup())


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
