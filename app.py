from flask import Flask, render_template, jsonify

from routes.cake import cake
from routes.login import login
from routes.message import message
from routes.rollingpaper import rolling
from routes.sign_up import sign_up
from routes.mypage import mypage
from datetime import datetime
from datetime import timedelta
from datetime import timezone

from flask_jwt_extended import (JWTManager, get_jwt, create_access_token, get_jwt_identity, set_access_cookies, jwt_required)
import os

app = Flask(__name__)

app.register_blueprint(login, url_prefix="/login")
app.register_blueprint(cake, url_prefix="/cake")
app.register_blueprint(message, url_prefix="/message")
app.register_blueprint(rolling, url_prefix="/rolling")
app.register_blueprint(sign_up, url_prefix="/sign-up")
app.register_blueprint(mypage, url_prefix="/mypage")

# jwt 관련
app.config["JWT_COOKIE_SECURE"] = False
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET')
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
jwt = JWTManager(app)


@app.route("/")
def hello_world():
    return "hello world!"

#refresh
@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        return response

#페이지별 확인
@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    user_id = get_jwt_identity()
    return jsonify(user_id=user_id), 200

@app.route("/message")
def msg():
    return render_template("message.html")

if __name__ == '__main__':
    app.run('0.0.0.0', port=7777, debug=True)