import asyncio
import logging
import sys
import aiogram
from saucebot.bot import main

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    logging.info(aiogram.__version__)
    asyncio.run(main())

    