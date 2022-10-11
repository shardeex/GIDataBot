from aiogram.utils.i18n import gettext as _, lazy_gettext as __

import genshin
from bot.messages import emoji


def title(
    character: genshin.Character
    ) -> str:
    return __(
        "{emoji.QUOTE} Quotes — {character.name} ({character.vision.name})"
    ).format(
        character=character,
        emoji=emoji
    )

def description(
    character: genshin.Character
    ) -> str:
    return __(
        "Tap to send quotes overview.\nType \"@GIDataBot {character.identifier} quote\" for more options."
    ).format(
        character=character
    )

def text(
    character: genshin.Character,
    add_info: bool = False
    ):
    strings = []

    strings.append(__(
        "<b>{emoji.QUOTE} Quotes — {character.name} ({character.vision.name})</b>\n\n" \
        "Here you can read character voice lines. <b>Avoid spoilers!</b>\n\n" \
    ))

    if add_info:
        strings.append(__(
            "<i>{emoji.INFO} Select quote using buttons below. Also, you should probably consider using inline mode.</i>"
        ))

    return "\n".join(map(str, strings)).format(
        character=character,
        emoji=emoji
    )

def button() -> str:
    return _(
        "{emoji.QUOTE} Quotes"
    ).format(
        emoji=emoji
    )

def manual_button() -> str:
    return _(
        "{emoji.MANUAL_SEARCH} Browse quotes manually (slow)"
    ).format(
        emoji=emoji
    )

def inline_button() -> str:
    return _(
        "{emoji.INLINE_SEARCH} Select quote via advanced mode"
    ).format(
        emoji=emoji
    )
