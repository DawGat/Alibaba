from flask import Flask, render_template, request, flash, redirect, url_for
from globals import Global
from webPage.flaskConfig import Config
from webPage.forms import LoginForm

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('garage'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/garage_opener/', methods=["POST", "GET"])
def garage():
    if request.method == 'POST':
        if request.form.get('submit_open_gate') == 'Open gate':
            Global.switches[0].trigger()
        else:
            return render_template("garageOpener.html", title='Garage door opener')
    elif request.method == 'GET':
        print("No Post Back Call")
    return render_template("garageOpener.html", title='Garage door opener')
