from flask import Blueprint, render_template, request, jsonify, Flask
from db import db
import os
from dotenv import load_dotenv
import bcrypt
from flask_jwt_extended import (
    create_access_token, unset_jwt_cookies, set_access_cookies
)

login = Blueprint("login", __name__, template_folder="templates")

@login.route('/')
def question():
    return render_template("login.html")

# jwt 관련
@login.route("/token", methods=["POST"])
def create_token():
    try:
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400

        user_id = request.json.get("user_id", None)
        password = request.json.get("password", None)

        print(password)

        if not user_id:
            return jsonify({"msg": "아이디를 입력해주세요"}), 400
        if not password:
            return jsonify({"msg": "비밀번호를 입력해주세요"}), 400

        user = db.user.find_one({'user_id': user_id})
        userId = user['user_id']
        passWord = user['password']

        ispasswordcorrect = bcrypt.checkpw(password.encode('utf-8'), passWord.encode('utf-8'))


        if user_id != userId or ispasswordcorrect != True:
            return jsonify({'msg': '아이디가 없거나 일치하는 비밀번호가 없습니다'}), 401

        response = jsonify({"msg": "로그인 완료"})
        access_token = create_access_token(identity=user_id)
        set_access_cookies(response, access_token)
        return response, 200
    except TypeError:
        response =jsonify({"msg": '아이디가 없거나 일치하는 비밀번호가 없습니다'})
        return response, 500




@login.route("/tokenout", methods=["POST"])
def token_out():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response