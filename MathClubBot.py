from aiogram.types import ContentType, Message
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN_API
from helpers.DataBases import start_table, update_last_step, cursor, connection, labels_create, labels_edit, info_table
from helpers.timezone import get_msk_time
import asyncio
import json
import os
import requests
from Web.WebSockets import send_data_to_server, start_update
from Texts import START_TEXT, START_VIDEOS, MATH31, MATH41, MATH42, MATH43, MATH44, \
    MATH51, MATH52, MATH53, MATH54, MATH61, MATH62, MATH63, MATH64, MATH71, MATH72, PHYS32, PHYS411, \
    PHYS412, PHYS413, PHYS414, PHYS415, PHYS511, PHYS512, PHYS513, PHYS514, PHYS515, PHYS611, PHYS731, \
    PHYS732, PROG33, PROG742, PROG431, PROG432, PROG433, PROG531, PROG631, PROG741, LINAL441, \
    LINAL541, LINAL641, LINAL751, LINAL752, TERVER451, TERVER551, TERVER651, TERVER761, \
    TERVER762, MATFIZ561, MATFIZ661, MATFIZ771, MATFIZ772, FIZHIM581, FIZHIM38, FIZHIM481, \
    FIZHIM582, RASSILKA23, POLEZNOVISMAT, POLEZNO22, POLEZNOPROGA, POLEZNOEKONOM, POLEZNOFIZIKA, \
    POLEZNAYAPODPISKA1, EKONOM, HYMYA37
from Media.videos import videoIntegral1, videoIntegral2, videoDiffuri1, videoDiffuri2, \
    videoRyadi1, videoRyadi2, videoPredeli1, videoPredeli2, videoKinematika1, videoKinematika2, \
    videoElectichestvo1, videoElectichestvo2, videoMKT1, videoMKT2, videoMagnetism1, videoMagnetism2, \
    videoDinamika1, videoDinamika2, videoC1, videoC2, videoLinal1, videoLinal2, videoMatfiz1, videoTerver1, \
    videoTerver2
from Media.photos import photoRyadi, photoIntegrali, photoDiffuri, photoPredeli, photoPhysics, \
    photoC, photoLinal, photoMatfiz, photoTerver
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
    create_inline_keyboard_section_631, create_inline_keyboard_section_441, \
    create_inline_keyboard_section_541, create_inline_keyboard_section_641, \
    create_inline_keyboard_section_751, create_inline_keyboard_section_752, \
    create_inline_keyboard_section_451, create_inline_keyboard_section_551, \
    create_inline_keyboard_section_651, create_inline_keyboard_section_761, \
    create_inline_keyboard_section_762, create_inline_keyboard_section_561, \
    create_inline_keyboard_section_661, create_inline_keyboard_section_771, \
    create_inline_keyboard_section_772, create_inline_keyboard_section_481, \
    create_inline_keyboard_section_581, create_inline_keyboard_section_582, \
    create_inline_keyboard_section_37, create_inline_keyboard_section_38, \
    create_inline_keyboard_section_22, create_inline_keyboard_section_1001, \
    create_inline_keyboard_section_1002, create_inline_keyboard_section_1003, \
    create_inline_keyboard_section_1004, create_inline_keyboard_section_39
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
url = f"https://api.telegram.org/bot{TOKEN_API}/getUpdates"

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

loop = asyncio.get_event_loop()
all_labels = []

