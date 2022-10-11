from aiocache import Cache
from deta import Deta

import genshin
from . import context

database = Deta().AsyncBase('users')

cache = Cache()
DEFAULT_TTL = 600

async def load_user(user_id: int) -> None:
    data = await cache.get(str(user_id))
    if not data:
        data = await database.get(str(user_id))

    if data:
        context.nickname.set(data['nickname'])
        context.language.set(data['language'])
        context.gender.set(data['gender'])
    else:  # set default
        context.nickname.set("Traveler")
        context.language.set("en")
        context.gender.set("M")
        await save_user(user_id)

async def save_user(user_id: int) -> None:
    
    # TODO: name change! or maybe not
    traveler = "aether_geo" if context.gender.get() == "M" else "lumine_geo"

    data = {
        "nickname": str(genshin.characters.get(traveler).name),
        "language": context.language.get(),
        "gender": context.gender.get()
    }

    await cache.set(str(user_id), data, ttl=DEFAULT_TTL)
    await database.put(data, str(user_id))

__all__ = [
    "database",
    "load_user",
    "save_user"
]
