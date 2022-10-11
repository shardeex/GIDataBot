from typing import *

from aiogram import Dispatcher, types
from aiogram.utils.i18n import I18n, SimpleI18nMiddleware

from database import load_user, context

try:
    from babel import Locale, UnknownLocaleError
except ImportError:  # pragma: no cover
    Locale = None

    class UnknownLocaleError(Exception):  # type: ignore
        pass


class FixedI18nMiddleware(SimpleI18nMiddleware):
    # quick fix for users in group chats, who hasn't write to bot's dm
    async def get_locale(
        self, event: types.TelegramObject, data: dict[str, Any]) -> str:
        event_from_user: Optional[types.User] = data.get(
            "event_from_user", None)
        if event_from_user is None:
            return self.i18n.default_locale

        _ = await load_user(event_from_user.id)
        return context.language.get()

def setup(dp: Dispatcher, i18n: I18n):
    FixedI18nMiddleware(i18n).setup(dp)
