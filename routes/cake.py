from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from db import db
import bcrypt

cake = Blueprint("cake", __name__, template_folder="templates")

@cake.route('/')
def question():
    return render_template("cake.html")

@cake.route("/cake", methods=["POST"])
def sel_cake():

    user_id = get_jwt_identity()
    # 세션에서 현재 유저 받아오기

    cake_receive = request.form['cake_id']
    nickname_receive = request.form['user_nickname']
    birth_receive = request.form['birth']

    all_cake = list(db.rollingpaper.find({}, {'_id': False}))
    last_cake_num = all_cake.pop()['rolling_id']

    rolling_id = str(int(last_cake_num) + 1)

    rolling_int = int(rolling_id)


    url = str(bcrypt.hashpw(rolling_id.encode('utf-8'), bcrypt.gensalt()), 'utf-8')

    print(cake_receive, nickname_receive, birth_receive, rolling_id, user_id, url)
    doc = {'rolling_id': rolling_int, 'birth': birth_receive, 'user_nickname': nickname_receive,
           'user_id': user_id, 'cake_id': cake_receive, 'url': url}
    db.rollingpaper.insert_one(doc)

    return jsonify({'msg': '케이크가 만들어졌어요!', 'url': url})

