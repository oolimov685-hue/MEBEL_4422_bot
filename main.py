import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = '8253406057:AAFiTOw4fU-ewsBec1h5D7fBvFv-GAlILqk'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

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
        "Sizga sifatli va zamonaviy mebel loyihalarini taqdim etishdan mamnunmiz. "
        "Quyidagi menyu orqali ishlarimiz bilan tanishishingiz yoki buyurtma qoldirishingiz mumkin 👇"
    )
    await message.reply(welcome_text, reply_markup=menu_keyboard, parse_mode="Markdown")

@dp.message_handler(lambda message: message.text == "ℹ️ Biz haqimizda")
async def about_us(message: types.Message):
    about_text = (
        "📐 **MEBEL_4422** — shkaflar, oshxona mebellari va har qanday turdagi custom "
        "mebellarni loyihalash va ishlab chiqarish bilan shug'ullanadi.\n\n"
        "Biz har bir loyihaga individual yondashib, uning 3D modelini chizib beramiz "
        "va yuqori sifatli materiallardan foydalanamiz."
    )
    await message.answer(about_text, parse_mode="Markdown")

@dp.message_handler(lambda message: message.text == "📂 Bizning ishlarimiz (Portfolio)")
async def show_portfolio(message: types.Message):
    portfolio_text = (
        "Bu bo'limda tez kunda biz tomondan tayyorlangan eng so'nggi va zamonaviy "
        "mebel loyihalari, shkaflar hamda oshxona mebellari rasmlari joylashtiriladi."
    )
    await message.answer(portfolio_text)

@dp.message_handler(lambda message: message.text == "✍️ Buyurtma berish")
async def make_order(message: types.Message):
    order_text = (
        "✍️ **Buyurtma berish yoki konsultatsiya olish uchun:**\n\n"
        "Iltimos, ismingiz, telefon raqamingiz va qanday mebel buyurtma qilmoqchi "
        "ekanligingizni yozib qoldiring. Mutaxassislarimiz siz bilan tez fursatda bog'lanishadi!"
    )
    await message.answer(order_text, parse_mode="Markdown")

@dp.message_handler(lambda message: message.text == "🧮 Mebel narxini hisoblash")
async def calc_mebel(message: types.Message):
    calc_text = (
        "🧮 **Mebel narxini dastlabki hisoblash:**\n\n"
        "Yaqin orada bu yerga o'lchamlar va ishlatiladigan materiallarni kiritib, "
        "mebelning taxminiy narxini chiqarib beradigan aqlli kalkulyator qo'shiladi."
    )
    await message.answer(calc_text, parse_mode="Markdown")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
