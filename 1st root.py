from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config import TOKEN_API
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)