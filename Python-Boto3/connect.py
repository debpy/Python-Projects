import boto3
def connect():
    return boto3.client('cloudwatch',region_name="ap-south-1",aws_access_key_id="***************",aws_secret_access_key="*************")
def ec2_connect():
	return   boto3.client('ec2', aws_access_key_id="*****************", aws_secret_access_key="************",region_name='ap-south-1')
def get_access():
	get_access.aws_access_key_id="*****************"
	get_access.aws_secret_access_key="***********************"

aws_access_key_id="*************"
aws_secret_access_key="*********************"
region_name='ap-south-1'
