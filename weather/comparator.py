from weather.api_calls import ApiCalls
from typing import Dict


class Comparator:

    def __init__(self):
        # TODO optimize this
        self.__weather_forecast_list = ApiCalls().get_weather_forecast_list()
        self.__person_requirements = {"Kasia":
                                          {'temp_min': 25,
                                           'temp_max': 1000000,
                                           'main_weather': ['Clear']},
                                      "Marcin":
                                          {'temp_min': -1000000,
                                           'temp_max': 28,
                                           'main_weather': []}
                                      }
        self.__positive_result = True
        self.__compare_answer = ''

    def compare_temp_min(self, day_forecast: Dict):
        if self.__person_requirements['Kasia']['temp_min'] >= day_forecast['temp_min']:
            self.__compare_answer += f'Too cold for Kasia\n'
            self.__positive_result = False
        elif self.__person_requirements['Marcin']['temp_min'] >= day_forecast['temp_min']:
            self.__compare_answer += f'Too cold for Marcin\n'
            self.__positive_result = False

    def compare_temp_max(self, day_forecast: Dict):
        if self.__person_requirements['Kasia']['temp_max'] <= day_forecast['temp_max']:
            self.__compare_answer += f'Too hot for Kasia\n'
            self.__positive_result = False
        elif self.__person_requirements['Marcin']['temp_max'] <= day_forecast['temp_max']:
            self.__compare_answer += f'Too hot for Marcin\n'
            self.__positive_result = False

    def compare_weather_status(self, day_forecast: Dict):
        for weather_condition in self.__person_requirements['Kasia']['main_weather']:
            if day_forecast['main_weather'] not in weather_condition:
                self.__compare_answer += f'Weather condition {day_forecast["main_weather"]} is not suitable for Kasia'
                self.__positive_result = False
        for weather_condition in self.__person_requirements['Marcin']['main_weather']:
            if day_forecast['main_weather'] not in weather_condition:
                self.__compare_answer += f'Weather condition {day_forecast["main_weather"]} is not suitable for Marcin'
                self.__positive_result = False

    def compare_all_days(self):
        for day, daily_forecast in enumerate(self.__weather_forecast_list):
            self.compare_temp_max(daily_forecast)
            self.compare_temp_min(daily_forecast)
            self.compare_weather_status(daily_forecast)
            self.__weather_forecast_list[day]['status'] = str(self.__positive_result)
            self.__weather_forecast_list[day]['conclusion'] = self.__compare_answer
            self.__positive_result = True
            self.__compare_answer = ''
        print(self.__weather_forecast_list)

    def get_compare_result(self):
        return self.__weather_forecast_list

if __name__ == "__main__":
    Comparator().compare_all_days()