from flask import Flask, render_template, post;
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route("/")
def ask_story () {
    return render_template("questions.html")
}

@app.route("/story")
def show_story() {
    text = story.generate(request.args)
    return render_template("story.html", text = text)
}
