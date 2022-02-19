from flask import Flask, jsonify, request

from helpers import Automate

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():

    obj = Automate()

    projects = obj.get_projects()

    return jsonify({'projects': projects})


@app.route('/getFolder', methods=['POST'])
def getFolder():

    obj = Automate()

    current_project = request.json['folderName']

    folders, files = obj.open_folder(current_project)

    content = {
        'folders': folders,
        'files': files
    }

    return jsonify({'content': content})


@app.route('/getFileContent', methods=['POST'])
def getFileContent():
    obj = Automate()

    file = request.json['fileName']

    content = obj.get_file_content(file)

    return jsonify({'content': content})


@app.route('/startSetup', methods=['POST'])
def startSetup():

    obj = Automate()

    prefix = request.json['prefix']

    obj.start_setup(prefix)

    return jsonify({'message': 'Setup started'})
