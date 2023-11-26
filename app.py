from flask import Flask, request, redirect, url_for
from flask_cors import CORS
import os

from trans import translatorMong

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


@app.route("/toMongolian", methods=['POST', 'GET'])
def translator():
    if request.method == 'POST':
        file = request.files.get('image')
        filename = sercure_filename(file.filename)
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            return 'No file uploaded'

        res = translatorMong(filename)
        return res
    elif request.method == 'GET':
        return 'GET'


if __name__ == "__main__":
    app.run()
