from flask import Flask, jsonify, request
from requests import get
import traceback

app = Flask(__name__)

@app.route('/')
def home():
    url = request.args.get('url')
    if not url:
        return 'Add ?url=<any url>'
    res = dict(given=dict(url=url))
    try:
        r = get(url, timeout=23)
        res = res | dict(status=r.status_code, url=r.url, headers=dict(r.headers), body=r.text)
    except:
        res = res | dict(status=10101, trace=traceback.format_exc())
    return jsonify(res)

