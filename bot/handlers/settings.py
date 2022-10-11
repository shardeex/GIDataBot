from aiogram import Dispatcher, F, filters, types
from aiogram.utils.i18n import gettext as _, I18n

from database import save_user, context
from bot import keyboards, messages, callbacks


get_gender_sign = lambda x: {"M": "♂️", "F": "♀️"}.get(x, "⚧")

async def command(message: types.Message) -> None:
    await message.answer(
        messages.settings.index.text(
            language=context.language.get(),
            gender=get_gender_sign(context.gender.get())
        ),
        reply_markup=keyboards.settings.keyboard(
            callbacks.Settings(menu="index")
        )
    )

async def index(
    query: types.CallbackQuery,
    callback_data: callbacks.Settings
    ) -> None:
    await query.message.edit_text(
        messages.settings.index.text(
            language=context.language.get(),
            gender=get_gender_sign(context.gender.get())
        ),
        reply_markup=keyboards.settings.keyboard(callback_data)
    )
    await query.answer()

async def language(
    query: types.CallbackQuery,
    callback_data: callbacks.Settings
    ) -> None:
    await query.message.edit_text(
        messages.settings.language.text(
            language=context.language.get()
        ),
        reply_markup=keyboards.settings.keyboard(callback_data)
    )
    await query.answer()

async def language_switch(
    query: types.CallbackQuery,
    callback_data: callbacks.Settings,
    i18n: I18n
    ) -> None:
    old_language = context.language.get()
    new_language = callback_data.language

    if old_language == new_language:
        await query.answer(
            messages.settings.language.same(
                language=old_language
            ),
            show_alert=True
        )
        return

    context.language.set(callback_data.language)
    await save_user(query.from_user.id)
    i18n.current_locale = callback_data.language

    await query.message.answer(
        "Changing language to {language}...".format(  # probably shouldn't be translated
            language=new_language
        ),
        reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[
                [
                    types.KeyboardButton(
                        text=str(messages.base.start.button())
                    )
                ]
            ],
            resize_keyboard=True
        )
    )
    await query.message.edit_text(
        messages.settings.language.text(
            language=context.language.get()
        ),
        reply_markup=keyboards.settings.keyboard(callback_data)
    )
    await query.answer(
        messages.settings.language.switched(
            language=new_language
        ),
        show_alert=True
    )

async def gender(
    query: types.CallbackQuery,
    callback_data: callbacks.Settings
    ) -> None:
    await query.message.edit_text(
        messages.settings.gender.text(
            gender=get_gender_sign(context.gender.get())
        ),
        reply_markup=keyboards.settings.keyboard(callback_data)
    )
    await query.answer()

async def gender_switch(
    query: types.CallbackQuery,
    callback_data: callbacks.Settings
    ) -> None:
    old_gender = context.gender.get()
    new_gender = "F" if old_gender == "M" else "M"
    context.gender.set(new_gender)
    await save_user(query.from_user.id)

    await query.message.edit_text(
        messages.settings.gender.text(
            gender=get_gender_sign(context.gender.get())
        ),
        reply_markup=keyboards.settings.keyboard(callback_data)
    )
    await query.answer(
        messages.settings.gender.switched(
            gender=new_gender
        ), show_alert=True
    )


def setup(dispatcher: Dispatcher) -> None:
    dispatcher.message.register(
        command, filters.Command(commands="settings")
    )

    dispatcher.callback_query.register(
        index, callbacks.Settings.filter(F.menu=="index")
    )
    dispatcher.callback_query.register(
        language, callbacks.Settings.filter(F.menu=="language")
    )
    dispatcher.callback_query.register(
        language_switch,
        callbacks.Settings.filter(F.menu=="language_switch")
    )
    dispatcher.callback_query.register(
        gender, callbacks.Settings.filter(F.menu=="gender")
    )
    dispatcher.callback_query.register(
        gender_switch,
        callbacks.Settings.filter(F.menu=="gender_switch")
    )
