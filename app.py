from flask import Flask
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_folder='covidmodels/build', static_url_path='')
CORS(app)

# for api
@cross_origin()
@app.route('/api', methods=['GET'])
def index():
    return {
        "finalProject": "Final Project Website"
    }

@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run()