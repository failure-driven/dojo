from flask import Flask, request
from rover import rover

app = Flask(__name__)


@app.route('/', methods=['POST'])
def application():
    return rover(request.json)
