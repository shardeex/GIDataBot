from aiogram.utils.i18n import gettext as _, lazy_gettext as __

import genshin
from bot.messages import emoji


def text(
    character: genshin.Character,
    add_info: bool = False
    ):
    strings = []

    strings.append(__(
        "<b>{emoji.ABOUT} About — {character.name} ({character.vision.name})</b>\n\n" \
        "Here you can read (and listen: coming soon!) character story and quotes.\n" \
    ))

    if add_info:
        strings.append(__(
            "<i>{emoji.INFO} Select category using buttons below.</i>"
        ))

    return "\n".join(map(str, strings)).format(
        character=character,
        emoji=emoji
    )

def button() -> str:
    return _(
        "{emoji.ABOUT} About"
    ).format(
        emoji=emoji
    )
