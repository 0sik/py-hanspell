from flask import Flask,jsonify
from flask import request
from hanspell import spell_checker
import json
import sys

app = Flask(__name__)

@app.route('/')
def hello():
    return "HelloWorld"


@app.route("/model",methods=['POST'])
def decision():
    text = request.get_json()['tags']
    spelled = spell_checker.check(text)
    spelled_text = spelled.checked
    json_data = {"message": spelled_text}
    return jsonify(json_data)


@app.route('/model', methods=['GET'])
def connect():
    return "Backend Server Connect"


if __name__ == '__main__':
    app.run(host='0.0.0.0' ,port = 5001, debug=True)