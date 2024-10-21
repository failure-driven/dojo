from flask import Flask, request
from flask_cors import CORS
from rover import rover

app = Flask(__name__)
cors = CORS(app)


@app.route('/', methods=['POST'])
def application():
    return rover(request.json)
