from genshin.models.element import *
from genshin.models.character import *


languages = ("en","zh_Hans","zh_Hant","ja","ko","id","th","vi","de","fr","pt","es","ru")

weapons = {}  # fallback

items = dict(sorted(dict.items(characters | weapons)))
