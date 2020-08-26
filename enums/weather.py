import enum
from typing import List

from enums.enum_interface import EnumInterface
from enums.help import Help


class Weather(enum.Enum):

    week = 0
    monday = 1
    tuesday = 2
    wednesday = 3
    thursday = 4
    friday = 5
    saturday = 6
    sunday = 7


class WeatherUtils(EnumInterface):

    @classmethod
    def info(cls) -> str:
        return Help.documentation(Weather, cls.additional_parameters())

    @staticmethod
    def additional_parameters() -> List:
        return ['aaa', 'bbb']

    @staticmethod
    def get_value(name):
        return Weather[name].value

if __name__ == "__main__":
    print(WeatherUtils.info())
