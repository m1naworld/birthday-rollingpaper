from flask import Blueprint, render_template, request, jsonify
from db import db


homework = Blueprint("homework", __name__, template_folder="templates")

@homework.route('/')
def question():
    return render_template("homework.html")

@homework.route('/<name>')
def answer(name):
    return "My name is " + name

@homework.route("/", methods=["POST"])
def homework_post():
    print(request.form)
    id = request.form['id_receive']
    comment = request.form['comment_receive']

    doc = {
        'id': id,
        'comment': comment
    }

    db.comment.insert_one(doc)

    print(id, comment)
    return jsonify({'msg': '응원 완료!'})

@homework.route("/view", methods=["GET"])
def homework_get():
    comments = list(db.comment.find({}, {"_id": False}))
    return jsonify({'comments': comments})