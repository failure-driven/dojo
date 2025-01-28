from flask import Flask, request, jsonify
from flask_cors import CORS
# import sys
# sys.path.insert(0, '../2024-10-21-mars-rover-py')
from rover import rover

app = Flask(__name__)
cors = CORS(app)


@app.route('/', methods=['POST'])
def application():
    response = jsonify(rover(request.json))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
