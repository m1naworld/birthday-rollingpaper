from flask import Blueprint, render_template, request, jsonify, Flask

from db import db

from flask_jwt_extended import (get_jwt_identity, jwt_required)

mypage = Blueprint("mypage", __name__, template_folder="templates")

@mypage.route('/')
def question():
    return render_template("mypage.html")

@mypage.route('/show', methods=["GET"])
@jwt_required()
def cshow():
    user_id = get_jwt_identity()
    rolling_list = list(db.rollingpaper.find({'user_id':user_id}, {'_id': False}))

    return jsonify({'rollings': rolling_list})

    return all_rolling

@mypage.route('/delete', methods=["POST"])
def cdelete():

    del_num = request.form['del_num']
    del_num = int(del_num)

    print(type(del_num))

    db.rollingpaper.delete_one({'rolling_id': del_num})

    return "삭제가 완료되었습니다"