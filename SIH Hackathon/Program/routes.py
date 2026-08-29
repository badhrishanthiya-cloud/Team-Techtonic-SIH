from flask import Flask, render_template
from program import app


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")
