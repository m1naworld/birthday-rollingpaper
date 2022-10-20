from flask import Blueprint, render_template, request, jsonify
from db import db


cake = Blueprint("cake", __name__, template_folder="templates")

@cake.route('/')
def question():
    return render_template("cake.html")