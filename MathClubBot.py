import requests
import logging
from aiogram.types import ContentType, Message
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from config import TOKEN_API
import asyncio
from aiogram.dispatcher.filters import Text
from Texts import START_TEXT, HELP_TEXT, START_VIDEOS, MATH31, MATH41, MATH42, MATH43, MATH44, \
    MATH51, MATH52, MATH53, MATH54, MATH61, MATH62, MATH63, MATH64, MATH71, MATH72, PHYS32, PHYS411, \
    PHYS412, PHYS413, PHYS414, PHYS415, PHYS511, PHYS512, PHYS513, PHYS514, PHYS515, PHYS611, PHYS731, \
    PHYS732, PROG33, PROG742, PROG431, PROG432, PROG433, PROG531, PROG631, PROG741
from Media.videos import videoIntegral1, videoIntegral2, videoDiffuri1, videoDiffuri2, \
    videoRyadi1, videoRyadi2, videoPredeli1, videoPredeli2, videoKinematika1, videoKinematika2, \
    videoElectichestvo1, videoElectichestvo2, videoMKT1, videoMKT2, videoMagnetism1, videoMagnetism2, \
    videoDinamika1, videoDinamika2, videoC1, videoC2
from Media.photos import photoRyadi, photoIntegrali, photoDiffuri, photoPredeli, photoPhysics, \
    photoC
from inlineKB import create_inline_keyboard_section_1, create_inline_keyboard_section_21,\
    create_inline_keyboard_section_31, create_inline_keyboard_section_41, \
    create_inline_keyboard_section_42, create_inline_keyboard_section_43, \
    create_inline_keyboard_section_44, create_inline_keyboard_section_51, \
    create_inline_keyboard_section_52, create_inline_keyboard_section_53, \
    create_inline_keyboard_section_54, create_inline_keyboard_section_61, \
    create_inline_keyboard_section_62, create_inline_keyboard_section_63, \
    create_inline_keyboard_section_64, create_inline_keyboard_section_711, \
    create_inline_keyboard_section_712, create_inline_keyboard_section_713, \
    create_inline_keyboard_section_714, create_inline_keyboard_section_721, \
    create_inline_keyboard_section_722, create_inline_keyboard_section_723, \
    create_inline_keyboard_section_724, create_inline_keyboard_section_32, \
    create_inline_keyboard_section_411, create_inline_keyboard_section_412, \
    create_inline_keyboard_section_413, create_inline_keyboard_section_414, \
    create_inline_keyboard_section_415, create_inline_keyboard_section_511, \
    create_inline_keyboard_section_512, create_inline_keyboard_section_513, \
    create_inline_keyboard_section_514, create_inline_keyboard_section_515, \
    create_inline_keyboard_section_611, create_inline_keyboard_section_731, \
    create_inline_keyboard_section_732, create_inline_keyboard_section_33, \
    create_inline_keyboard_section_531, create_inline_keyboard_section_431, \
    create_inline_keyboard_section_741, create_inline_keyboard_section_742, \
    create_inline_keyboard_section_631
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
url = f"https://api.telegram.org/bot{TOKEN_API}/getUpdates"

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

loop = asyncio.get_event_loop()


