from flask import Blueprint, render_template, request, jsonify
from db import db


cake = Blueprint("cake", __name__, template_folder="templates")

@cake.route('/')
def question():
    return render_template("cake.html")

@cake.route("/cake", methods=["GET"])
def find_user():
    temp_user = list(db.temp_user.find({},{'_id':False}))

    return jsonify(temp_user)

@cake.route("/cake", methods=["POST"])
def sel_cake():
    cake_receive = request.form['cake_give']
    nickname_receive = request.form['nickname_give']
    birth_receive = request.form['birth_give']

    user_id = request.form['temp_user']

    db.rollingpaper.update_one({'user_id': user_id}, {'$set': {'cake_id': cake_receive}})
    db.rollingpaper.update_one({'user_id': user_id}, {'$set': {'user_nickname': nickname_receive}})
    db.rollingpaper.update_one({'user_id': user_id}, {'$set': {'birth': birth_receive}})

    return jsonify({'msg': '케이크가 만들어졌어요!'})
