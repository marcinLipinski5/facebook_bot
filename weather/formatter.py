from weather.comparator import Comparator
from typing import Dict


class Formatter:

    def __init__(self):
        self.__weather_forecast_list = Comparator().get_compare_result() # Type: List

    def format_single_day_message(self, daily_forecast: Dict) -> str:
        answer = f'Forecast for {daily_forecast["day"]} {daily_forecast["time_stamp"]} ' \
                 f'{self.get_status_emoi(daily_forecast)}\n' \
                 f'Temperature range: {daily_forecast["temp_min"]} - {daily_forecast["temp_max"]}°C\n' \
                 f'Conditions: {daily_forecast["described_weather"]}\n' \
                 f'Conclusions:\n' \
                 f'{self.get_conclusions(daily_forecast)}\n'
        return answer

    def get_single_day_message(self, day_name: str) -> str:
        for daily_forecast in self.__weather_forecast_list:
            if daily_forecast['day'] == day_name:
                return self.format_single_day_message(daily_forecast)
        return f"Unable to collect data for {day_name}"

    def get_all_days_messages(self) -> str:
        answer = 'Weakly weather forecast:\n'
        for daily_forecast in self.__weather_forecast_list:
            answer += f'-----\n{self.format_single_day_message(daily_forecast)}'
        return answer

    @staticmethod
    def get_status_emoi(daily_forecast: Dict):
        if daily_forecast['status']:
            return '💖'
        else:
            return '💔'

    @staticmethod
    def get_conclusions(daily_forecast: Dict) -> str:
        if daily_forecast["conclusion"]:
            return daily_forecast["conclusion"]
        else:
            return "Perfect 🐱"
