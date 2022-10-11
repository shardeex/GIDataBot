from aiogram import Dispatcher, html, filters, types

from bot import messages


async def start(
    message: types.Message,
    command: filters.CommandObject
    ) -> None:
    if command.args:
        if command.args == "help":
            await help_cmd(message)
            return
        # await message.answer(f"I received start argument: <b>{command.args}</b>")

    await message.answer(
        messages.base.start.text(
            name=html.quote(message.from_user.full_name)
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

async def help_cmd(message: types.Message) -> None:
    await message.answer(messages.base.help.text())


def setup(dispatcher: Dispatcher) -> None:
    dispatcher.message.register(
        start, filters.Command(commands="start")
    )
    dispatcher.message.register(
        help_cmd, filters.Command(commands="help")
    )
