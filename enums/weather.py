import enum
from typing import List

from enums.enum_interface import EnumInterface
from enums.help import Help
from weather.comparator import Comparator
from weather.formatter import Formatter


class Weather(enum.Enum):

    week = 0
    monday = 1
    tuesday = 2
    wednesday = 3
    thursday = 4
    friday = 5
    saturday = 6
    sunday = 7
    today = 8


class WeatherUtils(EnumInterface):

    @classmethod
    def info(cls) -> str:
        return Help.documentation(Weather, cls.additional_parameters())

    @staticmethod
    def additional_parameters() -> List:
        return ['aaa', 'bbb']

    @staticmethod
    def get_value(enum_name):
        if enum_name == 'week':
            return Formatter().get_all_days_messages()
        else:
            return Formatter().get_single_day_message(enum_name)

