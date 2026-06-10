import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiohttp import web

# Bot Token
API_TOKEN = '8253406057:AAFiTOw4fU-ewsBec1h5D7fBvFv-GAlILqk'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Tugmalar
menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_portfolio = KeyboardButton("📂 Bizning ishlarimiz (Portfolio)")
btn_about = KeyboardButton("ℹ️ Biz haqimizda")
btn_order = KeyboardButton("✍️ Buyurtma berish")
btn_calc = KeyboardButton("🧮 Mebel narxini hisoblash")

menu_keyboard.add(btn_portfolio, btn_calc, btn_about, btn_order)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    welcome_text = (
        f"Assalomu alaykum, {message.from_user.full_name}!\n"
        "**MEBEL_4422** rasmiy botiga xush kelibsiz.\n\n"
        "Quyidagi menyu orqali ishlarimiz bilan tanishishingiz yoki buyurtma qoldirishingiz mumkin 👇"
    )
    await message.reply(welcome_text, reply_markup=menu_keyboard, parse_mode="Markdown")

@dp.message_handler(lambda message: message.text == "ℹ️ Biz haqimizda")
async def about_us(message: types.Message):
    about_text = (
        "📐 **MEBEL_4422** — shkaflar, oshxona mebellari va har qanday turdagi custom "
        "mebellarni loyihalash va ishlab chiqarish bilan shug'undleydi."
    )
    await message.answer(about_text, parse_mode="Markdown")

@dp.message_handler(lambda message: message.text == "📂 Bizning ishlarimiz (Portfolio)")
async def show_portfolio(message: types.Message):
    await message.answer("Bu bo'limda tez kunda tayyorlangan mebellar rasmlari joylashtiriladi.")

@dp.message_handler(lambda message: message.text == "✍️ Buyurtma berish")
async def make_order(message: types.Message):
    await message.answer("✍️ **Buyurtma uchun:**\n\nIsmingiz va telefon raqamingizni yozib qoldiring.", parse_mode="Markdown")

@dp.message_handler(lambda message: message.text == "🧮 Mebel narxini hisoblash")
async def calc_mebel(message: types.Message):
    await message.answer("🧮 Tez kunda bu yerga aqlli kalkulyator qo'shiladi.")

# Render majburiy port talab qilgani uchun soxta veb-server
async def handle(request):
    return web.Response(text="Bot is running!")

async def on_startup(dp):
    import asyncio
    asyncio.create_task(dp.start_polling())

if __name__ == '__main__':
    app = web.Application()
    app.router.add_get('/', handle)
    
    # Portni Render taqdim etgan muhitdan olamiz
    port = int(os.environ.get("PORT", 10000))
    
    # Botni ishga tushirish
    dp.loop.create_task(on_startup(dp))
    web.run_app(app, host='0.0.0.0', port=port)
