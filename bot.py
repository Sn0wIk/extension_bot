import aiogram, asyncio, os, uuid, converter
from config import token
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile, ReplyKeyboardMarkup, KeyboardButton

bot = Bot(token=token)
dp = Dispatcher()

os.makedirs('tempfiles', exist_ok = true)

tempway - {}

@dp.message(CommandStart())
async def start(message: types.Message)
    await bot.send_message(message.chat.id, 'дарова мабой\nтут мы короче жоска гангстерим и меняем эти бквы после точки у файлов\nкидаешь сюда пнг а мы тебе пдфку ема круто да? ну вот и я о том же\nтыкай команду /swag  дальше короче зёма')

@dp.message(Command("swag"))
    await bot.send_message(message.chat.id, 'отправляй свой файл с расширениями jpg png или pdf')

@dp.message(F.photo | F.document)
    async def handle_file(message: types.Message):

