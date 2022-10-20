from flask import Blueprint, render_template, request, jsonify
from db import db


signUp = Blueprint("signUp", __name__, template_folder="templates")

@signUp.route('/')
def question():
    return render_template("signUp.html")