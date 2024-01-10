from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, index!'

@app.route('/about')
def about():
    return 'About'