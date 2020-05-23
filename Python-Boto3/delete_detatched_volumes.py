#This program will delete the unattached volumes
import boto3
from  connect import aws_access_key_id,aws_secret_access_key,region_name
import json
from pprint import pprint

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def delete_unattached_volumes():
    ec2 = boto3.client('ec2',aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)
    vol_dict={}
    vol_list=[]
    vol_final_dict={}
    for region in ec2.describe_regions()['Regions']:
        ses=boto3.Session(region_name=region['RegionName'],aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        ec2_resource = ses.resource('ec2')
        ec2_client = ses.client('ec2')
        volume_iterator = ec2_resource.volumes.all()
        for v in volume_iterator:
        ###Find volumes that are not attached and in available state
            if v.attachments == [] :
                #print("Volume id=",v.volume_id)
                v_id=v.volume_id
                v.delete()
                vol_dict.update({"VolumeId":v_id,"Type":v.volume_type,"AvailabilityZone":v.availability_zone})
                vol_list.append(vol_dict.copy())
    vol_final_dict["Volumes"]=vol_list
    print(json.dumps(vol_final_dict,default=myconverter))

delete_unattached_volumes()