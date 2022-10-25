from flask import Blueprint, render_template, request, jsonify
from db import db
from dotenv import load_dotenv
import os
from flask_bcrypt import Bcrypt

sign_up = Blueprint("sign_up", __name__, template_folder="templates")

bcrypt = Bcrypt()

@sign_up.route('/')
def question():
    return render_template("signUp.html")

# 회원가입 아이디 중복 확인 API
@sign_up.route("/check", methods=["GET"])
def check_id():
        # 프론트에서 요청: /sign-up/check?id=값
        user_id = request.args.get('id')
        print(user_id)

        result = db.user.find_one({'user_id': user_id})
        print(result)
        print(type(result))
        print(result == None)

        if(result == None):
            doc = {"message": "사용 가능한 아이디 입니다.", "success": True}
        else:
            doc = {"message": "이미 사용 중인 아이디 입니다.", "success": False}

        return jsonify(doc)


load_dotenv()
salt = os.getenv('password_salt')


# 회원가입 API
@sign_up.route("/", methods=["POST"])
def join():
    print(request.form)
    user_id = request.form['user_id']
    password = request.form['password']
    print(user_id)
    print(password)

    # 비밀번호 해쉬
    hashed_password = bcrypt.generate_password_hash(password, int(salt))
    print(hashed_password)

    db.user.insert_one({'user_id': user_id, 'password': hashed_password})

    return jsonify("message", "회원가입 성공!")

