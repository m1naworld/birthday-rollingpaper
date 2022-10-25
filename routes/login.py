from flask import Blueprint, render_template, request, jsonify, Flask
from db import db
import os
from dotenv import load_dotenv
import bcrypt
from flask_jwt_extended import (
    create_access_token, create_refresh_token, jwt_required, get_jwt_identity,
)

login = Blueprint("login", __name__, template_folder="templates")

@login.route('/')
def question():
    return render_template("login.html")

# jwt 관련
@login.route("/token", methods=["POST"])
def create_token():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    user_id = request.json.get("user_id", None)
    password = request.json.get("password", None)
    print(password)

    if not user_id:
        return jsonify({"msg": "아이디를 입력해주세요"}), 400
    if not password:
        return jsonify({"msg": "비밀번호를 입력해주세요"}), 400

    user = db.user.find_one({'user_id': user_id}) # 나중에 수정!
    userId = user['user_id']
    passWord = user['password']

    ispasswordcorrect = bcrypt.checkpw(password.encode('utf-8'), passWord)

    if user_id != userId or ispasswordcorrect != True:
        return jsonify({'msg': '아이디가 없거나 일치하는 비밀번호가 없습니다'}), 401

    access_token = create_access_token(identity=user_id)
    refresh_token = create_refresh_token(identity=user_id)
    return jsonify(access_token=access_token, refresh_token=refresh_token), 200

