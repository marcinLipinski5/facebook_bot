import requests
import os
import json
import datetime
from typing import Dict, List


class ApiCalls:

    def __init__(self):
        self.__weather_forecast_week_list = []
        self.__get_weather_forecast()

    def __get_weather_forecast(self):
        url = f"https://api.openweathermap.org/data/2.5/onecall?" \
              f"lat=51.1000000&" \
              f"lon=17.0333300&" \
              f"exclude=hourly,minutely&" \
              f"appid={os.getenv('WEATHER_API_TOKEN')}&" \
              f"units=metric"
        answer = requests.get(url)
        for day in answer.json()['daily']:
            time_stamp = datetime.datetime.utcfromtimestamp(day['dt'])
            forecast_dict = {'time_stamp': time_stamp.strftime('%d:%m:%Y'),
                             'day': self.__get_day_name(time_stamp),
                             'temp_min': day['temp']['min'],
                             'temp_max': day['temp']['max'],
                             'main_weather': day['weather'][0]['main'],
                             'described_weather': day['weather'][0]['description']}
            self.__weather_forecast_week_list.append(forecast_dict)

    @staticmethod
    def __get_day_name(time_stamp: datetime.datetime) -> str:
        today = datetime.datetime.now()
        if today.day is time_stamp.day and today.month is time_stamp.month:
            return 'Today'
        return time_stamp.strftime('%A')

    def get_weather_forecast_list(self) -> List[Dict]:
        return self.__weather_forecast_week_list



if __name__ == "__main__":
    dupa =ApiCalls().get_weather_forecast_list()
    for kupa in dupa:
        print(kupa)