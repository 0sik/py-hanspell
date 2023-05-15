from flask import Flask,jsonify
from flask import request
from hanspell import spell_checker
import json
import sys

app = Flask(__name__)

@app.route('/')
def hello():
    return "HelloWorld"


@app.route("/api/grammers/check",methods=['POST'])
def decision():
    text = request.get_json()['content']
    content_chunks = [text[i:i+500] for i in range(0, len(text), 500)]

    spelled_text_chunks = []
    for chunk in content_chunks:
        spelled = spell_checker.check(chunk)
        spelled_text_chunks.append(spelled.checked)

    spelled_text = ''.join(spelled_text_chunks)
    json_data = {"content": spelled_text}
    return jsonify(json_data)
# 람다형식
# import json
# from hanspell import spell_checker

# def lambda_handler(event, context):
#     text = event['content']
#     content_chunks = [text[i:i+500] for i in range(0, len(text), 500)]

#     spelled_text_chunks = []
#     for chunk in content_chunks:
#         spelled = spell_checker.check(chunk)
#         spelled_text_chunks.append(spelled.checked)

#     spelled_text = ''.join(spelled_text_chunks)

#     return {
#         "content": spelled_text
#     }



@app.route('/model', methods=['GET'])
def connect():
    return "Backend Server Connect"


if __name__ == '__main__':
    app.run(host='0.0.0.0' ,port = 5001, debug=True)