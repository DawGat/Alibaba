from flask import Flask, render_template, request
import switches
app = Flask(__name__)


@app.route('/alibaba/', methods=["POST", "GET"])
def alibaba():
    if request.method == 'POST':
        if request.form.get('submit_button_1') == 'value1':
            switches.trigger_switch(1)
        else:
            return render_template("alibaba.html")
    elif request.method == 'GET':
        print("No Post Back Call")
    return render_template("alibaba.html")