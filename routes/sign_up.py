from flask import Blueprint, render_template, request, jsonify
from db import db


sign_up = Blueprint("sign_up", __name__, template_folder="templates")

@sign_up.route('/')
def question():
    return render_template("signUp.html")