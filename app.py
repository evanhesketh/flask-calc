# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

@app.get("/add")
def return_sum():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(operations.add(a, b))

@app.get("/sub")
def return_difference():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(operations.sub(a, b))

@app.get("/mult")
def return_product():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(operations.mult(a, b))

@app.get("/div")
def return_quotient():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(operations.div(a, b))

