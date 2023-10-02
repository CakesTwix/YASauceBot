from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from saucerer import Saucerer

# Bot token can be obtained via https://t.me/BotFather
TOKEN = ""

# Initialize Bot instance with a default parse mode which will be passed to all API calls
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

saucerer = Saucerer()

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


async def main() -> None:
    # And the run events dispatching
    await dp.start_polling(bot)
