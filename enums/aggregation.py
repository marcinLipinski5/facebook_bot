from enums.weather import WeatherUtils
from enums.emoi import EmoiUtils


class Aggregation:

    def __init__(self):
        self.documentation = []

        self.enum_dict = {'weather': WeatherUtils,
                          'emoi': EmoiUtils}

    def get_enum_instance(self, enum_name):
        return self.enum_dict[enum_name]

    def get_enum_documentation(self, enum_name):
        return self.get_enum_instance(enum_name).info()

    def get_full_documentation(self):
        enum_documentation_list = []
        for enum_name in self.enum_dict.keys():
            enum_documentation_list.append(self.get_enum_documentation(enum_name))
        return '\n--------------------\n'.join([enum_docu for enum_docu in enum_documentation_list])



if __name__ == "__main__":
    print(Aggregation().get_full_documentation())

