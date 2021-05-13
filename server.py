from flask import  Flask, render_template, request
app = Flask(__name__)

data = {"hello":"man"}

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.route("/data", methods = ["GET"])
def get():
    print("GET data:", data)
    return data

@app.route("/data", methods = ["POST"])
def post():
    data = request.get_json()
    print("SET data:", data)
    return "200"
if __name__ == "__main__":
    app.run()