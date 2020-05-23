from flask import Flask,jsonify
import under_utilized_ec2
json_dict={}
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"
@app.route('/ec2_metrics',methods=['GET'])
def get_ec2_metrics():
    response=under_utilized_ec2.get_ec2_instances({
        "StartTime": "2018-07-01",
        "EndTime": "2018-08-16",
         "CPUPercent":10,
         "NetworkIO":30
})
    json_dict["Instance_details"] = response
    return jsonify(json_dict)
if __name__ == '__main__':
    app.run(debug=True)