"""
# use bootstrap
# URL Route Registrations
# render template (basic.html, heaer.html, block content, footer.html)
# Message Flashing
"""
from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from forms import SampleForm
from dbmodel import User, app, db

ckeditor = CKEditor(app)
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


@app.route('/sample_form', methods=["GET", "POST"])
def sample_form():
    form = SampleForm()
    if form.validate_on_submit():

        user = User(
            name=request.form.get("username"),
            email=request.form.get("email"),
            password=request.form.get("password"),
            date=request.form.get("date"),
            body=request.form.get("body")
        )
        db.session.add(user)
        db.session.commit()

    return render_template("sample_form.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
