from flask import Blueprint, render_template, request, jsonify, Flask

from db import db

mypage = Blueprint("mypage", __name__, template_folder="templates")

@mypage.route('/')
def question():
    return render_template("mypage.html")

@mypage.route('/show', methods=["GET"])
def cshow():

    rolling_list = list(db.rollingpaper.find({}, {'_id': False}))

    return jsonify({'rollings': rolling_list})

    return all_rolling

@mypage.route('/delete', methods=["POST"])
def cdelete():
    return render_template("mypage.html")