 # app.py
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify(message="Hello level 400 FET, Quality Assurance!")
@app.route('/cause-error')
def cause_error():
    #Intentionally raise an exception to trigger a 500 error
    raise Exception('An error occurred')
if __name__ == '__main__':
    app.run(debug=True)
