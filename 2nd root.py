
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config import TOKEN_API
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands='Связаться с отделом заботы')
async def care(message: types.Message):
    await message.answer(text="Открываем доступ к твоему чату отделу заботы. Свободный сотрудник уже скоро напишет тебе. Вы обсудите твою ситуацию, план подготовки, чем и как мы можем помочь 😌 \n Пока мы бежим к тебе - опиши свой запрос")
    await bot.send_message(chat_id=778862180,text="Новенький птенчик",parse_mode="HTML")


@dp.message_handler(commands="Назад")
async def back(message: types.Message):
    await bot.send_message(chat_id=778862180, text="Новенький птенчик", parse_mode="HTML")