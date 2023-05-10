from flask import Flask, render_template
import datetime
import os

app = Flask(__name__)

@app.context_processor
def handle_context():
    return dict(os=os)

@app.route("/")
def index():
    #return render_template("index.html")
    #return render_template("login.html")
    return render_template("registro.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')