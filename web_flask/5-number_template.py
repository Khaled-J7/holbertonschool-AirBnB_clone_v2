
#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def show():
    """display Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def show2():
    """display HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def show3(text):
    """display “C ” followed by the value
    of the text variable (replace
    underscore _ symbols with a space )"""
    text = text.replace("_", " ")
    return "C {}".format(escape(text))


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def show4(text="is cool"):
    """display “Python ”, followed by the value of
    the text variable (replace
    underscore _ symbols with a space """
    text = text.replace("_", " ")
    return "Python {}".format(escape(text))


@app.route("/number/<int:n>", strict_slashes=False)
def show5(n):
    """display “n is a number”
    only if n is an integer"""
    return "{} is a number".format(escape(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def show6(n):
    """display a HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

