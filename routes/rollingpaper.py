from flask import Blueprint, render_template, request, jsonify
from db import db

rolling = Blueprint("rolling", __name__, template_folder="templates")


# 롤링 페이퍼 페이지 기본 정보 get
@rolling.route('/<url>')
def get_rollingpaper(url):
    print(url)

    # test 주석
    # result = {'url': 'mina', 'rolling_id': 4, 'user_nickname': "mina", "cake_id": "choco"}
    # message_count = db.message.count_documents({'rolling_id': 4})

    result = db.rollingpaper.find_one({'url': url})
    message_count = db.message.count_documents({'rolling_id': result['rolling_id']})

    print(result)
    print(message_count)

    return render_template("guestMain.html", mainpage_info=result, message_count=message_count), 200
