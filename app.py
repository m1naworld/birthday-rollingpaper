from flask import Flask
from routes.homework import homework
from routes.mars import mars
from routes.cake import cake
app = Flask(__name__)

app.register_blueprint(homework, url_prefix='/homework')
app.register_blueprint(mars, url_prefix="/mars")
app.register_blueprint(cake, url_prefix="/cake")

@app.route("/")
def hello_world():
    return "hello world"


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)