from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

import genshin
from bot import messages
from database import context

from bot import callbacks


def get_sorted_characters():
    # TODO: it is very slow block, I should probably somehow fix it.
    if context.gender.get() == "M":
        other_traveler = lambda x: str(x).startswith("lumine")
    else:
        other_traveler = lambda x: str(x).startswith("aether")
    
    result = [
        i for i in genshin.characters.values() \
        if not other_traveler(i.identifier)
    ]
    result.sort(key=lambda i: str(i.name))
    return result

def keyboard(callback: callbacks.Menu) -> types.InlineKeyboardMarkup:
    buttons = []
    sizes = [1]

    if callback.menu == "index":
        buttons = [
            types.InlineKeyboardButton(
                text=messages.menu.characters.button(),
                callback_data=callbacks.Menu(
                    menu="characters"
                ).pack()
            ),
            types.InlineKeyboardButton(
                text=messages.settings.index.button(),
                callback_data=callbacks.Settings(
                    menu="index"
                ).pack()
            ),
        ]
        sizes = [1, 1]

    if callback.menu == "characters":
        buttons = [
            types.InlineKeyboardButton(
                text=messages.menu.characters.manual_button(),
                callback_data=callbacks.Menu(
                    menu="character_view"
                ).pack()
            ),
            types.InlineKeyboardButton(
                text=messages.menu.index.inline_button(),
                switch_inline_query_current_chat=f""
            ),
            types.InlineKeyboardButton(
                text=messages.menu.index.button(),
                callback_data=callbacks.Menu(
                    menu="index"
                ).pack()
            )
        ]
        sizes = [1, 1, 1]
    
    if callback.menu == "character_view":
        characters = get_sorted_characters()
        character = characters[callback.character-1]

        buttons = [
            types.InlineKeyboardButton(
                text=messages.menu.character_view.button(character),
                callback_data=callbacks.Character(
                    identifier=character.identifier,
                    menu="index",
                ).pack()
            ),
            types.InlineKeyboardButton(
                text=messages.menu.index.button(),
                callback_data=callbacks.Menu(
                    menu="characters",
                ).pack()
            )
        ]
        if callback.character < len(characters):
            buttons.insert(
                1, types.InlineKeyboardButton(
                    text=messages.common.next_button(),
                    callback_data=callbacks.Menu(
                        menu="character_view",
                        character=callback.character+1
                    ).pack()
                )
            )
        if callback.character > 1:  # not first
            buttons.insert(
                1, types.InlineKeyboardButton(
                    text=messages.common.previous_button(),
                    callback_data=callbacks.Menu(
                        menu="character_view",
                        character=callback.character-1
                    ).pack()
                )
            )

        sizes = [1, 1, 1] if callback.character in \
            (1, len(characters)) else [1, 2, 1]

    return InlineKeyboardBuilder().add(*buttons).adjust(*sizes).as_markup()
