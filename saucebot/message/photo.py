from aiogram import F
from saucebot.bot import dp
from aiogram.types import Message
from saucebot.utils import sauce2text
from saucebot.bot import bot, saucerer
from aiogram.types import URLInputFile


@dp.message(F.photo)
async def all_photo_handler(message: Message) -> None:
    """
    Handler for all photo processing. Process them through SauceNao and send the result to the user.
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

