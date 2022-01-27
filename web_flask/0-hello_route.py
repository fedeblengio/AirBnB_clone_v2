from flask import Flask
app = Flask(__name__)

"""Task-0"""


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
