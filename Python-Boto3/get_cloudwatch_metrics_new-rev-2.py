import boto3
import connect
import json
import sys
from sys import exit
import datetime
#from datetime import datetime, timedelta
from operator import itemgetter
from requests import get
from boto3.session import Session
from operator import itemgetter
from requests import get
from pprint import pprint

#time=sys.argv[1]
#end_time=sys.argv[2]

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
'''
def jsonDefault(object):
    return object.__dict__
'''
def get_cpu_utilization(args):
#    session = Session(aws_access_key_id='AKIAIUIJFOR6DP7ZH6LQ',aws_secret_access_key='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',
#    region_name='ap-south-1')
#    cw = session.client('cloudwatch')
#    print(args)
    instance_id=args['InstanceId']
    region=args['Region']
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
 #   print("datapoints=",datapoints)
    dict_datapoints=dict((key,d[key]) for d in datapoints for key in d)
 #   print("dict_datapoints=",dict_datapoints)
    if dict_datapoints['Average'] < 8:
        print("The average CPU Utilization has been less than 8% for the last 30 days")
    else:
        print("The average CPU Utilization is above the threshold 8% for the last 30 days")

    #list_datapoints=list(datapoints)
    dict_datapoints['instance_id']=instance_id
    dict_datapoints['region']=region
    dict_datapoints['StartTime']=args['StartTime']
    dict_datapoints['EndTime']=args['EndTime']
#    print("dict_datapoints=",dict_datapoints)
    return json.dumps(dict_datapoints,default = myconverter)
 #   return json.dumps(dict_datapoints,default = myconverter)
 #   json_str = json.dumps(datapoints)
  #  print(datapoints)
    #last_datapoint = sorted(datapoints, key=itemgetter('Timestamp'))[-1]
    #utilization = last_datapoint['Average']
    #load = round((utilization/100.0), 2)
    #timestamp = str(last_datapoint['Timestamp'])
    #print("{0} load at {1}".format(load, timestamp))

def get_ec2_instances(args):
    connect.get_access()
    access_key = connect.get_access.aws_access_key_id
    secret_key = connect.get_access.aws_secret_access_key
    client = boto3.client('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key,region_name='ap-south-1')
#    dict_time=json.loads(sys.argv[1].replace("'", '"'))
    #print(dict_time)
    s_time=args['StartTime']
    e_time=args['EndTime']

    stime=datetime.datetime.strptime(s_time,'%Y-%m-%d')
    etime=datetime.datetime.strptime(e_time,'%Y-%m-%d')

    #client=connect.ec2_connect()
    ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
    for region in ec2_regions:
        conn = boto3.resource('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key,region_name=region)
        instances = conn.instances.filter()
        for instance in instances:
            #if instance.state["Name"] == "running":
#                print (instance.id, instance.instance_type, region)
                 pprint(get_cpu_utilization({"Namespace":"AWS/EC2","StartTime": stime,"EndTime": etime,"MetricName": "CPUUtilization", "Period": 86400,"Dimensions": [{"Name": "InstanceId","Value": instance.id}],"InstanceId":instance.id,"Region":region}))

get_ec2_instances({'StartTime':'2018-08-06','EndTime':'2018-08-08'})