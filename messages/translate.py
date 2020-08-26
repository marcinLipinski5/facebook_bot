class Translate:

    def __init__(self, raw_message: str):
        self.message_dict = self.extract_message_parts(raw_message)
        print(self.message_dict)

    @staticmethod
    def extract_message_parts(raw_message: str):
        message_list = raw_message.lower().split(' ')
        try:
            additional_parameters = message_list[2].split('-')
        except IndexError:
            additional_parameters = ['']

        return {'category': message_list[0].replace('#', ''),
                'command': message_list[1],
                'additional_parameters': additional_parameters}


if __name__ == "__main__":
    dupa = '#Weather Monday e-k-j'
    Translate(dupa)