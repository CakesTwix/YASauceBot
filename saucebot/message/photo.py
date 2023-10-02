from aiogram import F
from saucebot.bot import dp
from aiogram.types import Message
from saucerer import Saucerer
from saucebot.utils import sauce2text
from saucebot.bot import bot, saucerer
from aiogram.types import URLInputFile

@dp.message(F.photo)
async def all_photo_handler(message: Message):
    """
    """
    search_result = (await saucerer.search(
        await bot.download(
            message.photo[0].file_id
        )
    )).sauces

    await message.answer_photo(
        URLInputFile(search_result[0].image_url),
        sauce2text(search_result[0])
    )

    # await saucerer.close()