messages_store = []


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
    elif section == 441:
        keyboard = create_inline_keyboard_section_441()
        await bot.send_video(callback_query.from_user.id, video=videoLinal1,
                             caption=LINAL441,
                             reply_markup=keyboard)
    elif section == 541:
        keyboard = create_inline_keyboard_section_541()
        await bot.send_video(callback_query.from_user.id, video=videoLinal2,
                             caption=LINAL541,
                             reply_markup=keyboard)
    elif section == 641:
        keyboard = create_inline_keyboard_section_641()
        await bot.send_photo(callback_query.from_user.id, photo=photoLinal,
                             caption=LINAL641,
                             reply_markup=keyboard)
    elif section == 751:
        keyboard = create_inline_keyboard_section_751()
        await bot.send_message(callback_query.from_user.id,
                               text=f"{callback_query.from_user.full_name}" + LINAL751,
                               reply_markup=keyboard)
    elif section == 752:
        keyboard = create_inline_keyboard_section_752()
        await bot.send_message(callback_query.from_user.id,
                               text=f"{callback_query.from_user.full_name}" + LINAL752,
                               reply_markup=keyboard)
    elif section == 451:
        keyboard = create_inline_keyboard_section_451()
        await bot.send_video(callback_query.from_user.id, video=videoTerver1,
                             caption=TERVER451,
                             reply_markup=keyboard)
    elif section == 551:
        keyboard = create_inline_keyboard_section_551()
        await bot.send_video(callback_query.from_user.id, video=videoTerver2,
                             caption=TERVER551,
                             reply_markup=keyboard)
    elif section == 651:
        keyboard = create_inline_keyboard_section_651()
        await bot.send_photo(callback_query.from_user.id, photo=photoTerver,
                             caption=TERVER651,
                             reply_markup=keyboard)
    elif section == 761:
        keyboard = create_inline_keyboard_section_761()
        await bot.send_message(callback_query.from_user.id,
                               text=f"{callback_query.from_user.full_name}" + TERVER761,
                               reply_markup=keyboard)
    elif section == 762:
        keyboard = create_inline_keyboard_section_762()
        await bot.send_message(callback_query.from_user.id,
                               text=f"{callback_query.from_user.full_name}" + TERVER762,
                               reply_markup=keyboard)
    elif section == 561:
        keyboard = create_inline_keyboard_section_561()
        await bot.send_video(callback_query.from_user.id, video=videoMatfiz1,
                             caption=MATFIZ561,
                             reply_markup=keyboard)
    elif section == 661:
        keyboard = create_inline_keyboard_section_661()
        await bot.send_photo(callback_query.from_user.id, photo=photoMatfiz,
                             caption=MATFIZ661,
                             reply_markup=keyboard)
    elif section == 771:
        keyboard = create_inline_keyboard_section_771()
        await bot.send_message(callback_query.from_user.id,
                               text=f"{callback_query.from_user.full_name}" + MATFIZ771,
                               reply_markup=keyboard)
    elif section == 772:
        keyboard = create_inline_keyboard_section_772()
        await bot.send_message(callback_query.from_user.id,
                               text=f"{callback_query.from_user.full_name}" + MATFIZ772,
                               reply_markup=keyboard)
    elif section == 37:
        keyboard = create_inline_keyboard_section_37()
        await bot.send_message(callback_query.from_user.id,
                               text=f"{callback_query.from_user.full_name}" + HYMYA37,
                               reply_markup=keyboard)
    elif section == 471:
        await bot.send_message(callback_query.from_user.id,
                               text=f"{callback_query.from_user.full_name}" + PROG741)
    elif section == 472:
        await bot.send_message(callback_query.from_user.id,
                               text=f"{callback_query.from_user.full_name}" + PROG742)
    elif section == 38:
        keyboard = create_inline_keyboard_section_38()
        await bot.send_message(callback_query.from_user.id,
                               text=f"{callback_query.from_user.full_name}" + FIZHIM38,
                               reply_markup=keyboard)
    elif section == 481:
        keyboard = create_inline_keyboard_section_481()
        await bot.send_video(callback_query.from_user.id, video=videoMatfiz1,
                             caption=FIZHIM481,
                             reply_markup=keyboard)
    elif section == 581:
        keyboard = create_inline_keyboard_section_581()
        await bot.send_message(callback_query.from_user.id,
                               text=f"{callback_query.from_user.full_name}" + FIZHIM581,
                               reply_markup=keyboard)
    elif section == 582:
        keyboard = create_inline_keyboard_section_582()
        await bot.send_message(callback_query.from_user.id,
                               text=f"{callback_query.from_user.full_name}" + FIZHIM582,
                               reply_markup=keyboard)
    elif section == 39:
        keyboard = create_inline_keyboard_section_39()
        await bot.send_message(callback_query.from_user.id,
                               text=EKONOM,
                               reply_markup=keyboard)
    elif section == 491:
        await bot.send_message(callback_query.from_user.id,
                               text=PROG432)
    elif section == 492:
        await bot.send_message(callback_query.from_user.id,
                               text=PROG432)
    elif section == 493:
        await bot.send_message(callback_query.from_user.id,
                               text=PROG432)
    elif section == 494:
        await bot.send_message(callback_query.from_user.id,
                               text=PROG432)
    elif section == 23:
        await bot.send_message(callback_query.from_user.id,
                               text=RASSILKA23)
    elif section == 22:
        keyboard = create_inline_keyboard_section_22()
        await bot.send_message(callback_query.from_user.id,
                               text=POLEZNO22,
                               reply_markup=keyboard)
    elif section == 1001:
        keyboard = create_inline_keyboard_section_1001()
        await bot.send_message(callback_query.from_user.id,
                               text=POLEZNOVISMAT,
                               reply_markup=keyboard)
    elif section == 1002:
        keyboard = create_inline_keyboard_section_1002()
        await bot.send_message(callback_query.from_user.id,
                               text=POLEZNOFIZIKA,
                               reply_markup=keyboard)
    elif section == 1003:
        keyboard = create_inline_keyboard_section_1003()
        await bot.send_message(callback_query.from_user.id,
                               text=POLEZNOPROGA,
                               reply_markup=keyboard)
    elif section == 1004:
        keyboard = create_inline_keyboard_section_1004()
        await bot.send_message(callback_query.from_user.id,
                               text=POLEZNOEKONOM,
                               reply_markup=keyboard)
    elif section == 1000:
        await asyncio.sleep(10)
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=POLEZNAYAPODPISKA1)
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text="А рассылочка то работает и даже удобнее")
    update_last_step(tg_id=callback_query.from_user.id, date=get_msk_time(), section=section)
    all_labels.append(section)
    labels_create()
    labels_edit(tg_id=int(callback_query.from_user.id), all_labels=str(all_labels))


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = create_inline_keyboard_section_1()
    start_table()
    labels_create()
    all_labels.append(1)
    info_table(tg_id=int(message.from_user.id), username=message.from_user.full_name)
    update_last_step(message.from_user.id, get_msk_time(), "1")
    labels_edit(message.from_user.id, all_labels=str(all_labels))
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





