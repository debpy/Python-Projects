from sys import exit
from datetime import datetime, timedelta
from operator import itemgetter
from requests import get
from boto3.session import Session
from sys import exit
from operator import itemgetter
from requests import get
from pprint import pprint


def get_cloudwatch_metrics(args):
    session = Session(aws_access_key_id='********',aws_secret_access_key='************',
    region_name='ap-south-1')
    cw = session.client('cloudwatch')
    results = cw.get_metric_statistics(
    Namespace=args['Namespace'],
    MetricName=args['MetricName'],
    Dimensions=args['Dimensions'],
    StartTime=args['StartTime'],
    EndTime=args['EndTime'],
    Period=args['Period'],
    Statistics=['Average'])    
    datapoints = results['Datapoints']
    return datapoints



def get_ec2_instances():
    access_key = "********"
    secret_key = "**************"
    client = boto3.client('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key,region_name='ap-south-1')
    ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
    for region in ec2_regions:
        conn = boto3.resource('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key,region_name=region)
        instances = conn.instances.filter()
        for instance in instances:
            if instance.state["Name"] == "running":
                print (instance.id, instance.instance_type, region)
pprint(get_cloudwatch_metrics({"Namespace":"AWS/EC2","StartTime": "2018-08-02","EndTime": "2018-08-03","MetricName": "CPUUtilization",
"Period": 86400,"Dimensions": [
            {
                "Name": "InstanceId",
                "Value": "i-0482b66178be7b391"
            }
        ],
    }))