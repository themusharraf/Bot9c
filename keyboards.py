from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

kb = [
    [
        types.KeyboardButton(text="Contact", request_contact=True),
        types.KeyboardButton(text="Location", request_location=True),

    ]
]
keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

shp = [[
    types.KeyboardButton(text="Telefonlar"),
    types.KeyboardButton(text="Planshet"),
    types.KeyboardButton(text="Televizor"),
    types.KeyboardButton(text="Noutbuklar"),
]]

shopping = types.ReplyKeyboardMarkup(keyboard=shp, resize_keyboard=True)

builder = InlineKeyboardBuilder()
builder.row(types.InlineKeyboardButton(
    text="1 667 000 so'm", url="https://uzum.uz/uz/product/smartfon-xiaomi-redmi-828900")
)
builder1 = InlineKeyboardBuilder()
builder1.row(types.InlineKeyboardButton(
    text="2 667 000 so'm", url="https://uzum.uz/uz/product/smartfon-honor-x8a-6128-gb-307462")
)
builder2 = InlineKeyboardBuilder()
builder2.row(types.InlineKeyboardButton(
    text="4 667 000 so'm", url="https://uzum.uz/uz/product/smartfon-xiaomi-redmi-12-596077?skuid=1228128")
)
builder3 = InlineKeyboardBuilder()
builder3.row(types.InlineKeyboardButton(
    text="3 667 000 so'm", url="https://uzum.uz/uz/product/samsung-galaxy-a14-464-814143")
)
