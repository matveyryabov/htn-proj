from flask import (Flask, request, render_template, json, jsonify)
from flask_cors import CORS,cross_origin

app = Flask(__name__)

@app.route("/")
def my_index():
    return render_template("index.html")

#uploaded route
@app.route('/api/upload', methods = ['POST'])
@cross_origin()

if __name__ == "__main__":
    app.run(debug=True)
