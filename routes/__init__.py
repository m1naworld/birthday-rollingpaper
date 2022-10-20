from flask import Flask
from . import message


app = Flask(__name__)

app.register_blueprint(message.messageBP)
