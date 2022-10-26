from flask import Flask, render_template

from routes.cake import cake
from routes.login import login
from routes.message import message
from routes.rollingpaper import rolling
from routes.sign_up import sign_up
from routes.mypage import mypage

from flask_jwt_extended import JWTManager
import os

app = Flask(__name__)

app.register_blueprint(login, url_prefix="/login")
app.register_blueprint(cake, url_prefix="/cake")
app.register_blueprint(message, url_prefix="/message")
app.register_blueprint(rolling, url_prefix="/rolling")
app.register_blueprint(sign_up, url_prefix="/sign-up")
app.register_blueprint(mypage, url_prefix="/mypage")

# jwt 관련
app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET')
jwt = JWTManager(app)

@app.route("/")
def hello_world():
    return "hello world!"

@app.route("/message")
def msg():
    return render_template("message.html")

if __name__ == '__main__':
    app.run('0.0.0.0', port=7777, debug=True)