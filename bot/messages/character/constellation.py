from aiogram.utils.i18n import gettext as _, lazy_gettext as __

import genshin
from bot.messages import emoji


def title(
    character: genshin.Character
    ) -> str:
    return __(
        "{emoji.CONSTELLATION} Constellation \"{character.info.constellation}\" — {character.name} ({character.vision.name})"
    ).format(
        character=character,
        emoji=emoji
    )

def description(
    character: genshin.Character
    ) -> str:
    return __(
        "Tap to send constellation overview.\nType \"@GIDataBot {character.identifier} constellation\" for more options."
    ).format(
        character=character
    )

def text(
    character: genshin.Character,
    add_info: bool = False,
    ) -> str:
    strings = []

    strings.append(__(
        "<b>{emoji.CONSTELLATION} Constellation \"{character.info.constellation}\" — " \
        "{character.name} ({character.vision.name})</b>\n"
    ))

    for constellation in character.constellation:
        strings.append(__(
            "C{constellation.index}: {constellation.name}"
        ).format(
            constellation=constellation
        ))
    
    if add_info:
        strings.append(__(
            "\n<i>{emoji.INFO} Select constellation using buttons below.</i>"
        ))

    return "\n".join(map(str, strings)).format(
        character=character,
        emoji=emoji
    )

def button() -> str:
    return _(
        "{emoji.CONSTELLATION} Constellation"
    ).format(
        emoji=emoji
    )