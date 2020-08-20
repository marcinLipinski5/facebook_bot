from typing import List


class Help:

    @staticmethod
    def list(class_instance) -> List:
        return list(map(lambda c: c.name, class_instance))

    @classmethod
    def documentation(cls, class_instance, additional_parameters: List) -> str:
        command_list = '\n'.join(['\t#' + enum_name for enum_name in cls.list(class_instance)])
        return f'Commands for {class_instance.__name__}:\n' \
               f'{command_list}\n' \
               f'Additional parameters:\n' \
               f'{cls.get_additional_parameters(additional_parameters)}'.lower()

    @staticmethod
    def get_additional_parameters(additional_parameters_list) -> str:
        general_list = ['-e --extended : if available, display additional info for called command']
        return '\n'.join(['\t\t' + parameter for parameter in general_list + additional_parameters_list])

