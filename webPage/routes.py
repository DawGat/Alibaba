from webPage import app, db
from flask import render_template, request, flash, redirect, url_for
from globals import Global
from flask_login import current_user, login_user, logout_user, login_required
from webPage.forms import LoginForm
from webPage.models import User
from webPage.forms import UserForm


@app.route('/signin', methods=["POST", "GET"])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('garage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('signin'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('garage'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/garage_opener/', methods=["POST", "GET"])
@login_required
def garage():
    if request.method == 'POST':
        if request.form.get('submit_open_gate') == 'Open gate':
            Global.switches[0].trigger()
        else:
            return render_template("garageOpener.html", title='Garage door opener')
    elif request.method == 'GET':
        print("No Post Back Call")
    return render_template("garageOpener.html", title='Garage door opener')


@app.route('/users/', methods=["POST", "GET"])
@login_required
def users_page():
    users = User.query.all()
    return render_template('Users.html', title='Users', users=users)


@app.route('/add_user/', methods=["POST", "GET"])
@login_required
def add_user():
    form = UserForm()
    users = User.query.all()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, is_admin=form.is_admin.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('User has been added!')
        return redirect(url_for('users_page'))
    return render_template('addUser.html', title='Add User', form=form, users=users)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('signin'))
