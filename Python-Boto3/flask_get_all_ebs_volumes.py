from flask import Flask,jsonify
from get_all_ebs_volumes import *
from flask import abort
from flask import make_response
json_dict={}
app = Flask(__name__)

@app.route('/all-ebs-volumes',methods=['GET'])
def flask_get_all_ebs_volumes():
    response=get_all_volumes()
    if len(response) == 0:
        abort(404)
    json_dict["volumes"] = response
    return jsonify(json_dict)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
if __name__ == '__main__':
    app.run(debug=True)
