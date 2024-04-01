from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.7sv4ic7.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }
    db.pan.insert_one(doc)
    return jsonify({'msg':'응원해주셔서 감사합니다!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    pan_list = list(db.pan.find({}, {'_id': False}))
    return jsonify({'pan': pan_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5002, debug=True)