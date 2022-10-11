from aiogram.utils.i18n import gettext as _, lazy_gettext as __

import genshin
from bot.messages import emoji


def title(
    talent: genshin.Talent
    ) -> str:
    return __(
        "{talent.type.name}: {talent.name}"
    ).format(
        talent=talent,
        emoji=emoji
    )

def description(
    talent: genshin.Talent
    ) -> str:
    return __(
        "Tap to send talent \"{talent.name}\" overview."
    ).format(
        talent=talent
    )

def text(
    character: genshin.Character,
    talent: genshin.Talent,
    ):
    strings = []

    strings.append(__(
        "<b>{emoji.TALENT} {talent.type.name} \"{talent.name}\" — " \
        "{character.name} ({character.vision.name})</b>\n\n" \
        "{talent.description}"
    ))

    return "\n".join(map(str, strings)).format(
        character=character,
        talent=talent,
        emoji=emoji
    )

def button(talent: genshin.Talent) -> str:
    return _(
        "{talent.type.name}"
    ).format(
        talent=talent
    )
