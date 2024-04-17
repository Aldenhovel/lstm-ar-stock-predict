import torchinfo
from flask import Flask, render_template, request, jsonify, send_file
from predict import *
from grab import *
from backend import *


app = Flask(__name__, template_folder='./templates/', static_folder='./static/')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/processGreedySearch', methods=["POST"])
def processGreedySearch():
    data = request.get_json()
    checkpoint, search_step, code, date = unpackGreedySearchProfile(data)
    yaml_path = getSampleByCode(code, date)
    modelstate.updateState({'checkpoint': checkpoint})
    response = greedySearch(modelstate, yaml_path, search_step)
    return jsonify(response)

@app.route('/processBeamSearch', methods=["POST"])
def processBeamSearch():
    data = request.get_json()
    checkpoint, search_step, code, date, beam_size = unpackBeamSearchProfile(data)
    yaml_path = getSampleByCode(code, date)
    modelstate.updateState({'checkpoint': checkpoint})
    response = beamSearch(modelstate, yaml_path, search_step, beam_size)
    return jsonify(response)


@app.route('/getCheckpointsItems', methods=["GET"])
def getCheckpointsItems():
    response = {
        'checkpoints': getCheckpointsFilesName()
    }
    return jsonify(response)


if __name__ == "__main__":
    import sys
    sys.path.append('..')
    modelstate = ModelState()
    app.run()
