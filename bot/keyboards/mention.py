from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot import messages


def keyboard() -> types.InlineKeyboardMarkup:

    button = types.InlineKeyboardButton(
        **messages.common.mention_button()
    )
 
    return InlineKeyboardBuilder().add(button).as_markup()
