"""
# use bootstrap
# URL Route Registrations
# render template (basic.html, header.html, block content, footer.html)
# Message Flashing
"""
from flask import render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
# Login System
from flask_login import login_user, LoginManager, login_required, current_user, logout_user
# Generate password hash
from werkzeug.security import generate_password_hash, check_password_hash
# Import forms
from forms import SampleForm, LoginForm
# Initialize app. Connect to database.
from dbmodel import User, app, db

ckeditor = CKEditor(app)
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Check password
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            hashed_password = user.password
            if check_password_hash(hashed_password, password):
                # Logged in
                login_user(user)
                # redirect to home
                return redirect(url_for('home'))
            else:
                flash('Password is wrong. Please, try again.')
        else:
            flash('This email is not registered.')

    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/')
def home():
    # Read all record from database.
    users = User.query.all()
    for user in users:
        print(user.name, user.email, user.date, user.body)

    # Read a particular record by query from database.
    particular_user = User.query.filter_by(name='John').first()

    # Update A Particular Record By Query
    update_user = User.query.filter_by(name='John').first()
    if update_user:
        update_user.email = 'Johnson@email.address.com'
        db.session.commit()

    # Update A Record By PRIMARY KEY
    user_id = 3
    update_user_by_key = User.query.get(user_id)
    if update_user_by_key:
        update_user_by_key.date = '2022-09-26'
        db.session.commit()

    # Delete A Particular Record By PRIMARY KEY
    delete_id = 100
    delete_user = User.query.get(delete_id)
    if delete_user:
        db.session.delete(delete_user)
        db.session.commit()
    return render_template("index.html", users=users,
                           particular_user=particular_user,
                           update_user=update_user,
                           update_user_by_key=update_user_by_key)


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
        # Create a new record.
        user = User(
            name=request.form.get("username"),
            email=request.form.get("email"),
            password=generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8),
            date=request.form.get("date"),
            body=request.form.get("body")
        )
        db.session.add(user)
        db.session.commit()

    return render_template("sample_form.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
