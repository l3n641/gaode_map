from flask.cli import load_dotenv
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from functions import get_lat_lon_from_gaode
import os
import random

load_dotenv()
app = Flask(__name__, template_folder='templates')
key_list = os.getenv("GAODE_KEY").split(",")

if not key_list:
    raise ValueError("初始化key失败")


@app.route("/")
def index():
    return render_template('map.html')


@app.route("/search", methods=["post"])
def search():
    address = request.form.get("address")
    key = None
    if address:
        key = random.choice(key_list)
        lat_lon = get_lat_lon_from_gaode(key, address)
        json_data = {
            'name': address,
            'center': lat_lon,
            "type": 1
        }

        return json_data
