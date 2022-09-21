"""
render template (basic.html, heaer.html, block content, footer.html)
use bootstrap
"""
import secrets

from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
Bootstrap(app)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/redirect')
def redirect_url_for():
    return render_template("redirect_url_for.html")

if __name__ == '__main__':
    app.run(debug=True)
