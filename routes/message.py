from flask import Blueprint, render_template, request, jsonify

from pymongo import MongoClient
client = MongoClient('mongodb+srv://pablaw:9dlrhd!357@cluster0.spvewgv.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# 초기 세팅
messageBP = Blueprint("message", __name__, template_folder="templates")
# messageBP = Blueprint("message", __name__, url_prefix="/message")

@messageBP.route('/')
def msg():
    return render_template("message.html")

@messageBP.route("/save_msg", methods=["GET"])
def test_fn():
    return jsonify({'msg':'GET 연결 완료!'})

@messageBP.route("/save_msg", methods=["POST"])
def msg_post():
    name_receive = request.form['name_give']
    pw_receive = request.form['pw_give']
    candle_receive = request.form['candle_give']
    msg_receive = request.form['msg_give']

    doc = {
        'name': name_receive,
        'pw': pw_receive,
        'candle': candle_receive,
        'msg': msg_receive
    }
    db.rolling.insert_one(doc)

    return jsonify({'msg':'저장 완료!'})