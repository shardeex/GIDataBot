from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

import genshin
from bot import messages, callbacks


def keyboard(callback: callbacks.Settings) -> types.InlineKeyboardMarkup:
    buttons = []
    sizes = [1]

    if callback.menu == "index":
        buttons = [
            types.InlineKeyboardButton(
                text=messages.settings.language.button(),
                callback_data=callbacks.Settings(
                    menu="language"
                ).pack()
            ),
            types.InlineKeyboardButton(
                text=messages.settings.gender.button(),
                callback_data=callbacks.Settings(
                    menu="gender"
                ).pack()
            ),
            types.InlineKeyboardButton(
                text=messages.menu.index.button(),
                callback_data=callbacks.Menu(
                    menu="index"
                ).pack()
            ),
        ]
        sizes = [2, 1]
    
    if callback.menu in ("language", "language_switch"):
        buttons = [
            *[
                types.InlineKeyboardButton(
                    text=messages.settings.language.action_button(
                        language
                    ),
                    callback_data=callbacks.Settings(
                        menu="language_switch",
                        language=language
                    ).pack()
                ) for language in genshin.languages
            ],
            types.InlineKeyboardButton(
                text=messages.settings.index.button(),
                callback_data=callbacks.Settings(
                    menu="index"
                ).pack()
            )
        ]
        sizes = [5, 8, 1]

    if callback.menu in ("gender", "gender_switch"):
        buttons = [
            types.InlineKeyboardButton(
                text=messages.settings.gender.action_button(),
                callback_data=callbacks.Settings(
                    menu="gender_switch"
                ).pack()
            ),
            types.InlineKeyboardButton(
                text=messages.settings.index.button(),
                callback_data=callbacks.Settings(
                    menu="index"
                ).pack()
            )
        ]
        sizes = [1, 1]

    return InlineKeyboardBuilder().add(*buttons).adjust(*sizes).as_markup()
