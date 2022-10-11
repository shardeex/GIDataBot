from aiogram.utils.i18n import gettext as _, lazy_gettext as __

import genshin
from bot.messages import emoji


def title(
    constellation: genshin.Constellation
    ) -> str:
    return __(
        "C{constellation.index}: {constellation.name}"
    ).format(
        constellation=constellation,
        emoji=emoji
    )

def description(
    constellation: genshin.Constellation
    ) -> str:
    return __(
        "Tap to send constellation \"{constellation.name}\" overview."
    ).format(
        constellation=constellation
    )

def text(
    character: genshin.Character,
    constellation: genshin.Constellation
    ):
    strings = []
    
    strings.append(__(
        "<b>{emoji.CONSTELLATION} C{constellation.index} \"{constellation.name}\" — " \
        "{character.name} ({character.vision.name})</b>\n\n" \
        "{constellation.description}"
    ))

    return "\n".join(map(str, strings)).format(
        character=character,
        constellation=constellation,
        emoji=emoji
    )

def button(constellation: genshin.Constellation) -> str:
    return _(
        "C{constellation.index}"
    ).format(
        constellation=constellation
    )
