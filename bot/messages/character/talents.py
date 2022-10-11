from aiogram.utils.i18n import gettext as _, lazy_gettext as __

import genshin
from bot.messages import emoji


def title(
    character: genshin.Character
    ) -> str:
    return __(
        "{emoji.TALENT} Talents — {character.name} ({character.vision.name})"
    ).format(
        character=character,
        emoji=emoji
    )

def description(
    character: genshin.Character
    ) -> str:
    return __(
        "Tap to send talents overview.\nType \"@GIDataBot {character.identifier} talent\" for more options."
    ).format(
        character=character
    )

def text(
    character: genshin.Character,
    add_info: bool = False,
    ) -> str:
    strings = []
    
    strings.append(__(
        "<b>{emoji.TALENT} Talents \"{character.info.title}\" — " \
        "{character.name} ({character.vision.name})</b>\n"
    ))

    for talent in character.talents:
        strings.append(__(
            "{talent.type.name} — {talent.name}"
        ).format(
            talent=talent
        ))
    
    if add_info:
        strings.append(__(
            "\n<i>{emoji.INFO} Select talent using buttons below.</i>"
        ))

    return "\n".join(map(str, strings)).format(
        character=character,
        emoji=emoji
    )

def button() -> str:
    return _(
        "{emoji.TALENT} Talents"
    ).format(
        emoji=emoji
    )
