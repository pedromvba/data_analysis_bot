''' 
1. The src (source) folder is destined for source code
 
2. The .env is a place for you to declare environment variables so people won't see it on git, for example the bot API 

3. .gitignore lists the files that git should ignore when uploading the code, .env is there

4. Python-dotenv reads key-value pairs from a .env file and can set them as environment variables. It helps in the development of applications following the 12-factor principles.


5. Difference betweeen Json and Dictionary

Json:

b'{"ok":true,"result":[{"update_id":126772868,\n"message":{"message_id":1,"from":{"id":1550893356,"is_bot":false,"first_name":"Pedro","last_name":"Azevedo","language_code":"pt-br"},"chat":{"id":1550893356,"first_name":"Pedro","last_name":"Azevedo","type":"private"},"date":1657069160,"text":"/start","entities":[{"offset":0,"length":6,"type":"bot_command"}]}},{"update_id":126772869,\n"message":{"message_id":2,"from":{"id":1550893356,"is_bot":false,"first_name":"Pedro","last_name":"Azevedo","language_code":"pt-br"},"chat":{"id":1550893356,"first_name":"Pedro","last_name":"Azevedo","type":"private"},"date":1657124225,"text":"oi"}}]}'

Dictionary: 

{'ok': True, 'result': [{'update_id': 126772868, 'message': {'message_id': 1, 'from': {'id': 1550893356, 'is_bot': False, 'first_name': 'Pedro', 'last_name': 'Azevedo', 'language_code': 'pt-br'}, 'chat': {'id': 1550893356, 'first_name': 'Pedro', 'last_name': 'Azevedo', 'type': 'private'}, 'date': 1657069160, 'text': '/start', 'entities': [{'offset': 0, 'length': 6, 'type': 'bot_command'}]}}, {'update_id': 126772869, 'message': {'message_id': 2, 'from': {'id': 1550893356, 'is_bot': False, 'first_name': 'Pedro', 'last_name': 'Azevedo', 'language_code': 'pt-br'}, 'chat': {'id': 1550893356, 'first_name': 'Pedro', 'last_name': 'Azevedo', 'type': 'private'}, 'date': 1657124225, 'text': 'oi'}}]}

'''

'''
Importing secret/secure variables from .env file
'''
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()       # take environment variables from .env.
                    # Code of your application, which uses environment variables (e.g. from `os.environ` or
                    # `os.getenv`) as if they came from the actual environment.
                    # This is really useful for logins, passwords etc.
                    # TOKEN = os.getenv('API_KEY')

'''
Creating the Bot
'''

class TelegramBot:    
    def __init__(self): # initial configuration/attributes
       TOKEN = os.getenv('API_KEY')
       self.url = f'https://api.telegram.org/bot{TOKEN}/'   

                    # Making requests : All queries to the Telegram Bot API must be served over HTTPS and need to be presented in this form: https://api.telegram.org/bot<token>/METHOD_NAME. Like this for example:https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMe'''

    
    def start(self): # start the bot and keeps it looking for message
        update_id = None
        while True:
            update = (self.get_message(update_id)) # sets update value as the message itself
            messages = update['result']
            if messages: # if bot receives a message
                for message in messages:
                    try:
                        update_id = message['update_id'] # id of the message itself
                        chat_id = message['message']['from']['id'] #id of whom send the message
                        message_text = message['message']['text']
                        answer_bot = self.create_answer(message_text)
                        self.send_answer(chat_id, answer_bot)
                    except:
                        pass # if the message presents any error, it will ignore it and move on to the next

         
    def get_message(self, update_id): # looks for message
        link_request = f'{self.url}getUpdates?timeout=1000'  
                                                            # The ? flag is used in URLs to separate   the  'route' from the parameters, such as https://   www.google.com/search?q=stack
        if update_id:
            link_request = f'{self.url}getUpdates?timeout=1000&offset={update_id + 1}'
        result = requests.get(link_request)
        return json.loads(result.content)  #json.loads: transforms the json type into a dictionary; result comes in a json format.

    def create_answer(self, message_text): # creates the text to be sent
        
        if message_text in ['oi','olá']:
            return  'Ola Tudo Bem'
        else:
            return 'Não Entendi...'
    
    def send_answer(self, chat_id, answer):
        link_to_send = f'{self.url}sendMessage?chat_id={chat_id}&text={answer}'
        requests.get(link_to_send)
        return 


