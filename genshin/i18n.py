import re

from database import context


class I18n:
    __default = "en"

    def __init__(self, data: dict[str, str]) -> None:
        self.__data = data

    def __repr__(self) -> str:
        string = self.__data.get(context.language.get(), "")
        if string == "":  # not found translation or unknown locale
            string = self.__data[self.__default]  # en is always presented

        if string.startswith("#"):
            string = re.sub(r"\{nickname\}", context.nickname.get(), string)

            gender = context.gender.get()
            string = re.sub(fr"\{{{gender}#(.*?)\}}", r"\1", string)

            sibling_gender = "F" if gender == "M" else "M"
            string = re.sub(fr"\{{{sibling_gender}#(.*?)\}}", "", string)

            string = string[1:]  # remove "#"

        return string
