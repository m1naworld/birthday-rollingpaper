from flask import Flask
from routes.homework import homework
from routes.mars import mars

from routes.message import message
from routes.login import login
from routes.signUp import signUp
from routes.rollingpaper import rolling

app = Flask(__name__)

app.register_blueprint(homework, url_prefix='/homework')
app.register_blueprint(mars, url_prefix="/mars")

app.register_blueprint(message, url_prefix="/message")
app.register_blueprint(login, url_prefix="/login")
app.register_blueprint(signUp, url_prefix="/signUp")

app.register_blueprint(rolling, url_prefix="/rolling")



@app.route("/")
def hello_world():
    return "hello world"

if __name__ == '__main__':

    app.run('0.0.0.0', port=5000, debug=True)

