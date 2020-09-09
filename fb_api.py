import os

from flask import Flask, request
from pymessenger.bot import Bot

from enums.aggregation import Aggregation
from messages.translate import Translate

app = Flask(__name__)
bot = Bot(os.getenv('ACCESS_TOKEN'))


# TODO rebuild that mess

@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else:
        recipient_id = ''
        try:
            output = request.get_json()
            for event in output['entry']:
                messaging = event['messaging']
                for message in messaging:
                    if message.get('message'):
                        recipient_id = message['sender']['id']
                        if message['message'].get('text'):
                            print(message['message'].get('text'))
                            response_sent_text = get_message(str(message['message'].get('text')))
                            send_message(recipient_id, response_sent_text)
                        if message['message'].get('attachments'):
                             send_message(recipient_id, "response_sent_nontext")
        except:
            send_message(recipient_id, "response_sent_nontext")
    return "Message Processed"


def verify_fb_token(token_sent):
    if token_sent == os.getenv('VERIFY_TOKEN'):
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


def get_message(response):
    response_dict = Translate(response).get_translated_command()
    if response_dict['valid'] and response_dict['command']:
        try:
            answer = Aggregation().get_enum_value(enum_type=response_dict['category'],
                                                  enum_name=response_dict['command'])
        except KeyError:
            answer = "Niepoprawny typ enum"
    else:
        answer = f'Niepoprawna komenda. Regex: #typ enum dodatkowyParametr np:\n' \
                 f'#weather monday -e\n' \
                 f'{Aggregation().get_full_documentation()}'
    return answer


def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"