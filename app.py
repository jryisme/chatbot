from flask import Flask
from flask import request

from chatterbot import ChatBot

bot = ChatBot(
    'Norman',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

app = Flask(__name__)


@app.route('/ask', methods=['POST'])
def ask():
    content = request.json

    print("Ask: ", content.get("content"))

    answer = bot.get_response(content.get("content"))

    print("Answer: ", answer)

    return str(answer)
