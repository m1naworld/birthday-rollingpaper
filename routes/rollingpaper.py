from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from db import db
import bcrypt
from flask_jwt_extended import (get_jwt_identity, jwt_required)

from routes.login import token_out

rolling = Blueprint("rolling", __name__, template_folder="templates")

# 로그인 확인
@rolling.route('/check')
@jwt_required()
def check_user():
    try:
        user_id = get_jwt_identity()
        response = jsonify({"msg": "로그인한 회원"})
        return response, 200

    except TypeError:
        response = jsonify({"msg": '로그인 안한 회원'})
        return response, 500

# 롤링 페이퍼 페이지 기본 정보 get
# 로그인 유저용
@rolling.route('/')
@jwt_required()
def get_my_rollingpaper():
    try:
        user_id = get_jwt_identity()
        url = request.args.get('key')
        print(url)

        result = db.rollingpaper.find_one({'url': url}, {'_id': False})
        print(result)
        message_count = db.message.count_documents({'rolling_id': result['rolling_id']})
        # return render_template("rollingpaper.html", mainpage_info=result, message_count=message_count), 200

        success = result['user_id'] == user_id
        if(success):
            message_count = db.message.count_documents({'rolling_id': result['rolling_id']})
            return render_template("rollingpaper.html", mainpage_info=result, message_count=message_count), 200
        else:
            token_out()
            return render_template("login.html")
    except:
        return render_template("login.html")


# 롤링 페이퍼 페이지 기본 정보 get
# 로그인 안한 유저(게스트용)
@rolling.route('/guest/')
def get_rollingpaper():

    url = request.args.get('key')

    result = db.rollingpaper.find_one({'url': url})
    message_count = db.message.count_documents({'rolling_id': result['rolling_id']})
    return render_template("guestMain.html", mainpage_info=result, message_count=message_count), 200



# 롤링 페이지 캔들 정보 get
@rolling.route('/detail-data/<rolling_id>')
def get_candle(rolling_id):
    print(type(rolling_id))
    url = request.args.get('key')
    message_list = list(db.message.find({'rolling_id': int(rolling_id)}, {'_id': False}))
    print(message_list)
    return jsonify({'message_list': message_list}), 200


# 메시지 비밀번호 확인
@rolling.route('/message/check', methods=['POST'])
def check_message_password():
    rolling_id = request.form['rolling_id']
    password = request.form['message_password']
    message_id = request.form['message_id']
    print(message_id)
    print(password)

    data = db.message.find_one({'rolling_id': int(rolling_id), 'message_id': int(message_id)}, {'_id': False})

    password2 = data['message_password']

    print(password2)

    if bcrypt.checkpw(password.encode('utf-8'), password2.encode('utf-8')):
        success = True
        message = '비밀번호 일치'
        print("일치")
    else:
        success = False
        message = '비밀번호 불일치, 다시 입력해주세요!'
        print("불일치")

    return jsonify({'success': success, 'message': message, 'data': data})



# 메시지 내용 수정
@rolling.route('/message/update', methods=['POST'])
def message_update():
    rolling_id_receive = request.form['rolling_id']
    message_id_receive = request.form['message_id']
    message_content_receive = request.form['message_content']

    db.message.update_one({'rolling_id': int(rolling_id_receive), 'message_id': int(message_id_receive)}, {'$set': {'content': message_content_receive}})
    return jsonify({'message': '수정 완료!'}), 200


# 메시지 삭제
@rolling.route('/message/removal', methods=['POST'])
def message_delete():
    rolling_id_receive = request.form['rolling_id']
    message_id_receive = request.form['message_id']

    db.message.delete_one({'rolling_id': int(rolling_id_receive), 'message_id': int(message_id_receive)})
    return jsonify({'message': '삭제 완료!'}), 200

