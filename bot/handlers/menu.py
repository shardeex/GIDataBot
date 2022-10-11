from aiogram import Dispatcher, F, filters, types

from bot import messages, keyboards, callbacks


async def command(message: types.Message) -> None:
    await message.answer(
        messages.menu.index.text(),
        reply_markup=keyboards.menu.keyboard(
            callbacks.Menu(menu="index")
        )
    )

async def index(
    query: types.CallbackQuery,
    callback_data: callbacks.Menu
    ) -> None:
    await query.message.edit_text(
        messages.menu.index.text(),
        reply_markup=keyboards.menu.keyboard(callback_data)
    )
    await query.answer()

async def characters(
    query: types.CallbackQuery,
    callback_data: callbacks.Menu
    ) -> None:
    await query.message.edit_text(
        messages.menu.characters.text(),
        reply_markup=keyboards.menu.keyboard(callback_data)
    )
    await query.answer()

async def character_view(
    query: types.CallbackQuery,
    callback_data: callbacks.Menu
    ) -> None:
    character = keyboards.menu.get_sorted_characters()[callback_data.character-1]

    await query.message.edit_text(
        messages.menu.character_view.text(character),
        reply_markup=keyboards.menu.keyboard(callback_data)
    )
    await query.answer()

def setup(dispatcher: Dispatcher) -> None:
    dispatcher.message.register(
        command, filters.Text(text=messages.base.start.button())
    )
    dispatcher.callback_query.register(
        index, callbacks.Menu.filter(F.menu=="index")
    )
    dispatcher.callback_query.register(
        characters, callbacks.Menu.filter(F.menu=="characters")
    )
    dispatcher.callback_query.register(
        character_view, callbacks.Menu.filter(F.menu=="character_view")
    )