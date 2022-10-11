from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot import messages


def keyboard() -> types.InlineKeyboardMarkup:
    return None  # was annoying

    button = types.InlineKeyboardButton(
        **messages.common.mention_button()
    )
 
    return InlineKeyboardBuilder().add(button).as_markup()
