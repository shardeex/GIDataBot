from aiogram.utils.i18n import lazy_gettext as __

import bot


def text() -> str:
    return __(
        # link preview
        "<a href=\"github.com/shardeex/GIDataBot\">⁠</a>" \
        "<a href=\"t.me/GIDataBot\">Klee's Notes 🍀</a> | Genshin Impact Data Bot | @GIDataBot\n\n" \
        "/settings — change your bot language and traveler gender\n" \
        "/help — show this message :D\n\n" \
        "This bot wouldn't exist if it wasn't for <a href=\"ambr.top\">Project Amber</a>. " \
        "Many thanks for the files and images provided. " \
        "Don't forget to visit the site!\n\n" \
        "<a href=\"github.com/shardeex/GIDataBot\">GitHub</a> | " \
        "<a href=\"t.me/shardeex\">Author</a> | " \
        "<a href=\"t.me/GIBotsChannel\">Channel</a> | v{version}"
    ).format(
        version=bot.__version__
    )
