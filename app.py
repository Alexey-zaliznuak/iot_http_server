from flask import  Flask, render_template, request
from control_elemets_storage import ControlElementStorage
from elements import *
from socket import gethostbyname, gethostname
from json import load
from os import environ, system

IP = gethostbyname(gethostname())
application = Flask(__name__)

db_path = "./data/control-elements-state.db"
elements_manager = ControlElementStorage(db_path,  "ControlElements")
storage = init()

html = storage.get_elements_html()
values = {}
history = {}
output_elements_values = {"humidity-sensor": "30", "gas-sensor" : "400", "temperature" : "20°C"}

@application.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@application.route("/content")
def get_elements_content():
    return html

@application.route("/output_values", methods = ["GET"])
def output_values():
    return output_elements_values

@application.route("/")
def index():
    return render_template("index.html")

@application.route("/State/", methods = ["GET"])
def set_state():
    global values
    print(values)
    return values

@application.route("/State/", methods = ["POST"])
def get():
    global values
    values = request.get_json()
    print(values)
    return "200"

@application.route("/State/output_elements", methods = ["POST"])
def get_outputs_elements():
    global output_elements_values
    values = request.get_json()
    print(values)
    return "200"

def main():
    application.run(IP, port = 5000, debug = True)

if __name__ == "__main__":
    main()