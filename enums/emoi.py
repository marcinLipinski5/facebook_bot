import enum
from typing import List

from enums.enum_interface import EnumInterface
from enums.help import Help


class Emoi(enum.Enum):

    heart = 'jeszcze nie bangla'
    smile = 'to tyz nie bangla'


class EmoiUtils(EnumInterface):

    @classmethod
    def info(cls) -> str:
        return Help.documentation(Emoi, cls.additional_parameters())

    @staticmethod
    def additional_parameters() -> List:
        return ['ccc', 'ddd']

    @staticmethod
    def get_value(name):
        return Emoi[name].value


if __name__ == "__main__":
    print(EmoiUtils.info())
