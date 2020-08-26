from enums.weather import WeatherUtils
from enums.emoi import EmoiUtils


class Aggregation:

    def __init__(self):
        self.documentation = []

        self.enum_dict = {'weather': WeatherUtils,
                          'emoi': EmoiUtils}

    def get_enum_value(self, enum_type, enum_name):
        enum_instance = self.get_enum_instance(enum_type)
        return enum_instance.get_value(enum_name)

    def get_enum_instance(self, enum_type):
        return self.enum_dict[enum_type]

    def get_enum_documentation(self, enum_type):
        return self.get_enum_instance(enum_type).info()

    def get_full_documentation(self):
        enum_documentation_list = []
        for enum_type in self.enum_dict.keys():
            enum_documentation_list.append(self.get_enum_documentation(enum_type))
        return '\n--------------------\n'.join([enum_docu for enum_docu in enum_documentation_list])



if __name__ == "__main__":
    print(Aggregation().get_enum_value('weather', 'week'))

