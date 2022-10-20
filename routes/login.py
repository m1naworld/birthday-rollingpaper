from flask import Blueprint, render_template, request, jsonify
from db import db


login = Blueprint("login", __name__, template_folder="templates")

@login.route('/')
def question():
    return render_template("login.html")
