import random
from flask import Flask, request
from pymessenger.bot import Bot
from messages.translate import Translate
from enums.aggregation import Aggregation
import os

app = Flask(__name__)
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
VERIFY_TOKEN = os.getenv('VERIFY_TOKEN')
bot = Bot(ACCESS_TOKEN)

# TODO rebuild that mess

@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else:
       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                recipient_id = message['sender']['id']
                if message['message'].get('text'):
                    response_sent_text = get_message(str(message['message'].get('text')))
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('attachments'):
                    response_sent_nontext = get_message()
                    send_message(recipient_id, response_sent_nontext)
    return "Message Processed"


def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


def get_message(response):
    response_dict = Translate(response).get_translated_command()
    if response_dict['valid']:
        answer = Aggregation().get_enum_value(enum_type=response_dict['category'],
                                          enum_name=response_dict['command'])
    else:
        answer = f'Zjebana komenda. Regex: #typ enum dodatkowyParametr np:\n' \
                 f'#weather monday -e\n' \
                 f' Czytaj doku Mordo\n' \
                 f'{Aggregation().get_full_documentation()}'
    return answer




def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"
