from models.control_elemets_storage import ControlElementStorage
from models.values_manager import ValuesManeger
from flask import  Flask, render_template, request
from elements import *
from socket import gethostbyname, gethostname
from json import load
from os import environ, system

IP = gethostbyname(gethostname())
application = Flask(__name__)

db_path = "./data/control-elements-state.db"
elements_manager = ControlElementStorage(db_path,  "ControlElements")
storage = init()
ValuesManeger = ValuesManeger()

html = storage.get_elements_html()
output_elements_values = {"humidity-sensor": "30", "gas-sensor" : "400", "temperature" : "20°C"}
values = {}
history_values = {}

@application.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@application.route("/content")
def get_elements_content():
    return html

@application.route("/")
def index():
    return render_template("index.html")

@application.route("/input_elements/state/", methods = ["GET"])
def set_state():
    return values

@application.route("/input_elements/state/", methods = ["POST"])
def get():
    values = request.get_json()
    print(values)
    ValuesManeger.write(values)
    return "200"

@application.route("/output_elements/state/", methods = ["GET"])
def output_values():
    return output_elements_values
    
@application.route("/output_elements/state/", methods = ["POST"])
def get_outputs_elements():
    global output_elements_values
    values = request.get_json()

    ValuesManeger.write(values)
    return "200"

@application.route("/graphics/<name>")
def get_graphs(name):
    graphic_values = ValuesManeger.get(name)
    return graphic_values

@application.route("/graphsics")
def graphs():
    name = request.args['name']
    return render_template("graphs.html")

def main():
    application.run(IP, port = 5000, debug = True)

if __name__ == "__main__":
    main()