@dp.callback_query_handler(lambda c: c.data.startswith('section'))
async def process_callback_section(callback_query: types.CallbackQuery):
    await callback_query.answer()
    section = int(callback_query.data.split('_')[1])
    keyboard = None

    if section == 1:
        keyboard = create_inline_keyboard_section_1()
        await bot.send_message(callback_query.from_user.id, START_TEXT,
                               reply_markup=keyboard)
    elif section == 21:
        keyboard = create_inline_keyboard_section_21()
        await bot.send_message(callback_query.from_user.id, START_VIDEOS,
                               reply_markup=keyboard)
    elif section == 31:
        keyboard = create_inline_keyboard_section_31()
        await bot.send_message(callback_query.from_user.id, MATH31,
                               reply_markup=keyboard)
    elif section == 41:
        keyboard = create_inline_keyboard_section_41()
        await bot.send_video(callback_query.from_user.id, video=videoIntegral1,
                             caption=MATH41,
                             reply_markup=keyboard)
    elif section == 42:
        keyboard = create_inline_keyboard_section_42()
        await bot.send_video(callback_query.from_user.id, video=videoRyadi1,
                             caption=MATH42,
                             reply_markup=keyboard)
    elif section == 43:
        keyboard = create_inline_keyboard_section_43()
        await bot.send_video(callback_query.from_user.id, video=videoDiffuri1,
                             caption=MATH43,
                             reply_markup=keyboard)
    elif section == 44:
        keyboard = create_inline_keyboard_section_44()
        await bot.send_video(callback_query.from_user.id, video=videoPredeli1,
                             caption=MATH44,
                             reply_markup=keyboard)
    elif section == 51:
        keyboard = create_inline_keyboard_section_51()
        await bot.send_video(callback_query.from_user.id, video=videoIntegral2,
                             caption=MATH51,
                             reply_markup=keyboard)
    elif section == 52:
        keyboard = create_inline_keyboard_section_52()
        await bot.send_video(callback_query.from_user.id, video=videoRyadi2,
                             caption=MATH52,
                             reply_markup=keyboard)
    elif section == 53:
        keyboard = create_inline_keyboard_section_53()
        await bot.send_video(callback_query.from_user.id, video=videoDiffuri2,
                             caption=MATH53,
                             reply_markup=keyboard)
    elif section == 54:
        keyboard = create_inline_keyboard_section_54()
        await bot.send_video(callback_query.from_user.id, video=videoPredeli2,
                             caption=MATH54,
                             reply_markup=keyboard)
    elif section == 61:
        keyboard = create_inline_keyboard_section_61()
        await bot.send_photo(callback_query.from_user.id, photo=photoIntegrali,
                             caption=MATH61,
                             reply_markup=keyboard)
    elif section == 62:
        keyboard = create_inline_keyboard_section_62()
        await bot.send_photo(callback_query.from_user.id, photo=photoRyadi,
                             caption=MATH62,
                             reply_markup=keyboard)
    elif section == 63:
        keyboard = create_inline_keyboard_section_63()
        await bot.send_photo(callback_query.from_user.id, photo=photoDiffuri,
                             caption=MATH63,
                             reply_markup=keyboard)
    elif section == 64:
        keyboard = create_inline_keyboard_section_64()
        await bot.send_photo(callback_query.from_user.id, photo=photoPredeli,
                             caption=MATH64,
                             reply_markup=keyboard)
    elif section == 711:
        keyboard = create_inline_keyboard_section_711()
        await bot.send_message(callback_query.from_user.id, f"{callback_query.from_user.full_name}" + MATH71,
                               reply_markup=keyboard)
    elif section == 712:
        keyboard = create_inline_keyboard_section_712()
        await bot.send_message(callback_query.from_user.id, f"{callback_query.from_user.full_name}" + MATH71,
                               reply_markup=keyboard)
    elif section == 713:
        keyboard = create_inline_keyboard_section_713()
        await bot.send_message(callback_query.from_user.id, f"{callback_query.from_user.full_name}" + MATH71,
                               reply_markup=keyboard)
    elif section == 714:
        keyboard = create_inline_keyboard_section_714()
        await bot.send_message(callback_query.from_user.id, f"{callback_query.from_user.full_name}" + MATH71,
                               reply_markup=keyboard)
    elif section == 721:
        keyboard = create_inline_keyboard_section_721()
        await bot.send_message(callback_query.from_user.id, f"{callback_query.from_user.full_name}" + MATH72,
                               reply_markup=keyboard)
    elif section == 722:
        keyboard = create_inline_keyboard_section_722()
        await bot.send_message(callback_query.from_user.id, f"{callback_query.from_user.full_name}" + MATH72,
                               reply_markup=keyboard)
    elif section == 723:
        keyboard = create_inline_keyboard_section_723()
        await bot.send_message(callback_query.from_user.id, f"{callback_query.from_user.full_name}" + MATH72,
                               reply_markup=keyboard)
    elif section == 724:
        keyboard = create_inline_keyboard_section_724()
        await bot.send_message(callback_query.from_user.id, f"{callback_query.from_user.full_name}" + MATH72,
                               reply_markup=keyboard)
    elif section == 32:
        keyboard = create_inline_keyboard_section_32()
        await bot.send_message(callback_query.from_user.id,
                               text=PHYS32,
                               reply_markup=keyboard)
    elif section == 411:
        keyboard = create_inline_keyboard_section_411()
        await bot.send_video(callback_query.from_user.id, video=videoElectichestvo1,
                             caption=PHYS411,
                             reply_markup=keyboard)
    elif section == 412:
        keyboard = create_inline_keyboard_section_412()
        await bot.send_video(callback_query.from_user.id, video=videoMagnetism1,
                             caption=PHYS412,
                             reply_markup=keyboard)
    elif section == 413:
        keyboard = create_inline_keyboard_section_413()
        await bot.send_video(callback_query.from_user.id, video=videoMKT1,
                             caption=PHYS413,
                             reply_markup=keyboard)
    elif section == 414:
        keyboard = create_inline_keyboard_section_414()
        await bot.send_video(callback_query.from_user.id, video=videoKinematika1,
                             caption=PHYS414,
                             reply_markup=keyboard)
    elif section == 415:
        keyboard = create_inline_keyboard_section_415()
        await bot.send_video(callback_query.from_user.id, video=videoDinamika1,
                             caption=PHYS415,
                             reply_markup=keyboard)
    elif section == 511:
        keyboard = create_inline_keyboard_section_511()
        await bot.send_video(callback_query.from_user.id, video=videoElectichestvo2,
                             caption=PHYS511,
                             reply_markup=keyboard)
    elif section == 512:
        keyboard = create_inline_keyboard_section_512()
        await bot.send_video(callback_query.from_user.id, video=videoMagnetism2,
                             caption=PHYS512,
                             reply_markup=keyboard)
    elif section == 513:
        keyboard = create_inline_keyboard_section_513()
        await bot.send_video(callback_query.from_user.id, video=videoMKT2,
                             caption=PHYS513,
                             reply_markup=keyboard)
    elif section == 514:
        keyboard = create_inline_keyboard_section_514()
        await bot.send_video(callback_query.from_user.id, video=videoKinematika2,
                             caption=PHYS514,
                             reply_markup=keyboard)
    elif section == 515:
        keyboard = create_inline_keyboard_section_515()
        await bot.send_video(callback_query.from_user.id, video=videoDinamika2,
                             caption=PHYS515,
                             reply_markup=keyboard)
    elif section == 611:
        keyboard = create_inline_keyboard_section_611()
        await bot.send_photo(callback_query.from_user.id, photo=photoPhysics,
                             caption=PHYS611,
                             reply_markup=keyboard)
    elif section == 731:
        keyboard = create_inline_keyboard_section_731()
        await bot.send_message(callback_query.from_user.id,
                               text=f"{callback_query.from_user.full_name}" + PHYS731,
                               reply_markup=keyboard)
    elif section == 732:
        keyboard = create_inline_keyboard_section_732()
        await bot.send_message(callback_query.from_user.id,
                               text=f"{callback_query.from_user.full_name}" + PHYS732,
                               reply_markup=keyboard)
    elif section == 33:
        keyboard = create_inline_keyboard_section_33()
        await bot.send_message(callback_query.from_user.id,
                               text=PROG33,
                               reply_markup=keyboard)
    elif section == 431:
        keyboard = create_inline_keyboard_section_431()
        await bot.send_video(callback_query.from_user.id, video=videoC1,
                             caption=PROG431,
                             reply_markup=keyboard)
    elif section == 432:
        await bot.send_message(callback_query.from_user.id,
                               text=PROG432)
    elif section == 433:
        await bot.send_message(callback_query.from_user.id,
                               text=PROG433)
    elif section == 531:
        keyboard = create_inline_keyboard_section_531()
        await bot.send_video(callback_query.from_user.id, video=videoC2,
                             caption=PROG531,
                             reply_markup=keyboard)
    elif section == 631:
        keyboard = create_inline_keyboard_section_631()
        await bot.send_photo(callback_query.from_user.id, photo=photoC,
                             caption=PROG631,
                             reply_markup=keyboard)
    elif section == 741:
        keyboard = create_inline_keyboard_section_741()
        await bot.send_message(callback_query.from_user.id,
                               text=f"{callback_query.from_user.full_name}" + PROG741,
                               reply_markup=keyboard)
    elif section == 742:
        keyboard = create_inline_keyboard_section_742()
        await bot.send_message(callback_query.from_user.id,
                               text=f"{callback_query.from_user.full_name}" + PROG742,
                               reply_markup=keyboard)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = create_inline_keyboard_section_1()
    await message.answer(f"Привет. {message.chat.full_name}!" + START_TEXT,
                         reply_markup=markup)


@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_file_id(message: Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=ContentType.VIDEO)
async def send_video_file_id(message: Message):
    await message.reply(message.video.file_id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)





