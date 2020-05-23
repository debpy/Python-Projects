#This program will print all snapshots of EBS volumes
import boto3
from  connect import *
import json
from botocore.exceptions import ClientError
from pprint import pprint
import datetime
def get_all_snapshots():
    client=ec2_connect()
    regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
    for region in regions:
        resource=boto3.resource('ec2',region_name=region,aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key)
        client=boto3.client('ec2',region_name=region,aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key)
        volumes=resource.volumes.all()
        for v in volumes:
            for snap in client.describe_snapshots(OwnerIds=['self'])['Snapshots']:
                if snap['VolumeId']==v.volume_id:
                    print(snap['SnapshotId'])
get_all_snapshots()
