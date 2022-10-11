from aiogram.utils.i18n import gettext as _, lazy_gettext as __

from bot.messages import emoji


def text(gender: str):
    return __(
        "<b>{emoji.GENDER} Settings — Gender</b>\n\n" \
        "{emoji.CURRENT} Current gender: <b>{gender}</b>\n\n" \
        "<i>{emoji.INFO} Here you can easily switch your traveler gender.</i>"
    ).format(
        gender=gender,
        emoji=emoji
    )

def switched(gender: str):
    return __(
        "{emoji.SUCCESS} Gender succesfully switched to \"{gender}\"."
    ).format(
        gender=gender,
        emoji=emoji
    )

def button() -> str:
    return _(
        "{emoji.GENDER} Gender"
    ).format(
        emoji=emoji
    )

def action_button() -> str:
    return _(
        "{emoji.GENDER} Switch gender"
    ).format(
        emoji=emoji
    )
