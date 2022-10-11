from aiogram.utils.i18n import gettext as _, lazy_gettext as __

import genshin
from bot.messages import emoji


def title(
    character: genshin.Character
    ) -> str:
    return __(
        "{character.name} ({character.vision.name})"
    ).format(
        character=character
    )

def description() -> str:
    return _(
        "Tap to send character profile."
    )

def text(
    character: genshin.Character,
    ) -> str:
    strings = []
    
    strings.append(__(
        "<b>{character.stars} \"{character.info.title}\" {character.name} ({character.vision.name})</b>\n\n" \
        "<b>{emoji.VISION} Vision:</b> {character.vision.name}\n" \
        "<b>{emoji.WEAPON} Weapon:</b> {character.weapon_type.name}\n" \
        "<b>{emoji.CONSTELLATION} Constellation:</b> {character.info.constellation}\n" \
        "<b>{emoji.AFFILATION} Affilation:</b> {character.info.affilation}" \
    ))

    if character.info.birthday.days_left is None:
        strings.append(__(
            "<b>{emoji.BIRTHDAY} Birthday:</b> set by the player.\n" \
        ))
    else:
        strings.append(__(
            "<b>{emoji.BIRTHDAY} Birthday:</b> {character.info.birthday} " \
            "({character.info.birthday.days_left} days left)\n" \
        ))

    strings.append(__(
        "<i>{emoji.INFO} {character.description}</i><a href=\"{character.artwork_url}\">⁠</a>"
    ))

    return "\n".join(map(str, strings)).format(
        character=character,
        emoji=emoji
    )

def button() -> str:
    return _(
        "{emoji.CHARACTER} Character"
    ).format(
        emoji=emoji
    )
