from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram.utils.i18n import gettext as _

import genshin
from bot import messages, callbacks


def keyboard(callback: callbacks.Character) -> types.InlineKeyboardMarkup:
    character = genshin.characters.get(callback.identifier)
    buttons = []
    sizes = [1]
    
    if callback.menu == "index":
        buttons = [
            types.InlineKeyboardButton(
                text=messages.character.stats.button(),
                callback_data=callbacks.Character(
                    identifier=callback.identifier,
                    menu="stats"
                ).pack()
            ),
            types.InlineKeyboardButton(
                text=messages.character.talents.button(),
                callback_data=callbacks.Character(
                    identifier=callback.identifier,
                    menu="talents"
                ).pack()
            ),
            types.InlineKeyboardButton(
                text=messages.character.constellation.button(),
                callback_data=callbacks.Character(
                    identifier=callback.identifier,
                    menu="constellation"
                ).pack()
            ),
            types.InlineKeyboardButton(
                text=messages.character.about.button(),
                callback_data=callbacks.Character(
                    identifier=callback.identifier,
                    menu="about"
                ).pack()
            ),
            types.InlineKeyboardButton(
                text=messages.menu.index.button(),
                callback_data=callbacks.Menu(
                    menu="index"
                ).pack()
            )
        ]
        sizes = [2, 2, 1]
    
    if callback.menu == "stats":
        buttons = [
            types.InlineKeyboardButton(
                text=messages.character.index.button(),
                callback_data=callbacks.Character(
                    identifier=callback.identifier,
                    menu="index"
                ).pack()
            )
        ]
        sizes = [1]
    
    if callback.menu == "talents":
        buttons = [
            *[
                types.InlineKeyboardButton(
                    text=messages.character.talent_view.button(talent),
                    callback_data=callbacks.Character(
                        identifier=callback.identifier,
                        menu="talent_view",
                        talent=character.talents.index(talent)+1
                    ).pack()
                )
            for talent in character.talents
            ],
            types.InlineKeyboardButton(
                text=messages.character.index.button(),
                callback_data=callbacks.Character(
                    identifier=callback.identifier,
                    menu="index"
                ).pack()
            )
        ]
        sizes = [3, 3, 1]
    
    if callback.menu == "talent_view":
        buttons = [
            types.InlineKeyboardButton(
                text=messages.character.talents.button(),
                callback_data=callbacks.Character(
                    identifier=callback.identifier,
                    menu="talents",
                ).pack()
            )
        ]
        if callback.talent < len(character.talents):
            buttons.insert(
                0, types.InlineKeyboardButton(
                    text=messages.common.next_button(),
                    callback_data=callbacks.Character(
                        identifier=callback.identifier,
                        menu="talent_view",
                        talent=callback.talent+1
                    ).pack()
                )
            )
        if callback.talent > 1:  # not first
            buttons.insert(
                0, types.InlineKeyboardButton(
                    text=messages.common.previous_button(),
                    callback_data=callbacks.Character(
                        identifier=callback.identifier,
                        menu="talent_view",
                        talent=callback.talent-1
                    ).pack()
                )
            )

        sizes = [1, 1] if callback.talent in \
            (1, len(character.talents)) else [2, 1]
    
    if callback.menu == "constellation":
        buttons = [
            *[
                types.InlineKeyboardButton(
                    text=messages.character.constellation_view.button(constellation),
                    callback_data=callbacks.Character(
                        identifier=callback.identifier,
                        menu="constellation_view",
                        constellation=constellation.index
                    ).pack()
                )
            for constellation in character.constellation
            ],
            types.InlineKeyboardButton(
                text=messages.character.index.button(),
                callback_data=callbacks.Character(
                    identifier=callback.identifier,
                    menu="index"
                ).pack()
            )
        ]
        sizes = [3, 3, 1]

    if callback.menu == "constellation_view":
        buttons = [
            types.InlineKeyboardButton(
                text=messages.character.constellation.button(),
                callback_data=callbacks.Character(
                    identifier=callback.identifier,
                    menu="constellation"
                ).pack()
            )
        ]
        if callback.constellation < len(character.constellation):
            buttons.insert(
                0, types.InlineKeyboardButton(
                    text=messages.common.next_button(),
                    callback_data=callbacks.Character(
                        identifier=callback.identifier,
                        menu="constellation_view",
                        constellation=callback.constellation+1
                    ).pack()
                )
            )
        if callback.constellation > 1:  # not first
            buttons.insert(
                0, types.InlineKeyboardButton(
                    text=messages.common.previous_button(),
                    callback_data=callbacks.Character(
                        identifier=callback.identifier,
                        menu="constellation_view",
                        constellation=callback.constellation-1
                    ).pack()
                )
            )

        sizes = [1, 1] if callback.constellation in \
            (1, len(character.constellation)) else [2, 1]

    if callback.menu == "about":
        buttons = [
            types.InlineKeyboardButton(
                text=messages.character.story.button(),
                callback_data=callbacks.Character(
                    identifier=callback.identifier,
                    menu="story"
                ).pack()
            ),
            types.InlineKeyboardButton(
                text=messages.character.quotes.button(),
                callback_data=callbacks.Character(
                    identifier=callback.identifier,
                    menu="quotes"
                ).pack()
            ),
            types.InlineKeyboardButton(
                text=messages.character.index.button(),
                callback_data=callbacks.Character(
                    identifier=callback.identifier,
                    menu="index"
                ).pack()
            )
        ]
        sizes = [2, 1]

    if callback.menu == "story":
        buttons = [
            types.InlineKeyboardButton(
                text=messages.character.story.manual_button(),
                callback_data=callbacks.Character(
                    identifier=callback.identifier,
                    menu="story_view",
                    story=1
                ).pack()
            ),
            types.InlineKeyboardButton(
                text=messages.character.story.inline_button(),
                switch_inline_query_current_chat=f"{character.identifier} story"
            ),
            types.InlineKeyboardButton(
                text=messages.character.about.button(),
                callback_data=callbacks.Character(
                    identifier=callback.identifier,
                    menu="about"
                ).pack()
            )
        ]
    
    if callback.menu == "story_view":
        buttons = [
            types.InlineKeyboardButton(
                text=messages.character.story.button(),
                callback_data=callbacks.Character(
                    identifier=callback.identifier,
                    menu="story"
                ).pack()
            )
        ]
        if callback.story < len(character.story):
            buttons.insert(
                0, types.InlineKeyboardButton(
                    text=messages.common.next_button(),
                    callback_data=callbacks.Character(
                        identifier=callback.identifier,
                        menu="story_view",
                        story=callback.story+1
                    ).pack()
                )
            )
        if callback.story > 1:  # not first
            buttons.insert(
                0, types.InlineKeyboardButton(
                    text=messages.common.previous_button(),
                    callback_data=callbacks.Character(
                        identifier=callback.identifier,
                        menu="story_view",
                        story=callback.story-1
                    ).pack()
                )
            )

        sizes = [1, 1] if callback.story in \
            (1, len(character.story)) else [2, 1]
    
    if callback.menu == "quotes":
        buttons = [
            types.InlineKeyboardButton(
                text=messages.character.quotes.manual_button(),
                callback_data=callbacks.Character(
                    identifier=callback.identifier,
                    menu="quote_view",
                    quote=1
                ).pack()
            ),
            types.InlineKeyboardButton(
                text=messages.character.quotes.inline_button(),
                switch_inline_query_current_chat=f"{character.identifier} quote"
            ),
            types.InlineKeyboardButton(
                text=messages.character.about.button(),
                callback_data=callbacks.Character(
                    identifier=callback.identifier,
                    menu="about"
                ).pack()
            )
        ]

    if callback.menu == "quote_view":
        buttons = [
            types.InlineKeyboardButton(
                text=messages.character.quotes.button(),
                callback_data=callbacks.Character(
                    identifier=callback.identifier,
                    menu="quotes"
                ).pack()
            )
        ]
        if callback.quote < len(character.quotes):
            buttons.insert(
                0, types.InlineKeyboardButton(
                    text=messages.common.next_button(),
                    callback_data=callbacks.Character(
                        identifier=callback.identifier,
                        menu="quote_view",
                        quote=callback.quote+1
                    ).pack()
                )
            )
        if callback.quote > 1:  # not first
            buttons.insert(
                0, types.InlineKeyboardButton(
                    text=messages.common.previous_button(),
                    callback_data=callbacks.Character(
                        identifier=callback.identifier,
                        menu="quote_view",
                        quote=callback.quote-1
                    ).pack()
                )
            )

        sizes = [1, 1] if callback.quote in \
            (1, len(character.quotes)) else [2, 1]
    
    return InlineKeyboardBuilder().add(*buttons).adjust(*sizes).as_markup()
