from flask import Flask, request, jsonify
from flask_cors import CORS
# We will need to import some methods to return the data from our other file where we get the data from the BCI
from BCIfakedata import test_to_send

app = Flask(__name__)
# Enable the cross origin resource sharing
CORS(app)

@app.route('/GETdata', methods=["GET"])
def index():
    # GET request
    if request.method == 'GET':
        message = {'textfield': test_to_send()}
        # Serialize and use JSON headers
        return jsonify(message)

# Debug make the server automatically reload over changes
app.run(debug=True, port=5555)
