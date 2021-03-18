from flask import Flask,request
from operations import add, sub, mult, div # type: ignore

app = Flask(__name__)


@app.route('/')
def func():
    
    return "<h1>hello</h1>"


@app.route('/add')
def add_func():
    a = request.args['a']
    b= request.args['b']

    return f"<h1> {add(int(a),int(b))} </h1>"

@app.route('/sub')
def sub_func():
    a = request.args['a']
    b= request.args['b']
    return f"<h1> {sub(int(a),int(b))} </h1>"

@app.route('/mult')
def mult_func():
    a = request.args['a']
    b= request.args['b']
    return f"<h1> {mult(int(a),int(b))} </h1>"

@app.route('/div')
def div_func():
    a = request.args['a']
    b= request.args['b']
    return f"<h1> {div(int(a),int(b))} </h1>"


