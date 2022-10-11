from datetime import datetime
import logging

from aiogram import Bot, types
from fastapi import FastAPI

from bot import dispatcher


logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

app = FastAPI()
starttime = datetime.now()

@app.post('/bot{token}/')
async def process_update(token: str, update: types.Update):
    bot = Bot(token=token, parse_mode='HTML')
    try:
        await dispatcher.feed_update(bot, update)
        await bot.session.close()
    except Exception as error:
        # await error_dispatcher.feed_update(bot, update)
        logger.exception(error)

@app.get('/')
def read_root():
    return f'@GIDataBot is running for {datetime.now() - starttime}'

"""
TODO:

1) main callback. aLl information I need in callbacks:
menu_id, identifier (optional) and index (optional). that's all!
other callback make it only harder to import and navigate between
different callback categories.

"""