from crypt import methods
from flask import Flask, render_template

app= Flask(__name__)


@app.route("/login", methods=['GET'])
def get_login():
    return render_template('login.html')

@app.route("/register", methods=['GET'])
def get_register():
    return render_template('register.html')
    