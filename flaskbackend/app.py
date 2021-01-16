from flask import (Flask, request, render_template, json, jsonify, url_for, session)
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS,cross_origin
from flask_restful import Resource, Api
import os
from werkzeug.utils import secure_filename
import logging
from PIL import Image

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)
api = Api(app)

UPLOAD_FOLDER = './images'
UPLOAD_FOLDERCAM = './cameraimg'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'rgba'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

    def __str__(self):
        return f'{self.id} {self.content}'

def todo_serializer(todo):
    return {
        'id': todo.id,
        'content': todo.content
      }

@app.route("/")
def my_index():
    return render_template("index.html")

@app.route("/api", methods = ['GET'])
@cross_origin()
def index():
    return jsonify([*map(todo_serializer, Todo.query.all())])

@app.route("/api/create", methods = ['POST'])
@cross_origin()
def create():
    request_data = json.loads(request.data)
    todo = Todo(content = request_data['content']) 

    db.session.add(todo)
    db.session.commit()

    return {'201': 'Add succesfully'}

@app.route("/api/create/<int:id>", methods = ['POST'])
@cross_origin()
def edit(id):
    request_data = json.loads(request.data)
    Todo.query.filter_by(id=request_data['id']).update({'content': request_data['content']})
    db.session.commit()

@app.route('/api/<int:id>', methods=['GET'])
@cross_origin()
def show(id):
    return jsonify([*map(todo_serializer, Todo.query.filter_by(id=id))])

@app.route('/api/<int:id>/delete', methods = ['POST'])
@cross_origin()
def delete(id):
    request_data = json.loads(request.data)
    Todo.query.filter_by(id=request_data['id']).delete()
    db.session.commit()



@app.route('/upload', methods=['POST'])
@cross_origin()
def fileUpload():
    target=os.path.join(UPLOAD_FOLDER,'')
    if not os.path.isdir(target):
        os.mkdir(target)
    logger.info("welcome to upload`")
    file = request.files['file'] 
    filename = secure_filename(file.filename)
    destination="/".join([target, filename])
    file.save(destination)
    session['uploadFilePath']=destination
    response="Upload successfully"
    return response

@app.route('/uploadcam', methods=['POST'])
@cross_origin()
def camUpload():
    target=os.path.join(UPLOAD_FOLDERCAM,'test_docs')
    if not os.path.isdir(target):
        os.mkdir(target)
    logger.info("welcome to upload`")
    file = request.files['file'] 
    img = Image.open(file.stream)
    if img.mode in ("RGBA", "P"): 
        img = img.convert("RGB")
    img.save('./cameraimg/imagefile.png')
    response="Upload successfully"
    return response

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True)
