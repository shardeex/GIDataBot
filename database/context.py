from contextvars import ContextVar
from typing import Literal


nickname: ContextVar[str] = ContextVar("nickname")

# # Python 3.11
# from genshin import languages
# language: ContextVar[Literal[*languages]] = ContextVar()
language: ContextVar[str] = ContextVar("language")

gender: ContextVar[Literal["M", "F"]] = ContextVar("gender")

__all__ = [
    "nickname",
    "language",
    "gender"
]
