### Desenvolvido por Rubens Lemos em julho de 2020
### Tech Challenge - Digital Innovation One - Banco Carrefour
from telebot import TeleBot
import json
import sys

try:
    import config
except ImportError:
    print("Erro na importacao de configuracoes")
    sys.exit(1)

try:
    import diaflow
except ImportError:
    print("Erro na importacao do modulo DialogFlow")
    sys.exit(2)

with open('credentials.json', 'r') as json_file:
    credentials = json.load(json_file)

try:
    import mongodb
except ImportError:
    print("Erro na importacao do modulo MongoDB")
    sys.exit(3)

app = TeleBot(__name__)

@app.route('(?!/).+')
def parrot(message):
    user_msg = message['text']
    user_name = message['chat']['first_name']
    session_id = message['chat']['id']
    msg = {
        'customer': {
            'user_name': user_name,
            'chat_id': session_id,
            'user_msg': user_msg
        }
            
    }
    msg['bot'] = diaflow.send_text_dialog(credentials['project_id'], session_id, user_msg, config.lang, credentials['private_key'])
    app.send_message(session_id, msg['bot']['text'])
    result = mongodb.insert_data(msg)
    print(result)  #printar no terminal o resultado da inserção no banco de dados - apenas didático

if __name__ == "__main__":
    app.config['api_key'] = config.api_key_telegram
    app.poll(debug=True)
