class Translate:

    def __init__(self, raw_message: str):
        self.raw_message = raw_message
        self.command_beginning_char = '#'
        self.command_separator = ' '
        self.parameters_separator = '-'

    def get_translated_command(self):
        try:
            if self.does_message_contains_command():
                return self.extract_message_parts()
            raise AssertionError
        except Exception:
            return {'valid': False}

    def extract_message_parts(self):
        message_list = self.raw_message.lower().split(self.command_separator)
        try:
            additional_parameters = message_list[2].split(self.parameters_separator)
        except IndexError:
            additional_parameters = ['']

        return {'valid': True,
                'category': message_list[0].replace(self.command_beginning_char, ''),
                'command': message_list[1],
                'additional_parameters': additional_parameters}

    def does_message_contains_command(self):
        try:
            assert type(self.raw_message) == str
            assert self.raw_message[0] == "#"
            return True
        except AssertionError:
            return False



if __name__ == "__main__":
    # dupa = '[#Weather Monday e-k-j]'
    dupa = ['aa', 'aaa']
    print(Translate(dupa).get_translated_command())