from aiogram.utils.i18n import gettext as _, lazy_gettext as __

import genshin
from bot.messages import emoji


def text(language: str):
    return __(
        "<b>{emoji.LANGUAGE} Settings — Language</b>\n\n" \
        "{emoji.CURRENT} Current language: <b>{language}</b>\n" \
        "{emoji.DEFAULT} Klee's description for example: <b>\"{klee.description}\"</b>\n\n"
        "<i>Here you can easily change your bot language. " \
        "Note: some languages can be translated not correctly.</i>"
    ).format(
        language=language,
        emoji=emoji,
        klee=genshin.characters["klee"]
    )

def switched(language: str):
    return __(
        "{emoji.SUCCESS} Language succesfully switched to \"{language}\"."
    ).format(
        language=language,
        emoji=emoji
    )

def same(language: str):
    return __(
        "{emoji.FAIL} You are already using \"{language}\" language!"
    ).format(
        language=language,
        emoji=emoji
    )

def button() -> str:
    return _(
        "{emoji.LANGUAGE} Language"
    ).format(
        emoji=emoji
    )

def action_button(language: str) -> str:
    return language
