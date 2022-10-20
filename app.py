from flask import Flask, render_template, request, jsonify

from routes.message import messageBP
from routes.cake import cake
from routes.login import login
from routes.rollingpaper import rolling
from routes.sign_up import sign_up

app = Flask(__name__)

app.register_blueprint(login, url_prefix="/login")
app.register_blueprint(cake, url_prefix="/cake")
app.register_blueprint(messageBP, url_prefix="/message")
app.register_blueprint(rolling, url_prefix="/rolling")
app.register_blueprint(sign_up, url_prefix="/sign-up")

@app.route("/")
def hello_world():
    return "hello world!"

@app.route("/message")
def msg():
    return render_template("message.html")

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)