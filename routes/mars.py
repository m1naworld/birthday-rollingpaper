from flask import Blueprint, render_template, request, jsonify
from db import db


mars = Blueprint("mars", __name__, template_folder="templates")

@mars.route('/')
def question():
    return render_template("mars.html")


@mars.route("/", methods=["POST"])
def web_mars_post():
    print(request.form)
    name_receive = request.form['name']
    address_receive = request.form['address']
    size_receive = request.form['size']
    doc = {
        'name': name_receive,
        'address': address_receive,
        'size': size_receive
    }
    db.mars.insert_one(doc)
    return jsonify({'msg': 'POST 연결 완료!'})


@mars.route("/view", methods=["GET"])
def web_mars_get():
    mars = list(db.mars.find({}, {'_id': False}))
    return jsonify({'mars': mars})

