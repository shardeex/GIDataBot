from aiogram.utils.i18n import gettext as _, lazy_gettext as __

import genshin
from bot.messages import emoji


def text() -> str:
    return _(
        "<b>{emoji.CHARACTER} Characters — Klee's Notes! {emoji.DEFAULT}</b>\n\n" \
        "Here you can search information about characters.\n\n" \
        "<i>{emoji.INFO} Select character using buttons below. " \
        "Also, you should probably consider using inline mode.</i>"
    ).format(
        emoji=emoji
    )

def button() -> str:
    return _(
        "{emoji.CHARACTER} Characters"
    ).format(
        emoji=emoji
    )

def manual_button() -> str:
    return _(
        "{emoji.MANUAL_SEARCH} Browse characters manually (slow)"
    ).format(
        emoji=emoji
    )
