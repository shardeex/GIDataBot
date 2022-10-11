from aiogram import html
from aiogram.utils.i18n import gettext as _, lazy_gettext as __
from babel.support import LazyProxy


def title(name: str) -> str:
    return __(
        "{name}, tell others about this bot."
    ).format(
        name=html.quote(name)
    )

def description() -> str:
    return _(
        "Tap to send information about this bot."
    )

def text(name: str) -> str:
    return __(
        "<i>🎁 It seems that Klee left a small gift for you in the Golden Apple " \
        "Archipelago, <b>{name}</b>...</i>\n\n" \
        "📜 These are <b>Klee's Notes</b> about Teyvat! For now it's only about " \
        "characters, but stay tuned. A small gift from a little elf girl " \
        "who looks so much like her mother.\n\n" \
        "<i>🍀 Klee is still small and does not know many languages, so she " \
        "uses Google translator sometimes. She is very worried about " \
        "mistakes, so she asks her to help correct them. Thank you very much " \
        "for your understanding!</i>" 
    ).format(
        name=html.quote(name)
    )

def button() -> LazyProxy:
    return __(
        "🪟 Create new window"
    )
