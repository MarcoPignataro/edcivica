from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")
@app.route(pagoPa)
def pagoPa():
    return render_template("pagoPa.html")
app.run(debug=True)