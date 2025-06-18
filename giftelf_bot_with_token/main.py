from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я готов к работе.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
