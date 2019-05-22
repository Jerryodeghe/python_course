"""
    Ignnore the warning you see from pylint about "UNABLE TO IMPORT FLASK". 
    To run the program from the "my_website" folder run the
    command:
    1. export FLASK_APP=application.py  
    2. python -m flask run

"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')