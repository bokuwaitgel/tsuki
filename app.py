from flask import Flask, request, redirect, url_for
from flask_cors import CORS

import os

from test import MazaalToRequest, GetResult
from hello import tableJson

UPLOAD_FOLDER = './images'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def sercure_filename(filename):
    return 'img' + '.'+filename.rsplit('.', 1)[1].lower()

@app.route("/")
def index():
    return "Hello World!"

@app.route("/question" , methods=['POST', 'GET'])
def test():
    if request.method == 'POST':
        file = request.files.get('image')
        filename = sercure_filename(file.filename)
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else: 
            return 'No file uploaded'
        prompt = request.form.get('prompt')
        result =  MazaalToRequest(filename, prompt)
        return result

    else:
        return 'No file uploaded'
    
@app.route("/getResult" , methods=['GET'])
def getResult():
    return GetResult(request.args.get("id"))

@app.route("/extractTable" , methods=['POST'])
def extractTable():
    if request.method == 'POST':
        file = request.files.get('image')
        filename = sercure_filename(file.filename)
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else: 
            return 'No file uploaded'
    return tableJson(filename)

if __name__ == "__main__":
    app.run()