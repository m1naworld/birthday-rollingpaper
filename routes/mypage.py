from flask import Blueprint, render_template, request, jsonify, Flask

mypage = Blueprint("mypage", __name__, template_folder="templates")

@mypage.route('/')
def question():
    return render_template("mypage.html")