from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/pagoPA")
def pagoPA():
    return render_template("pagoPA.html")

@app.route("/assistenza")
def assistenza():
    return render_template("assistenza.html")

@app.route("/login")
def login():
    return render_template("login.html")

app.run(debug=True)
