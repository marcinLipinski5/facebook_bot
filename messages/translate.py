from typing import Dict


class Translate:

    def __init__(self, raw_message: str):
        self.raw_message = raw_message
        self.command_beginning_char = '#'
        self.command_separator = ' '
        self.parameters_separator = '-'
        self.command_dict = {'valid': False,
                             'category': '',
                             'command': '',
                             'additional_parameters': []}

    def get_translated_command(self) -> Dict:
        try:
            if self.does_message_contains_command():
                return self.extract_message_parts()
            raise AssertionError
        except Exception:
            return self.command_dict

    def extract_message_parts(self) -> Dict:
        message_list = self.raw_message.lower().replace(self.command_beginning_char, '').split(self.command_separator)
        if '' in message_list: message_list.remove('')

        self.command_dict['category'] = message_list[0]
        try:
            self.command_dict['command'] = message_list[1]
        except IndexError:
            pass
        try:
            self.command_dict['additional_parameters'] = message_list[2].split(self.parameters_separator)
        except IndexError:
            pass
        self.command_dict['valid'] = True
        return self.command_dict

    def does_message_contains_command(self) -> bool:
        try:
            assert type(self.raw_message) == str
            assert self.raw_message[0] == "#"
            return True
        except AssertionError:
            return False



if __name__ == "__main__":
    # dupa = '#Weather Monday e-k-j'
    # dupa = ['aa', 'aaa']
    dupa = '#help dsda dfsfsdf a-s-d asdas'
    print(Translate(dupa).get_translated_command())