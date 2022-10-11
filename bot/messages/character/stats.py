from aiogram.utils.i18n import gettext as _, lazy_gettext as __

import genshin
from bot.messages import emoji


def title(
    character: genshin.Character
    ) -> str:
    return __(
        "{emoji.STATS} Stats — {character.name} ({character.vision.name})"
    ).format(
        character=character,
        emoji=emoji
    )

def description() -> str:
    return _(
        "Tap to send character stats."
    )

def text(
    character: genshin.Character,
    add_info: bool = False,
    ) -> str:
    strings = []

    strings.append(__(
        "<b>{emoji.STATS} Stats — {character.name} ({character.vision.name})</b>\n\n" \
        "<b>{emoji.HP} {character.stats.max.hp.type.name}:</b> {character.stats.max.hp.value:.0f}\n" \
        "<b>{emoji.ATTACK} {character.stats.max.attack.type.name}:</b> {character.stats.max.attack.value:.0f}\n" \
        "<b>{emoji.DEFENSE} {character.stats.max.defense.type.name}:</b> {character.stats.max.defense.value:.0f}"
    ))

    if character.stats.max.secondary.type.identifier == "elemental_mastery":
        strings.append(__(
            "<b>{emoji.SECONDARY_STAT} {character.stats.max.secondary.type.name}:</b> {character.stats.max.secondary.value:.0f}"
        ))
    else:
        strings.append(__(
            "<b>{emoji.SECONDARY_STAT} {character.stats.max.secondary.type.name}:</b> {character.stats.max.secondary.value:.1%}"
        ))

    if add_info:
        strings.append(__(
            "\n<i>{emoji.INFO} Shown character stats for level 90. More levels coming soon!</i>"
        ))

    return "\n".join(map(str, strings)).format(
        character=character,
        emoji=emoji
    )

def button() -> str:
    return _(
        "{emoji.STATS} Stats"
    ).format(
        emoji=emoji
    )
