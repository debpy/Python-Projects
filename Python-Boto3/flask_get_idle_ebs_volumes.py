from flask import Flask,jsonify,request
from get_idle_ebs_volumes import *
from flask import abort
from flask import make_response
json_dict={}
app = Flask(__name__)

@app.route('/get-unused-volumes',methods=['POST'])
def get_unused_ebs_volumes():
    if not all(item in request.json for item in ("StartTime","EndTime","IdleDays")):
        abort(400)
    else:
        data=request.json
        response=get_unused_volumes(data)
        json_dict["Volumes"] = response
        return jsonify(json_dict)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)
if __name__ == '__main__':
    app.run(debug=True)
