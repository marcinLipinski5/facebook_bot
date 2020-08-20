import enum
from typing import List

from enums.enum_interface import EnumInterface
from enums.help import Help


class Emoi(enum.Enum):

    hear = 0
    smile = 1


class EmoiUtils(EnumInterface):

    @classmethod
    def info(cls) -> str:
        return Help.documentation(Emoi, cls.additional_parameters())

    @staticmethod
    def additional_parameters() -> List:
        return ['ccc', 'ddd']


if __name__ == "__main__":
    print(EmoiUtils.info())
