from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, index! Are you deploying??'

@app.route('/about')
def about():
    return 'About'