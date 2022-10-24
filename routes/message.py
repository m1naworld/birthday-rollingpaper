from flask import Blueprint, render_template, request, jsonify

from db import db

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
    name_receive = request.form['nick_give']
    pw_receive = request.form['pwd_give']
    msg_receive = request.form['msg_give']
    candle_receive = request.form['candle_give']


    doc = {
        'nickname': name_receive,
        'message_password': pw_receive,
        'content': msg_receive,
        'candle_id': candle_receive
    }
    db.message.insert_one(doc)

    return jsonify({'msg':'저장 완료!'})



