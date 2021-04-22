from flask import  Flask, render_template, request
from control_elemets_storage import ControlElementStorage
from elements import *
app = Flask(__name__)

global values
values = {}

#element(name = "BEACON", value_type = "range 0 1023 1", put_type = "input"),
#element(name = "DISPLAY", value_type = "text", put_type = "input")

db_path = "./data/control-elements-state.db"
elements_manager = ControlElementStorage(db_path,  "ControlElements")

storage = init()
html = storage.get_elements_html()

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

if __name__ == "__main__":
    app.run(host="192.168.1.29", port="5000", debug=True)
    #host="192.168.126.174", port="5000"