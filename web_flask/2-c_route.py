from flask import Flask
app = Flask(__name__)

"""Task-2"""


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def replaceTexT(text):
    text = text.replace("_", " ")
    return "C " + text


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
