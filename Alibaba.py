from flask import Flask, render_template, request
import switches
app = Flask(__name__)

switches.InitiateSwitches()

@app.route('/alibaba/', methods = ["POST", "GET"])
def alibaba():
    if request.method == 'POST':
        if request.form.get('submit_button_1') == 'value1':
            switches.openSwitches()
        else:
            return render_template("alibaba.html")
    elif request.method == 'GET':
        print("No Post Back Call")
    return render_template("alibaba.html")

if __name__ == '__main__':
   app.run('0.0.0.0', 5000, False)