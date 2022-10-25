from flask import Blueprint, render_template, request, jsonify
from db import db


rolling = Blueprint("rolling", __name__, template_folder="templates")

# 롤링 페이퍼 페이지 get
@rolling.route('/<url>')
def get_rollingpaper(url):
    print(url)

    # test 주석
    # result = {'url': "mina", 'user_nickname': "mina", "cake_id": "choco"}
    # message_data = list(db.message.find({'rolling_id': 4}, {'_id': False}))

    result = db.rollingpaper.find_one({'url': url})
    message_data = list(db.message.find({'rolling_id': result['rolling_id']}))

    print(result)
    print(message_data)

    return render_template("guestMain.html", main_data=result, message_data=message_data, message_count=len(message_data))

