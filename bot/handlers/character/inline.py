from typing import Tuple

from aiogram import types

import genshin
from bot import messages, keyboards


RESULTS_MAXSIZE = 50

def main(
    character: genshin.Character,
    inline: types.InlineQueryResult
    ) -> Tuple[types.InlineQueryResultArticle, str]:
    menu = next(iter(inline.query.split()[1:]), "main")

    if menu == "stats":
        return stats(character, inline)  # 1..90
    if menu in ("t", "talent"):
        return talent(character, inline)  # a, s, e, q, p1, p2, u
    if menu in ("c", "constellation"):
        return constellation(character)
    if menu in ("s", "story"):
        return story(character, inline)  # offsets
    if menu in ("q", "quote"):
        return quotes(character, inline)  # offsets

    return [
        types.InlineQueryResultArticle(
            id=character.identifier,
            title=messages.character.index.title(character),
            description=messages.character.index.description(),
            thumb_url=character.icon_url,
            input_message_content=types.InputTextMessageContent(
                message_text=messages.character.index.text(
                    character=character
                )
            ),
            reply_markup=keyboards.mention.keyboard()
        ),
        types.InlineQueryResultArticle(
            id=f"{character.identifier}:stats",
            title=messages.character.stats.title(character),
            description=messages.character.stats.description(),
            thumb_url=character.icon_url,  # TODO: talent ??? icon
            input_message_content=types.InputTextMessageContent(
                message_text=messages.character.stats.text(
                    character=character
                )
            ),
            reply_markup=keyboards.mention.keyboard()
        ),
        types.InlineQueryResultArticle(
            id=f"{character.identifier}:talent",
            title=messages.character.talents.title(character),
            description=messages.character.talents.description(character),
            thumb_url=character.icon_url,  # TODO: talent ??? icon
            input_message_content=types.InputTextMessageContent(
                message_text=messages.character.talents.text(
                    character=character
                )
            ),
            reply_markup=keyboards.mention.keyboard()
        ),
        types.InlineQueryResultArticle(
            id=f"{character.identifier}:constellation",
            title=messages.character.constellation.title(character),
            description=messages.character.constellation.description(character),
            thumb_url=character.icon_url,  # TODO: constellation artwork url
            input_message_content=types.InputTextMessageContent(
                message_text=messages.character.constellation.text(
                    character=character
                )
            ),
            reply_markup=keyboards.mention.keyboard()
        ),
        types.InlineQueryResultArticle(
            id=f"{character.identifier}:story",
            title=messages.character.story.title(character),
            description=messages.character.story.description(character),
            thumb_url=character.icon_url,  # TODO: story icon
            input_message_content=types.InputTextMessageContent(
                message_text=messages.character.story.text(
                    character=character
                )
            ),
            reply_markup=keyboards.mention.keyboard()
        ),
        types.InlineQueryResultArticle(
            id=f"{character.identifier}:quotes",
            title=messages.character.quotes.title(character),
            description=messages.character.quotes.description(character),
            thumb_url=character.icon_url,  # TODO: quotes icon
            input_message_content=types.InputTextMessageContent(
                message_text=messages.character.quotes.text(
                    character=character
                )
            ),
            reply_markup=keyboards.mention.keyboard()
        ),
    ], ""

def stats(
    character: genshin.Character,
    inline: types.InlineQueryResult
    ) -> Tuple[types.InlineQueryResultArticle, str]:
    return [
        types.InlineQueryResultArticle(
            id=f"{character.identifier}:stats",
            title=messages.character.stats.title(character),
            description=messages.character.stats.description(),
            thumb_url=character.icon_url,  # TODO: stats ??? icon
            input_message_content=types.InputTextMessageContent(
                message_text=messages.character.stats.text(
                    character=character
                )
            ),
            reply_markup=keyboards.mention.keyboard()
        ),
    ], ""

