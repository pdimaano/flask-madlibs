from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/questions')
def get_word_values():
    """"""
    words = excited_story.prompts

    return render_template(
        "questions.html",
        words=words
    )



@app.get('/story')
def show_story():
    """"""
    answers = request.args
    # print("!!!!!!!!", answers["noun"])
    text = excited_story.generate(answers)

    return render_template(
        "results.html",
        text=text
    )
