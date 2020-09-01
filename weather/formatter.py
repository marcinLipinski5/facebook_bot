from weather.comparator import Comparator


class Formatter:

    def __init__(self):
        self.__weather_forecast_list = Comparator().get_compare_result()

    def format_single_day_message(self, daily_forecast):
        answer = f'Forecast for {daily_forecast["day"]} {daily_forecast[""]} \n' \
                 f'Temperature range: {daily_forecast["temp_min"]} - {daily_forecast["temp_mas"]}'