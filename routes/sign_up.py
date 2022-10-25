from flask import Blueprint, render_template, request, jsonify
from db import db
from dotenv import load_dotenv
import os
import bcrypt

sign_up = Blueprint("sign_up", __name__, template_folder="templates")

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


# 회원가입 API
@sign_up.route("/", methods=["POST"])
def join():

    print(request.form)
    user_id = request.form['user_id']
    password = request.form['password']
    print(user_id)
    print(password)

    # print(request.form)
    # user_id = request.form['user_id']
    # password = request.form['password']
    # print(user_id)
    # print(password)
    user_id = "mina"  # 임의 지정! 지워주세영!!
    password = "minaa"  # 임의 지정! 지워주세영!!

    user = db.user.find_one({'user_id': user_id})

    if(user):
        return jsonify("message", "다시 시도 해 주세요.")

    else:
        # 비밀번호 해쉬
        password = password.encode('utf-8')
        password_hash = bcrypt.hashpw(password, bcrypt.gensalt())
        print(password_hash)

        # 실제 저장 되는 값
        insert_password_hash = password_hash.decode()
        print(insert_password_hash)
        insert_password_hash = "$2b$12$veVxHEZEw2.Q/sGioOUxKO32anq3uq0wsGM/jGhpZAaR1Ta.CFhfW"

        # DB 저장
        db.user.insert_one({'user_id': user_id, 'password': insert_password_hash})


        # 프론트에서 받아온 값과 DB조회 비밀번호 값 일치 확인
        # print(bcrypt.checkpw(password, insert_password_hash.encode('utf-8')))

        return jsonify("message", "회원가입 성공!")


