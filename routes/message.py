from flask import Blueprint, render_template, request, jsonify
from db import db

message = Blueprint("message", __name__, template_folder="templates")

@message.route('/')
def msg():
    return render_template("message.html")
