import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command, CommandStart
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

buttons = [
    [KeyboardButton(text='Backend'), KeyboardButton(text='Frontend')],
    [KeyboardButton(text='UX/UI'), KeyboardButton(text="О нас")]
]

keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

contact_buttons = [
    [KeyboardButton(text='Связаться с нами')]
]

contact_keyboard = ReplyKeyboardMarkup(keyboard=contact_buttons, resize_keyboard=True)

@dp.message(CommandStart())
async def start_bot(message: Message):
    await message.reply(f"Привет {message.from_user.first_name}!", reply_markup=keyboard)

@dp.message(Command("help"))
async def help_command(message: Message):
    await message.reply("Помогу чем смогу. Используй /start для начала.")

@dp.message(F.text == "Backend")
async def backend_info(message: Message):
    await message.reply(
        "*Backend* — это внутренняя часть веб-приложений или сайтов, которая отвечает за работу с данными и бизнес-логикой. Если представить сайт как ресторан, то *Frontend* — это то, что видит посетитель (оформление и меню), а *Backend* — это кухня, где происходят все процессы: готовка блюд, хранение продуктов и управление заказами.",
        parse_mode='Markdown'
    )
    await message.reply("Вы можете связаться с нами по следующим контактам:\nТелефон: +996 (557) 05 2018\nEmail: office@geeks.kg")

@dp.message(F.text == "Frontend")
async def frontend_info(message: Message):
    await message.reply(
        "*Frontend* — это внешняя часть веб-приложений или сайтов, то, что видит и с чем взаимодействует пользователь. Если сайт — это машина, то *Frontend* — это панель управления, руль и кнопки, которые вы видите и используете.",
        parse_mode='Markdown'
    )
    

@dp.message(F.text == "UX/UI")
async def ux_ui_info(message: Message):
    await message.reply(
        "**UX/UI** — это создание сайтов и приложений, которые одновременно удобны и красивы. *UX* (пользовательский опыт) делает так, чтобы пользоваться продуктом было легко и интуитивно понятно, а *UI* (пользовательский интерфейс) отвечает за его привлекательный внешний вид и визуальные детали. Вместе они делают так, чтобы продукт был и удобным, и приятным для глаз.",
        parse_mode='Markdown'
    )
    await message.reply("Вы можете связаться с нами по следующим контактам:\nТелефон: +996 (557) 05 2018\nEmail: office@geeks.kg")

@dp.message(F.text == "О нас")
async def about_us(message: Message):
    await message.reply(
        "Мы самая передовая компания в IT-сфере в Кыргызстане! Мы выпустили более 20.000 студентов, которые на данное время работают на успешные компании. Мы предлагаем вам уникальные возможности, которые имеются только у нас. Успейте зарегистрироваться на одно из направлений до следующей недели и получите 50% скидку на первый месяц!"
    )

@dp.message()
async def echo(message: Message):
    await message.answer("Я вас не понял, попробуйте снова.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")
