#This program will list all EBS volumes present across all regions
import boto3
from  connect import aws_access_key_id,aws_secret_access_key,region_name
import json
from botocore.exceptions import ClientError
from pprint import pprint
import datetime

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def get_all_volumes():
    ec2 = boto3.client('ec2',aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)
    vol_dict={}
    vol_list=[]
    vol_final_dict={}
    for region in ec2.describe_regions()['Regions']:
        ec2_resource = boto3.resource('ec2', region_name=region['RegionName'],aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        ec2_client = boto3.client('ec2',aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region['RegionName'])
        volume_iterator = ec2_resource.volumes.all()
        for v in volume_iterator:
        ###Find volumes that are not attached and in available state
            if v.attachments == [] and  v.state=='available':
                print("Volume id=",v.volume_id)
                ###Creating snapshots of inactive volumes
                reservations =ec2_client.create_snapshot(VolumeId=v.volume_id,Description="Snapshot for the volume" + v.volume_id)
                result = reservations["SnapshotId"]
                print("Result=",result)
                ec2_client.create_tags(Resources=[result],Tags=[{"Key": 'Name', "Value": "snapshot" },])
                vol_dict.update({"VolumeId":v.volume_id,"State":v.state,"Type":v.volume_type,"Iops":v.iops,"SnapshotId":v.snapshot_id,"CreateTime":v.create_time,"Size":v.size,"AvailabilityZone":v.availability_zone})
                vol_list.append(vol_dict.copy())
    vol_final_dict["Volumes"]=vol_list
    print(json.dumps(vol_final_dict,default=myconverter))

get_all_volumes()