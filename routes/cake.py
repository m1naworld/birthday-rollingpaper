from flask import Blueprint, render_template, request, jsonify
from db import db


cake = Blueprint("cake", __name__, template_folder="templates")

@cake.route('/')
def question():
    return render_template("cake.html")

@cake.route("/cake", methods=["POST"])
def sel_cake():
    all_cake = list(db.rollingpaper.find({}, {'_id': False}))

    cake_receive = request.form['cake_give']
    nickname_receive = request.form['nickname_give']
    birth_receive = request.form['birth_give']

    user_id = request.form['temp_user']
    # 콜렉터 신규 입력시
    db.rollingpaper.insert_one({'user_id': user_id}, {'$set': {'rolling_id': user_id + int(len(all_cake) + 1)}})
    db.rollingpaper.insert_one({'user_id': user_id}, {'$set': {'cake_id': cake_receive}})
    db.rollingpaper.insert_one({'user_id': user_id}, {'$set': {'user_nickname': nickname_receive}})
    db.rollingpaper.insert_one({'user_id': user_id}, {'$set': {'birth': birth_receive}})

    return jsonify({'msg': '케이크가 만들어졌어요!'})
