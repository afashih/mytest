from flask import Flask, render_template, url_for

from redis import StrictRedis

r = StrictRedis()


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('createQuestion.html')


@app.route('/about')
def about():
    return "<h1>About</h1>"


@app.route('/question/<title>')
def question(title):
    return "<h1>" + title + "</h1>"


if __name__ == "__main__":
    app.run(host="localhost", port="4000", debug=True)
