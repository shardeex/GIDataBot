from ..i18n import I18n


class GenshinItem:
    '''
    Base class for in-game objects, like characters, weapons, etc.

    Attributes:
    -----------
        - identifier `str`: unique object id
        - name `genshin.I18n`: translatable object name
        - description `genshin.I18n`: translatable object description
        - rarity `int`: object rarity
        - stars `str`: object stars (equals rarity)
    
    Returns: identifier
    '''
    __star_symbol = "★"

    def __init__(self, data: dict) -> None:
        '''_summary_

        Args:
            data (dict): _description_
        '''
        self.identifier = data["identifier"]
        self.name = I18n(data["name"])
        self.description = I18n(data["description"])
        self.rarity = data["rarity"]

    @property
    def stars(self) -> str:
        return self.__star_symbol * self.rarity
    
    def __repr__(self):
        return self.identifier
