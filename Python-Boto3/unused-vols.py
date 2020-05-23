#This program will print ununsed EBS volumes and create snapshots for them
import boto3
from  connect import aws_access_key_id,aws_secret_access_key,region_name
import json
from botocore.exceptions import ClientError
from pprint import pprint
import datetime
#from datetime import datetime

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def get_metrics(volume_id,start_time,end_time,region):
    """Get volume idle time on an individual volume over `start_date`
       to today"""
    cloudwatch = boto3.client("cloudwatch",aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region)
    metrics = cloudwatch.get_metric_statistics(
        Namespace='AWS/EBS',
        MetricName='VolumeIdleTime',
        Dimensions=[{'Name': 'VolumeId', 'Value': volume_id}],
        Period=3600,  # every hour
        StartTime=start_time,
        EndTime=end_time,
        Statistics=['Minimum'],
        Unit='Seconds'
    )
    return metrics['Datapoints']

def get_unused_volumes(data):
    StartTime=data['StartTime']
    EndTime=data['EndTime']
    IdleDays=data['IdleDays']
    ec2 = boto3.client('ec2',aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)
    vol_dict={}
    vol_list=[]
    vol_final_dict={}
    IdleSeconds=(IdleDays*24*3600)-1
    start_time=str(StartTime)
    end_time=str(EndTime)
    start_time=datetime.datetime.strptime(start_time, '%Y-%m-%d')
    #print("start_time=",start_time)
    end_time=datetime.datetime.strptime(end_time, '%Y-%m-%d')
    #print("end_time=",end_time)
    #print("IdleSeconds=",IdleSeconds)
#    all_regions=ec2.describe_regions()['Regions']
#    print(all_regions)
    for region in ec2.describe_regions()['Regions']:
        ses=boto3.Session(region_name=region['RegionName'],aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        ec2_resource = ses.resource('ec2')
        ec2_client = ses.client('ec2')
        volume_iterator = ec2_resource.volumes.all()
        for v in volume_iterator:
#            print(v)
        ###Find volumes that are not attached and in available state
            if v.attachments == [] and  v.state=='available':
#                print("Volume id=",v.volume_id)
                ###Creating snapshots of inactive volumes
                metrics=get_metrics(v.volume_id,start_time,end_time,region['RegionName'])
#                print("Metrics=",metrics)
                if len(metrics):
                    for metric in metrics:
                        if metric['Minimum'] > IdleSeconds:
                            reservations =ec2_client.create_snapshot(VolumeId=v.volume_id,Description="Snapshot for the volume" + v.volume_id)
                            result = reservations["SnapshotId"]
                #print("Result=",result)
                            ec2_client.create_tags(Resources=[result],Tags=[{"Key": 'Name', "Value": "snapshot" },])
                            vol_dict.update({"VolumeId":v.volume_id,"State":v.state,"Type":v.volume_type,"Iops":v.iops,"SnapshotId":result,"CreateTime":v.create_time,"Size":v.size,"AvailabilityZone":v.availability_zone})
                            vol_list.append(vol_dict.copy())
    return vol_list
#    vol_final_dict["Volumes"]=vol_list######
#    print(json.dumps(vol_final_dict,default=myconverter))####

#get_all_volumes()
#get_unused_volumes({"StartTime":"2018-08-27","EndTime":"2018-08-28","IdleDays":1})
