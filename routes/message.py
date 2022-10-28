from flask import Blueprint, render_template, request, jsonify

from db import db

import bcrypt

message = Blueprint("message", __name__, template_folder="templates")

@message.route('/detail-data/<rolling_id>')
def send_msg(rolling_id):
    return render_template("message.html")

# @message.route("/save_msg", methods=["GET"])
# def test_fn():
#     return jsonify({'msg':'GET 연결 완료!'})

@message.route("/save_msg", methods=["POST"])
def msg_post():
    name_receive = request.form['nick_give']
    msg_receive = request.form['msg_give']
    candle_receive = request.form['candle_give']
    pw_receive = request.form['pwd_give']
    rolling_id = request.form['rolling_give']
    print(rolling_id);
    data = db.message.find_one({'title': '초기값'})
    count = data['count']

    message_id = int(count) + 1

    rolling_id = int(rolling_id)
    print(type(rolling_id))
    db.message.update_one({'count': int(count)}, {'$set': {'count': message_id}})

    pw_receive = pw_receive.encode('utf-8')
    hashed_password = bcrypt.hashpw(pw_receive, bcrypt.gensalt())
    pw_receive = hashed_password.decode('utf-8')

    doc = {
        'rolling_id': rolling_id,
        'message_id' : message_id,
        'nickname': name_receive,
        'message_password': pw_receive,
        'content': msg_receive,
        'candle_id': candle_receive
    }
    db.message.insert_one(doc)


    return jsonify({'msg':'저장 완료!'})


