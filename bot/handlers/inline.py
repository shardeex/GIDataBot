from typing import *

from aiogram import Dispatcher, F, html, filters, types

import genshin
from bot import messages, handlers, keyboards
from database import context


RESULTS_MAXSIZE = 50

def parse_identifier(inline: types.InlineQuery) -> Tuple[list, str]:
    identifier = inline.query.split()[0]

    if identifier.startswith(("lumine", "aether")):
        if context.gender.get() == "M":
            item = genshin.items[identifier.replace("lumine", "aether")]
        else:
            item = genshin.items[identifier.replace("aether", "lumine")]
    else:
        item = genshin.items[identifier]

    if isinstance(item, genshin.Character):
        return handlers.character.inline.main(item, inline)

def parse_search(inline: types.InlineQuery) -> Tuple[list, str]:
    start = int(inline.offset) if inline.offset else 0
    search = inline.query.casefold()
    
    if context.gender.get() == "M":
        other_traveler = lambda x: str(x).startswith("lumine")
    else:
        other_traveler = lambda x: str(x).startswith("aether")
    
    items = [
        i for i in genshin.items.values()
        if search in str(i.name).casefold()\
            and not other_traveler(i.identifier)
    ]
    items.sort(key=lambda i: str(i.name))

    overall = len(items)

    if start >= overall:  # done
        items = []
    elif start + RESULTS_MAXSIZE >= overall:  # last
        items = items[start:overall+1]
    else:
        items = items[start:start+RESULTS_MAXSIZE]
    
    if len(items) < RESULTS_MAXSIZE:
        next_offset = ""
    else:
        next_offset = str(start + RESULTS_MAXSIZE)

    results = []
    for item in items:
        if isinstance(item, genshin.Character):
            title = messages.character.index.title(item)
            text = messages.character.index.text(item)

        results.append(
            types.InlineQueryResultArticle(
                id=item.identifier,
                title=title,
                description=messages.common.inline_default_description(item.identifier),
                thumb_url=item.icon_url,
                input_message_content=types.InputTextMessageContent(
                    message_text=text
                ),
                reply_markup=keyboards.mention.keyboard()
            )
        )
    
    if not results:
        results = [
            types.InlineQueryResultArticle(
                id="totallynormalresultipromise",
                title=messages.base.start.title(inline.from_user.full_name),
                description=messages.base.start.description(),
                # thumb_url=item.icon_url, # TODO: bot icon
                input_message_content=types.InputTextMessageContent(
                    message_text=messages.base.start.text(inline.from_user.full_name)
                ),
                reply_markup=keyboards.mention.keyboard()
            )
        ]

    return results, next_offset

async def index(inline: types.InlineQuery) -> None:
    if next(iter(inline.query.casefold().split()), "") in genshin.items.keys():
        results, next_offset = parse_identifier(inline)
    else:
        results, next_offset = parse_search(inline)

    await inline.answer(
        results=results,
        cache_time=0,      # I had to do this because of languages.
        is_personal=True,  # Otherwise it could mess up.
        next_offset=next_offset,
        switch_pm_text=messages.common.inline_help(),
        switch_pm_parameter="help"
    )

def setup(dispatcher: Dispatcher) -> None:
    dispatcher.inline_query.register(index)
