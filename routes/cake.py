from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from db import db
import bcrypt

cake = Blueprint("cake", __name__, template_folder="templates")

@cake.route('/')
def question():
    return render_template("cake.html")



@cake.route("/cake", methods=["POST"])
def sel_cake():

    cake_receive = request.form['cake_give']
    nickname_receive = request.form['nickname_give']
    birth_receive = request.form['birth_give']

    all_cake = list(db.rollingpaper.find({}, {'_id': False}))
    last_cake_num = all_cake.pop()['rolling_id']

    rolling_id = str(int(last_cake_num) + 1)
    cake_value = str(bcrypt.hashpw(rolling_id.encode('utf-8'), bcrypt.gensalt()), 'utf-8')
    rolling_int = int(rolling_id)
    print(cake_receive, nickname_receive, birth_receive, rolling_id )
    # 세션에서 현재 유저 받아오기
    user_id = request.form['temp_user']

    url = str(bcrypt.hashpw(rolling_id.encode('utf-8'), bcrypt.gensalt()), 'utf-8')
    # print(bcrypt.hashpw(rolling_id.encode('utf-8'), bcrypt.gensalt()))
    print(url)
    doc = {'rolling_id': rolling_int, 'birth': birth_receive, 'user_nickname': nickname_receive,
           'user_id': user_id, 'cake_id': cake_receive, 'url': url}
    db.rollingpaper.insert_one(doc)

    return jsonify({'url': url})