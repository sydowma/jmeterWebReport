from flask import Flask, request, render_template
import dirs_name
app = Flask(__name__)

app.debug = False

@app.route("/index", methods=["GET"])
def home():
    return render_template('home.html', dirs_name=dirs_name.dirs_name())