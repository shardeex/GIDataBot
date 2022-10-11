from aiogram.utils.i18n import gettext as __

import genshin
from bot.messages import emoji


def title(
    character: genshin.Character,
    quote: genshin.About
    ) -> str:
    return __(
        "{emoji.QUOTE} {quote.title} — {character.name} ({character.vision.name})"
    ).format(
        character=character,
        quote=quote,
        emoji=emoji
    )

def description(
    quote: genshin.About
    ) -> str:
    return __(
        "\"{quote.text}\""
    ).format(
        quote=quote
    )

def text(
    character: genshin.Character,
    quote: genshin.About
    ):
    strings = []

    strings.append(__(
        "<b>{emoji.QUOTE} {quote.title} — {character.name} ({character.vision.name})</b>\n\n" \
        "{quote.text}\n\n" \
        "<i>{emoji.INFO} Condition: {quote.condition}</i>"
    ))

    return "\n".join(map(str, strings)).format(
        character=character,
        quote=quote,
        emoji=emoji
    )
