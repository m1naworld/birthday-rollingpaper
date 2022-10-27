from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from db import db


rolling = Blueprint("rolling", __name__, template_folder="templates")

@rolling.route('/')
def question():
    return render_template('rollingpaper.html')


