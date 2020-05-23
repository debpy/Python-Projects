#The program will find all the stopped ec2 instances for more than 30 days across all regions 
from datetime import datetime, timedelta  
import json
import boto3
from  connect import aws_access_key_id,aws_secret_access_key,region_name
import pprint
from datetime import timezone
import pytz
utc=pytz.UTC

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

        ec2_client.describe_instances()['Reservations'][0]['Instances'][0]['LaunchTime']

def stopped_ec2_instances(args):
        inst_dict={}
        inst_list=[]
        inst_final_dict={}
        today = datetime.now(timezone.utc)+ timedelta(days=1)  #
        days_arg=args['days']
        one_month= timedelta(days=days_arg)  #########
        start_date = today - one_month
        ec2 = boto3.client('ec2',aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)
        for region in ec2.describe_regions()['Regions']:
            ses=boto3.Session(region_name=region['RegionName'],aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
            ec2_client = ses.client('ec2')	
            if ec2_client.describe_instances()['Reservations'] == []:
                pass
            else:
                state=ec2_client.describe_instances()['Reservations'][0]['Instances'][0]['State']['Name']
                instance_id=ec2_client.describe_instances()['Reservations'][0]['Instances'][0]['InstanceId']
                LaunchTime=ec2_client.describe_instances()['Reservations'][0]['Instances'][0]['LaunchTime']
                if state=='stopped' and LaunchTime < start_date:
                    inst_dict.update({"InstanceId":instance_id,"Region":region['RegionName']})
                    inst_list.append(inst_dict.copy())
        return inst_list
        #inst_final_dict["Instances"]=inst_list
        #print(json.dumps(inst_final_dict,default=myconverter))

#get_stopped_ec2_instances()