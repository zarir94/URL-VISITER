from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World! v3'

@app.route('/about')
def about():
    return 'About v3'