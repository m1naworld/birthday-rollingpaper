from flask import Blueprint, render_template, request, jsonify

from db import db

import bcrypt

message = Blueprint("message", __name__, template_folder="templates")

@message.route('/')
def msg():
    return render_template("message.html")

@message.route("/save_msg", methods=["GET"])
def test_fn():
    return jsonify({'msg':'GET 연결 완료!'})

@message.route("/save_msg", methods=["POST"])
def msg_post():
    rolling_id = 0
    name_receive = request.form['nick_give']
    msg_receive = request.form['msg_give']
    candle_receive = request.form['candle_give']
    pw_receive = request.form['pwd_give']

    pw_receive = pw_receive.encode('utf-8')
    hashed_password = bcrypt.hashpw(pw_receive, bcrypt.gensalt())
    pw_receive = hashed_password.decode('utf-8')

    doc = {
        'rolling_id' : int(rolling_id)+1,
        'nickname': name_receive,
        'message_password': pw_receive,
        'content': msg_receive,
        'candle_id': candle_receive
    }
    db.message.insert_one(doc)

    return jsonify({'msg':'저장 완료!'})


