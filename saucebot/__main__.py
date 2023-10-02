import asyncio
import logging
import sys

from saucebot.bot import main
import saucebot.message

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())