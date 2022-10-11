from aiogram import Dispatcher, F, filters, types

import genshin
from bot import keyboards, messages, callbacks


async def command(
    message: types.Message,
    command: filters.CommandObject
    ) -> None:
    character = genshin.characters.get(command.command)
    callback_data = callbacks.Character(
        identifier=character.identifier,
        menu="index"
    )
    await message.answer(
        messages.character.index.text(
            character=character
        ),
        reply_markup=keyboards.character.keyboard(callback_data)
    )

async def index(
    query: types.CallbackQuery,
    callback_data: callbacks.Character
    ) -> None:
    character = genshin.characters.get(callback_data.identifier)
    await query.message.edit_text(
        messages.character.index.text(
            character=character
        ),
        reply_markup=keyboards.character.keyboard(callback_data)
    )
    await query.answer()

async def stats(
    query: types.CallbackQuery,
    callback_data: callbacks.Character
    ) -> None:
    character = genshin.characters.get(callback_data.identifier)
    await query.message.edit_text(
        messages.character.stats.text(
            character=character, add_info=True
        ),
        reply_markup=keyboards.character.keyboard(callback_data)
    )
    await query.answer()

async def talents(
    query: types.CallbackQuery,
    callback_data: callbacks.Character
    ) -> None:
    character = genshin.characters.get(callback_data.identifier)
    await query.message.edit_text(
        messages.character.talents.text(
            character=character, add_info=True
        ),
        reply_markup=keyboards.character.keyboard(callback_data)
    )
    await query.answer()

async def talent_view(
    query: types.CallbackQuery,
    callback_data: callbacks.Character
    ) -> None:
    character = genshin.characters.get(callback_data.identifier)
    talent = character.talents[callback_data.talent - 1]
       
    await query.message.edit_text(
        messages.character.talent_view.text(
            character=character,
            talent=talent,
        ),
        reply_markup=keyboards.character.keyboard(callback_data)
    )
    await query.answer()

async def constellation(
    query: types.CallbackQuery,
    callback_data: callbacks.Character
    ) -> None:
    character = genshin.characters.get(callback_data.identifier)
    await query.message.edit_text(
        messages.character.constellation.text(
            character=character, add_info=True
        ),
        reply_markup=keyboards.character.keyboard(callback_data)
    )
    await query.answer()

async def constellation_view(
    query: types.CallbackQuery,
    callback_data: callbacks.Character
    ) -> None:
    character = genshin.characters.get(callback_data.identifier)
    constellation = character.constellation[callback_data.constellation - 1]

    await query.message.edit_text(
        messages.character.constellation_view.text(
            character=character,
            constellation=constellation,
        ),
        reply_markup=keyboards.character.keyboard(callback_data)
    )
    await query.answer()

async def about(
    query: types.CallbackQuery,
    callback_data: callbacks.Character
    ) -> None:
    character = genshin.characters.get(callback_data.identifier)
    await query.message.edit_text(
        messages.character.about.text(
            character=character, add_info=True
        ),
        reply_markup=keyboards.character.keyboard(callback_data)
    )
    await query.answer()

async def story(
    query: types.CallbackQuery,
    callback_data: callbacks.Character
    ) -> None:
    character = genshin.characters.get(callback_data.identifier)
    await query.message.edit_text(
        messages.character.story.text(
            character=character, add_info=True
        ),
        reply_markup=keyboards.character.keyboard(callback_data)
    )
    await query.answer()

async def story_view(
    query: types.CallbackQuery,
    callback_data: callbacks.Character
    ) -> None:
    character = genshin.characters.get(callback_data.identifier)
    story = character.story[callback_data.story - 1]  # TODO for beta
    await query.message.edit_text(
        messages.character.story_view.text(
            character=character,
            story=story
        ),
        reply_markup=keyboards.character.keyboard(callback_data)
    )
    await query.answer()

async def quotes(
    query: types.CallbackQuery,
    callback_data: callbacks.Character
    ) -> None:
    character = genshin.characters.get(callback_data.identifier)
    await query.message.edit_text(
        messages.character.quotes.text(
            character=character, add_info=True
        ),
        reply_markup=keyboards.character.keyboard(callback_data)
    )
    await query.answer()

async def quote_view(
    query: types.CallbackQuery,
    callback_data: callbacks.Character
    ) -> None:
    character = genshin.characters.get(callback_data.identifier)
    quote = character.quotes[callback_data.quote - 1]  # TODO for beta
    await query.message.edit_text(
        messages.character.quote_view.text(
            character=character,
            quote=quote
        ),
        reply_markup=keyboards.character.keyboard(callback_data)
    )
    await query.answer()

def setup(dispatcher: Dispatcher) -> None:
    dispatcher.message.register(
        command,
        filters.Command(commands=list(genshin.characters.keys()))
    )

    dispatcher.callback_query.register(
        index,
        callbacks.Character.filter(F.menu=="index")
    )
    dispatcher.callback_query.register(
        stats,
        callbacks.Character.filter(F.menu=="stats")
    )
    dispatcher.callback_query.register(
        talents,
        callbacks.Character.filter(F.menu=="talents")
    )
    dispatcher.callback_query.register(
        talent_view,
        callbacks.Character.filter(F.menu=="talent_view")
    )
    dispatcher.callback_query.register(
        constellation,
        callbacks.Character.filter(F.menu=="constellation")
    )
    dispatcher.callback_query.register(
        constellation_view,
        callbacks.Character.filter(F.menu=="constellation_view")
    )
    dispatcher.callback_query.register(
        about,
        callbacks.Character.filter(F.menu=="about")
    )
    dispatcher.callback_query.register(
        story,
        callbacks.Character.filter(F.menu=="story")
    )
    dispatcher.callback_query.register(
        story_view,
        callbacks.Character.filter(F.menu=="story_view")
    )
    dispatcher.callback_query.register(
        quotes,
        callbacks.Character.filter(F.menu=="quotes")
    )
    dispatcher.callback_query.register(
        quote_view,
        callbacks.Character.filter(F.menu=="quote_view")
    )
