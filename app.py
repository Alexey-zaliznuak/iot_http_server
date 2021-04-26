from flask import  Flask, render_template, request
from control_elemets_storage import ControlElementStorage
from socket import gethostbyname, gethostname
from elements import *
from json import load
from os import environ, system
import asyncio

with open("settings.json", "r") as f:
    settings = load(f)

IP = gethostbyname(gethostname())
app = Flask(__name__)

db_path = "./data/control-elements-state.db"
elements_manager = ControlElementStorage(db_path,  "ControlElements")

global values, output_elements_values
storage = init()
html = storage.get_elements_html()

values = {}
output_elements_values = {"humidity-sensor": "30", "gas-sensor" : "400", "temperature" : "20°C"}

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.route("/content")
def get_elements_content():
    return html

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/State/", methods = ["GET"])
def set_state():
    global values
    print(values)
    return values

@app.route("/State/", methods = ["POST"])
def get():
    global values
    values = request.get_json()
    print(values)
    return "200"

@app.route("/State/output_elements", methods = ["GET"])
def get_outputs_elements():
    global output_elements_values
    values = request.get_json()
    print(values)
    return "200"

async def main():
    app.run(IP, port = 5000, debug = True)

if __name__ == "__main__":
    asyncio.run(main())