def talent(
    character: genshin.Character,
    inline: types.InlineQueryResult
    ) -> Tuple[types.InlineQueryResultArticle, str]:
    result = [
        types.InlineQueryResultArticle(
            id=f"{character.identifier}:talent",
            title=messages.character.talents.title(character),
            description=messages.character.talents.description(character),
            thumb_url=character.icon_url,  # TODO: talent icon ???
            input_message_content=types.InputTextMessageContent(
                message_text=messages.character.talents.text(
                    character=character
                )
            ),
            reply_markup=keyboards.mention.keyboard()
        )
    ]

    for talent in character.talents:
        result.append(
            types.InlineQueryResultArticle(
                id=f"{character.identifier}:talent:{talent.type}",
                title=messages.character.talent_view.title(talent),
                description=messages.character.talent_view.description(talent),
                thumb_url=character.icon_url,  # TODO: talent icon
                input_message_content=types.InputTextMessageContent(
                    message_text=messages.character.talent_view.text(
                        character=character,
                        talent=talent
                    )
                ),
                reply_markup=keyboards.mention.keyboard()
            )
        )

    return result, ""

def constellation(
    character: genshin.Character,
    ) -> Tuple[types.InlineQueryResultArticle, str]:
    result = [
        types.InlineQueryResultArticle(
            id=f"{character.identifier}:constellation",
            title=messages.character.constellation.title(character),
            description=messages.character.constellation.description(character),
            thumb_url=character.icon_url,  # TODO: constellation artwork url
            input_message_content=types.InputTextMessageContent(
                message_text=messages.character.constellation.text(
                    character=character
                )
            ),
            reply_markup=keyboards.mention.keyboard()
        )
    ]

    for constellation in character.constellation:
        result.append(
            types.InlineQueryResultArticle(
                id=f"{character.identifier}:constellation:{constellation.index}",
                title=messages.character.constellation_view.title(constellation),
                description=messages.character.constellation_view.description(constellation),
                thumb_url=character.icon_url,  # TODO: constellation icon url
                input_message_content=types.InputTextMessageContent(
                    message_text=messages.character.constellation_view.text(
                        character=character,
                        constellation=constellation
                    )
                ),
                reply_markup=keyboards.mention.keyboard()
            )
        )

    return result, ""

def story(
    character: genshin.Character,
    inline: types.InlineQueryResult
    ) -> Tuple[types.InlineQueryResultArticle, str]:
    start = int(inline.offset) if inline.offset else 0
    overall = len(character.story)

    if start >= overall:  # done
        stories = []
    elif start + RESULTS_MAXSIZE >= overall:  # last
        stories = character.story[start:overall+1]
    else:
        stories = character.story[start:start+RESULTS_MAXSIZE]
    
    if len(stories) < RESULTS_MAXSIZE:
        next_offset = ""
    else:
        next_offset = str(start + RESULTS_MAXSIZE)
    
    results = []
    for story in stories:
        results.append(
            types.InlineQueryResultArticle(
                id=f"{character.identifier}:story:{character.story.index(story)}",
                title=messages.character.story_view.title(character, story),
                description=messages.character.story_view.description(story),
                thumb_url=character.icon_url,  # TODO: story icon
                input_message_content=types.InputTextMessageContent(
                    message_text=messages.character.story_view.text(
                        character=character,
                        story=story
                    )
                ),
                reply_markup=keyboards.mention.keyboard()
            )
        )
    
    return results, next_offset

def quotes(
    character: genshin.Character,
    inline: types.InlineQueryResult
    ) -> Tuple[types.InlineQueryResultArticle, str]:
    start = int(inline.offset) if inline.offset else 0
    overall = len(character.quotes)

    if start >= overall:  # done
        quotes = []
    elif start + RESULTS_MAXSIZE >= overall:  # last
        quotes = character.quotes[start:overall+1]
    else:
        quotes = character.quotes[start:start+RESULTS_MAXSIZE]
    
    if len(quotes) < RESULTS_MAXSIZE:
        next_offset = ""
    else:
        next_offset = str(start + RESULTS_MAXSIZE)
    
    results = []
    for quote in quotes:
        results.append(
            types.InlineQueryResultArticle(
                id=f"{character.identifier}:quotes:{character.quotes.index(quote)}",
                title=messages.character.quote_view.title(character, quote),
                description=messages.character.quote_view.description(quote),
                thumb_url=character.icon_url,  # TODO: quotes icon
                input_message_content=types.InputTextMessageContent(
                    message_text=messages.character.quote_view.text(
                        character=character,
                        quote=quote
                    )
                ),
                reply_markup=keyboards.mention.keyboard()
            )
        )
    
    return results, next_offset
