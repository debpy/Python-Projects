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
def get_ec2_instances():
    connect.get_access()
    access_key = connect.get_access.aws_access_key_id
    secret_key = connect.get_access.aws_secret_access_key
    print(access_key)
    print(secret_key)
    '''
    client = boto3.client('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key,region_name='ap-south-1')

    ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
    for region in ec2_regions:
        conn = boto3.resource('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key,region_name=region)
        instances = conn.instances.filter()
        for instance in instances:
            if instance.state["Name"] == "running":
                print (instance.id, instance.instance_type, region)
'''
get_ec2_instances()