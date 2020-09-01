import enum
from typing import List

from enums.enum_interface import EnumInterface
from enums.help import Help
from weather.comparator import Comparator


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
        compare_weather = Comparator()
        compare_weather.compare_all_days()
        forecast_list = compare_weather.get_compare_result()
        if enum_name == 'week':
            print(forecast_list)
            return forecast_list
        for day, daily_forecast in enumerate(forecast_list):
            if daily_forecast['day'].lower() == enum_name:
                return daily_forecast

if __name__ == "__main__":
    print(WeatherUtils.info())
