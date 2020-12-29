import asyncio

from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN, admin_id
import requests as request


url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id=1269621546&text=Mana text qo'limdan keladii!"
request.get(url)
exit()

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)

if __name__ == "__main__":
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)