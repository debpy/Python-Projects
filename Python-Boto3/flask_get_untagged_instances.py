from flask import Flask,jsonify
from get_untagged_instances import untagged_instances
from flask import abort
from flask import make_response
json_dict={}
app = Flask(__name__)

@app.route('/untagged-instances',methods=['GET'])
def get_untagged_instances():
    response=untagged_instances()
    if len(response) == 0:
        abort(404)
    json_dict["Untagged-instances"] = response
    return jsonify(json_dict)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
if __name__ == '__main__':
    app.run(debug=True)