from flask import Blueprint, render_template, request, jsonify
from db import db
import bcrypt
from flask_jwt_extended import (get_jwt_identity, jwt_required)

cake = Blueprint("cake", __name__, template_folder="templates")

@cake.route('/')
def question():
    return render_template("cake.html")

@cake.route("/makecake", methods=["POST"])
@jwt_required()
def sel_cake():
    print('?')
    user_id = get_jwt_identity()
    print(user_id)
    cake_receive = request.form['cake_id']
    nickname_receive = request.form['user_nickname']
    birth_receive = request.form['birth']

    all_cake = list(db.rollingpaper.find({}, {'_id': False}))
    last_cake_num = all_cake.pop()['rolling_id']

    rolling_id = str(int(last_cake_num) + 1)

    print(cake_receive, nickname_receive, birth_receive, rolling_id, user_id)
    # 세션에서 현재 유저 받아오기
    # user_id = request.form['temp_user']

    url = str(bcrypt.hashpw(rolling_id.encode('utf-8'), bcrypt.gensalt()), 'utf-8')
    # print(bcrypt.hashpw(rolling_id.encode('utf-8'), bcrypt.gensalt()))
    print(url)
    doc = {'rolling_id': rolling_id, 'birth': birth_receive, 'user_nickname': nickname_receive,
           'user_id': user_id, 'cake_id': cake_receive, 'url': url}
    db.rollingpaper.insert_one(doc)

    return jsonify({'msg': '케이크가 만들어졌어요!', 'user_id': user_id})
#



# rolling_id = '1234';
# print(bcrypt.hashpw(rolling_id.encode('utf-8'), bcrypt.gensalt()))
#
# bytes = bcrypt.hashpw(rolling_id.encode('utf-8'), bcrypt.gensalt())
# result = str(bytes, 'utf-8')
# print(result)