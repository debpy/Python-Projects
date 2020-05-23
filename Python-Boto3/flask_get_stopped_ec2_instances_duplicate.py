from flask import Flask,jsonify
from get_stopped_ec2_instances import *
from flask import abort
from flask import make_response
json_dict={}
app = Flask(__name__)

@app.route('/stopped-instances',methods=['GET'])
def get_stopped_instances():
    response=stopped_ec2_instances()
    if len(response) == 0:
        abort(404)
    json_dict["Stopped-Instances"] = response
    return jsonify(json_dict)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
if __name__ == '__main__':
    app.run(debug=True)