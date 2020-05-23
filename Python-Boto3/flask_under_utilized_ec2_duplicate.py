from flask import Flask,jsonify,request
import under_utilized_ec2
json_dict={}
app = Flask(__name__)

@app.route('/ec2_metrics',methods=['POST'])
def get_ec2_metrics():
    if request.is_json:
        content = request.get_json()
        response=under_utilized_ec2.get_ec2_instances(content)
        json_dict={}

    json_dict["Instance_details"] = response
    return jsonify(json_dict)
if __name__ == '__main__':
    app.run(debug=True)