import boto3
import connect
import json
import sys
from sys import exit
import datetime
from datetime import datetime, timedelta
from operator import itemgetter
from requests import get
from boto3.session import Session
from operator import itemgetter
from requests import get
from pprint import pprint

start_time=sys.argv[1]
end_time=sys.argv[2]

def myconverter(o):
 #   if isinstance(o, datetime.datetime):
        return o.__str__()

def get_cloudwatch_metrics(args,instance_id,region):
#    region_name='ap-south-1')
#    cw = session.client('cloudwatch')
    instance_id=instance_id
    region=region
    conn=connect.connect()
#    now = datetime.utcnow()
#    past = now - timedelta(minutes=30)
#    future = now + timedelta(minutes=30)
    results=conn.get_metric_statistics(
    Namespace=args['Namespace'],
    MetricName=args['MetricName'],
    Dimensions=args['Dimensions'],
    StartTime=args['StartTime'],
    EndTime=args['EndTime'],
#    StartTime=past,
#    EndTime=future,
    Period=args['Period'],
    Statistics=['Average'])
    datapoints = results['Datapoints']
    list_datapoints=list(datapoints)
    list_datapoints[0]['instance_id']=instance_id
    list_datapoints[0]['region']=region
    list_datapoints[0]['StartTime']=args['StartTime']
    list_datapoints[0]['EndTime']=args['EndTime']
 #   return json.dumps(list_datapoints)
    return json.dumps(list_datapoints,default = myconverter)
 #   json_str = json.dumps(datapoints)
  #  print(datapoints)
    #last_datapoint = sorted(datapoints, key=itemgetter('Timestamp'))[-1]
    #utilization = last_datapoint['Average']
    #load = round((utilization/100.0), 2)
    #timestamp = str(last_datapoint['Timestamp'])
    #print("{0} load at {1}".format(load, timestamp))


def get_ec2_instances():
    connect.get_access()
    access_key = connect.get_access.aws_access_key_id
    secret_key = connect.get_access.aws_secret_access_key
    client = boto3.client('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key,region_name='ap-south-1')
    stime=datetime.strptime(start_time,'%Y-%m-%d')
    etime=datetime.strptime(end_time,'%Y-%m-%d')

    #client=connect.ec2_connect()
    ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
    for region in ec2_regions:
        conn = boto3.resource('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key,region_name=region)
        instances = conn.instances.filter()
        for instance in instances:
            if instance.state["Name"] == "running":
#                print (instance.id, instance.instance_type, region)
                pprint(get_cloudwatch_metrics({"Namespace":"AWS/EC2","StartTime": stime,"EndTime": etime,"MetricName": "CPUUtilization",
"Period": 86400,"Dimensions": [
            {
                "Name": "InstanceId",
                "Value": instance.id
               
            }
        ],
    },instance.id,region))

data=get_ec2_instances()
