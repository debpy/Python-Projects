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


def get_ec2_instances():
	#client = boto3.client('ec2')
	client=connect.ec2_connect()
	ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]	
	public_ip={'PublicIp':[]}
	for region in ec2_regions:
		client = boto3.client('ec2', aws_access_key_id=connect.aws_access_key_id, aws_secret_access_key=connect.aws_secret_access_key, region_name=region)
		address = client.describe_addresses()
		if address['Addresses'] != []:
			for address in address['Addresses']:		
				if 'InstanceId' not in address:
					public_ip['PublicIp'].append(address['PublicIp'])
					#client.release_address(AllocationId=address['AllocationId'])#
	public_ip_json=json.dumps(public_ip)
	return public_ip_json
	#print(public_ip_json)
	
		#print(address['PublicIp'])
print(get_ec2_instances())