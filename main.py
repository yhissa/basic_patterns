"""
# URL Route Registrations
# render template (basic.html, heaer.html, block content, footer.html)
# use bootstrap
# Message Flashing
"""
import secrets

from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
Bootstrap(app)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/redirect')
def redirect_url_for():
    return render_template("url_for.html")


@app.route('/flash', methods=["GET", "POST"])
def flash_message():
    # Flashes a message to the next request.
    # In order to remove the flashed message from the session and to display it to the user,
    # the template has to call get_flashed_messages().
    if request.method == "GET":
        flash('flash message is displayed.')
    return render_template("flash.html")


if __name__ == '__main__':
    app.run(debug=True)
