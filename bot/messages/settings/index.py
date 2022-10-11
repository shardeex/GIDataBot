from aiogram.utils.i18n import gettext as _, lazy_gettext as __

from bot.messages import emoji


def text(language: str, gender: str) -> str:
    return __(
        "<b>{emoji.SETTINGS} Settings — Main menu</b>\n\n" \
        "{emoji.LANGUAGE} Language: <b>{language}</b>\n" \
        "{emoji.GENDER} Traveler: <b>{gender}</b>\n\n" \
        "<i>{emoji.INFO} Here you can edit your settings to perform better bot using experience.</i>"
    ).format(
        language=language,
        gender=gender,
        emoji=emoji
    )

def button() -> str:
    return _(
        "{emoji.SETTINGS} Settings"
    ).format(
        emoji=emoji
    )
