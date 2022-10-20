from flask import Flask, render_template, request, jsonify

from routes.message import messageBP


app = Flask(__name__)

app.register_blueprint(messageBP, url_prefix="/message")

@app.route("/")
def hello_world():
    return "hello world"

@app.route("/message")
def msg():
    return render_template("message.html")
#
# @message.route("/test", methods=["GET"])
# def test_fn():
#     return jsonify({'msg':'GET 연결 완료!'})

if __name__ == '__main__':
    # 초기세팅
    app.run('0.0.0.0', port=9999, debug=True)