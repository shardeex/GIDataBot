from aiogram.utils.i18n import gettext as _, lazy_gettext as __

from bot.messages import emoji


def text() -> str:
    return _(
        "<b>{emoji.MENU} Menu — Klee's Notes! {emoji.DEFAULT}</b>\n\n" \
        "{emoji.MANUAL_SEARCH} Search anything about characters. Weapons and more coming soon.\n\n" \
        "<i>{emoji.INFO} Use buttons below.</i>"
    ).format(
        emoji=emoji
    )

def button() -> str:
    return _(
        "{emoji.MENU} Menu"
    ).format(
        emoji=emoji
    )

def inline_button() -> str:
    # search characters and any Genshin item soon...
    return _(
        "{emoji.INLINE_SEARCH} Select characters via inline mode"
    ).format(
        emoji=emoji
    )