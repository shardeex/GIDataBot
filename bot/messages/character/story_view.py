from aiogram.utils.i18n import gettext as __

import genshin
from bot.messages import emoji


def title(
    character: genshin.Character,
    story: genshin.About
    ) -> str:
    return __(
        "{emoji.STORY} {story.title} — {character.name} ({character.vision.name})"
    ).format(
        character=character,
        story=story,
        emoji=emoji
    )

def description(
    story: genshin.About
    ) -> str:
    return __(
        "\"{story.text}\""
    ).format(
        story=story
    )

def text(
    character: genshin.Character,
    story: genshin.About
    ):
    strings = []

    strings.append(__(
        "<b>{emoji.STORY} {story.title} — {character.name} ({character.vision.name})</b>\n\n" \
        "{story.text}\n\n" \
        "<i>{emoji.INFO} Condition: {story.condition}</i>"
    ))

    return "\n".join(map(str, strings)).format(
        character=character,
        story=story,
        emoji=emoji
    )
