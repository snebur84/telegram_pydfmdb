import pymongo
import sys
import datetime
from pprint import pprint
from random import randint

try:
    import config
except ImportError:
    print("Erro na importacao de configuracoes")
    sys.exit(1)

def insert_data(msg):
    client = pymongo.MongoClient(config.dburl)
    db = client.chatbot_python
    msg['register'] = datetime.datetime.now()
    try:
        result = db.conversation_log.insert_one(msg)
    except ImportError:
        print("Erro no preenchimento da base")
        sys.exit(1)
    return(result)