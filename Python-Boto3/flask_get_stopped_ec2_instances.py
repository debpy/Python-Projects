from flask import Flask,jsonify,request
from get_stopped_ec2_instances import *
from flask import abort
from flask import make_response
json_dict={}
app = Flask(__name__)

@app.route('/stopped-instances',methods=['POST'])
def get_stopped_instances():
    if not request.json and not 'days' in request.json:
        abort(400)
    else:
        days=request.json
        response=stopped_ec2_instances(days)
        json_dict["Stopped-Instances"] = response
        return jsonify(json_dict)
        
@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)
if __name__ == '__main__':
    app.run(debug=True)