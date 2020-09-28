from flask import Flask, render_template, request
import switch_board


app = Flask(__name__)


@app.route('/alibaba/', methods=["POST", "GET"])
def alibaba():
    if request.method == 'POST':
        if request.form.get('submit_button_1') == 'value1':
            switch_board.trigger_switch(10)
        else:
            return render_template("alibaba.html")
    elif request.method == 'GET':
        print("No Post Back Call")
    return render_template("alibaba.html")