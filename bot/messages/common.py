import random

from aiogram.utils.i18n import gettext as _, lazy_gettext as __

from database import context
from bot.messages import emoji


def mention_button() -> dict:
    choices = [
        {"url": "t.me/GIDataBot", "text": _(
            "Your best Teyvat guide, not emergency food."
        )},
        {"url": "t.me/GIDataBot", "text": _(
            "Don't forget to check out other characters!"
        )},
        {"url": "t.me/GIDataBot", "text": _(
            "Random ad string #3"
        )},
        {"url": "t.me/GIDataBot", "text": _(
            "Just click it, please."
        )},
        {"url": "t.me/GIBotsChannel", "text": _(
            "Check out updates and other bots! And subscribe, please."
        )},
        {"url": "t.me/GIWishBot", "text": _(
            "Check out my Wish Simulator! Outdated, but still nice."
        )}
    ]
    if context.language.get() in ("ru", "en"):  # Only for russian and non-switched users
        choices.extend([
            {"url": "t.me/shardeexGI", "text": _(
                "[RU] Personal author Genshin Impact channel!"
            )},
            {"url": "t.me/sh4rdeex", "text": _(
                "[RU] Personal author channel!"
            )},
            {"url": "t.me/KleeDonate", "text": _(
                "[RU] Get your Blessing of the Welkin Moon for pleasant price."
            )},
            {"url": "t.me/KleeDonate", "text": _(
                "[RU] Get your BP: Gnostic Hymn only for pleasant price!"
            )}
        ])
    return random.choice(choices)

def next_button() -> str:
    return _(
        "{emoji.NEXT} Next"
    ).format(
        emoji=emoji
    )

def previous_button() -> str:
    return _(
        "{emoji.PREVIOUS} Previous"
    ).format(
        emoji=emoji
    )

def inline_help() -> str:
    return _(
        "Help, how do I use this bot?"
    )

def inline_default_description(identifier: str) -> str:
    return __(
        "Type \"@GIDataBot {identifier}\" for more options"
    ).format(
        identifier=identifier
    )
