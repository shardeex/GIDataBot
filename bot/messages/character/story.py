from aiogram.utils.i18n import gettext as _, lazy_gettext as __

import genshin
from bot.messages import emoji


def title(
    character: genshin.Character
    ) -> str:
    return __(
        "{emoji.STORY} Story — {character.name} ({character.vision.name})"
    ).format(
        character=character,
        emoji=emoji
    )

def description(
    character: genshin.Character
    ) -> str:
    return __(
        "Tap to send story overview.\nType \"@GIDataBot {character.identifier} story\" for more options."
    ).format(
        character=character
    )

def text(
    character: genshin.Character,
    add_info: bool = False
    ):
    strings = []

    strings.append(__(
        "<b>{emoji.STORY} Story — {character.name} ({character.vision.name})</b>\n\n" \
        "Here you can read character story lines. <b>Avoid spoilers!</b>" \
    ))

    if add_info:
        strings.append(__(
            "<i>\n{emoji.INFO} Select story using buttons below. Also, you should probably consider using inline mode.</i>"
        ))

    return "\n".join(map(str, strings)).format(
        character=character,
        emoji=emoji
    )

def button() -> str:
    return _(
        "{emoji.STORY} Story"
    ).format(
        emoji=emoji
    )

def manual_button() -> str:
    return _(
        "{emoji.MANUAL_SEARCH} Browse story manually (slow)"
    ).format(
        emoji=emoji
    )

def inline_button() -> str:
    return _(
        "{emoji.INLINE_SEARCH} Select story via advanced mode"
    ).format(
        emoji=emoji
    )
