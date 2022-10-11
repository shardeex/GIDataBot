from aiogram.utils.i18n import gettext as _, lazy_gettext as __

import genshin
from bot.messages import emoji


def text(
    character: genshin.Character
    ) -> str:
    return _(
        "<b>{character.stars} \"{character.info.title}\" {character.name} ({character.vision.name})</b>\n\n"
        "{character.description}\n\n" \
        "<i>{emoji.INFO} Select character using buttons below.</i>" \
        "<a href=\"{character.artwork_url}\">⁠</a>"
    ).format(
        character=character,
        emoji=emoji
    )

def button(character: genshin.Character) -> str:
    return _(
        "{emoji.CHARACTER} Learn more about {character.name}!"
    ).format(
        character=character,
        emoji=emoji
    )
