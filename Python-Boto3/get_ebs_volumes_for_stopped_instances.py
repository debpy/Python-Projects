import boto3
from  connect import *
import json
from botocore.exceptions import ClientError
from pprint import pprint
import datetime
client = ec2_connect()
regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
def get_volumes_for_stopped_instances():
    vol_dict={}
    vol_list=[]
    for region in regions:
        client=boto3.client('ec2',region_name=region,aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        resource=boto3.resource('ec2',region_name=region,aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        filters = [{  'Name': 'instance-state-name', 'Values': ['stopped']}]
        for instance in client.describe_instances(Filters=filters)['Reservations']:
            instance_id=instance['Instances'][0]['InstanceId']
            instance = resource.Instance(instance_id)
            volumes=instance.volumes.all()
            for v in volumes:
                vol_dict.update({"VolumeId":v.volume_id,"State":v.state,"Type":v.volume_type,"CreateTime":v.create_time,"AvailabilityZone":v.availability_zone,"Snapshot Id":v.snapshot_id})
                vol_list.append(vol_dict.copy())
    return vol_list
