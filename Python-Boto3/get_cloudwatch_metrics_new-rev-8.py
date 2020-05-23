import boto3
from  connect import aws_access_key_id,aws_secret_access_key,region_name
import json
from botocore.exceptions import ClientError
from pprint import pprint
import datetime