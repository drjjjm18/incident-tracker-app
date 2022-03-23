from flask import Flask
from flask import url_for
app = Flask(__name__)

@app.route("/")
def hello_world():
    url_for('static', filename='style.css')
    return "<p>Hello, World!</p>"