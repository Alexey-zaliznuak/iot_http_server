from flask import  Flask, render_template, request, redirect, url_for, flash, make_response, session
from control_elemets_storage import ControlElementStorage
import datetime

app = Flask(__name__)
app.permanent_session_lifetime = datetime.timedelta(days=1)
app.secret_key = "644540709"

db_path = "./data/control-elements-state.db"
elements_manager = ControlElementStorage(db_path,  "ControlElements")

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.route("/")
def about():
    return render_template("index.html")

@app.route("/SetState/<obj>/<state>/", methods = ["GET"])
def chage_state(obj, state):
    elements_manager.update_element(obj, state)
    return "200"

@app.route("/GetState/<obj>")
def get_state(obj):
    response = elements_manager.get_state(obj)[0][0]
    return response
    #actuators = светодиоды, реле и т.д. (от англ. action = действие)
    #sensors = кнопки, 
if __name__ == "__main__":
    app.run(host="192.168.126.174", port="5000")