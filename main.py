import flask
from flask import request, jsonify
import pandas as pd
from decouple import config

data = pd.read_csv(config('URL'))
data = data.to_dict('records')

app = flask.Flask(__name__)
app.config["DEBUG"] = False

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Records API</h1>
<p>A prototype API for reading HR records.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/data/all', methods=['GET'])
def api_all():
    return jsonify(data)

@app.route('/api/v1/resources/data/<int:rowcount>', methods=['GET'])
def api_test(rowcount):
    data_1 = data[:rowcount]
    return jsonify(data_1)

if __name__ == "__main__":
  app.run()