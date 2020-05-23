from flask import Flask,jsonify
import get_untagged_instances
from flask import abort
from flask import make_response

json_dict={}
app = Flask(__name__)

@app.route('/get-untagged-instances',methods=['GET'])
def get_untagged_instances():
    response=get_untagged_instances.get_untagged_instances()
	if len(response) == 0:
		abort(404)
	json_dict["Untagged_instances"] = response
    return jsonify(json_dict)
if __name__ == '__main__':
    app.run(debug=True)