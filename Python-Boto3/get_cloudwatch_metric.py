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

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
'''
def jsonDefault(object):
    return object.__dict__
'''
class CpuUtilization:
    def get_cputilization(self,args):
        instance_id=args['InstanceId']
        region=args['Region']
        conn=connect.connect()
        results=conn.get_metric_statistics(
        Namespace=args['Namespace'],
        MetricName=args['MetricName'],
        Dimensions=args['Dimensions'],
        StartTime=args['StartTime'],
        EndTime=args['EndTime'],
        Period=args['Period'],
        Statistics=['Average'])
    #    print("Instance id=",instance_id)
        datapoints = results['Datapoints']
    #    print("datapoints=",datapoints)    
        dict_datapoints=dict((key,d[key]) for d in datapoints for key in d)
 #   print("dict_datapoints=",dict_datapoints)
 #   print("The average CPU Utilization in percentage is", dict_datapoints['Average'])
        if  dict_datapoints:
            if dict_datapoints['Average'] < 8.0:
     #    print("The average CPU Utilization has been less than 8% for the last 30 days")
                final_dict={'InstanceId':instance_id}
                final_dict.update({'Region':region})
                final_dict.update({'Average':dict_datapoints['Average']})
                return final_dict
            else:
                print("The average CPU Utilization is above the threshold 8% for the last 30 days")

        #list_datapoints=list(datapoints)
  #          dict_datapoints['instance_id']=instance_id
  #         dict_datapoints['region']=region
  #          dict_datapoints['StartTime']=args['StartTime']
  #          dict_datapoints['EndTime']=args['EndTime']
  #      return json.dumps(dict_datapoints,default = myconverter)


class NetworkOutput:
    def get_network_output(self,args):
        instance_id=args['InstanceId']
        region=args['Region']
        conn=connect.connect()
        results_network_output=conn.get_metric_statistics(
        Namespace=args['Namespace'],
        MetricName=args['MetricName'],
        Dimensions=args['Dimensions'],
        StartTime=args['StartTime'],
        EndTime=args['EndTime'],
        Period=args['Period'],
        Statistics=['Sum'])
        datapoints_network_output = results_network_output['Datapoints']
        #print("datapoints_network_output=",datapoints_network_output)
        if  datapoints_network_output:
            network_output=datapoints_network_output[0]['Sum']
            return network_output

class NetworkInput:
    def get_network_input(self,args):
        instance_id=args['InstanceId']
        region=args['Region']
        conn=connect.connect()
        results_network_input=conn.get_metric_statistics(
        Namespace=args['Namespace'],
        MetricName=args['MetricName'],
        Dimensions=args['Dimensions'],
        StartTime=args['StartTime'],
        EndTime=args['EndTime'],
        Period=args['Period'],
        Statistics=['Sum'])
        datapoints_network_input = results_network_input['Datapoints']
        #print("datapoints_network_input=",datapoints_network_input)
        if datapoints_network_input:
            network_input=datapoints_network_input[0]['Sum']
            return network_input

def get_ec2_instances(args):
    connect.get_access()
    aws_access_key_id = connect.get_access.aws_access_key_id
    aws_secret_access_key = connect.get_access.aws_secret_access_key
    client = boto3.client('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,region_name='ap-south-1')

    s_time=args['StartTime']
    e_time=args['EndTime']

    stime=datetime.datetime.strptime(s_time,'%Y-%m-%d')
    etime=datetime.datetime.strptime(e_time,'%Y-%m-%d')
    
    cpu=CpuUtilization()
    ni=NetworkInput()
    no=NetworkOutput()

    final_list=[]
    json_dict={}
    ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
    for region in ec2_regions:
        ses=boto3.Session(region_name=region,aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        ses_resource = ses.resource('ec2',region_name=region)
        ses_client = ses.client('ec2',region_name=region)
        #ec2 = ses.resource('ec2',region_name=region)
        instances = ses_resource.instances.filter()
        for instance in instances:
            #if instance.state["Name"] == "running":
                 print (instance.id, instance.instance_type, region)
                 final_dict=cpu.get_cputilization({"Namespace":"AWS/EC2","StartTime": stime,"EndTime": etime,"MetricName": "CPUUtilization", "Period": 86400,"Dimensions": [{"Name": "InstanceId","Value": instance.id}],"InstanceId":instance.id,"Region":region})
                 network_output=no.get_network_output({"Namespace":"AWS/EC2","StartTime": stime,"EndTime": etime,"MetricName": "NetworkOut", "Period": 86400,"Dimensions": [{"Name": "InstanceId","Value": instance.id}],"InstanceId":instance.id,"Region":region})
                 network_input=ni.get_network_input({"Namespace":"AWS/EC2","StartTime": stime,"EndTime": etime,"MetricName": "NetworkIn", "Period": 86400,"Dimensions": [{"Name": "InstanceId","Value": instance.id}],"InstanceId":instance.id,"Region":region})
                 print("network_output=",network_output)
                 print("network_input=",network_input)
                 if network_output is not None and network_input is not None:
                    total_network_io=network_output+network_input
                    print("The total network I/O consumption in bytes is: ",total_network_io)
                    total_network_io_mb=round((total_network_io/1000000.0), 2)
                    print("The total network I/O consumption in MB is: ",total_network_io_mb)
                    if total_network_io_mb < 20.0:
                        print("The average Network I/O has been less than 20 MB for the last 30 days")
                        final_dict.update({'Sum':total_network_io_mb})
                        final_list.append(final_dict)
                        #final_dict=json.dumps(final_dict)
                        print(final_list)
                    else:
                        pass
                 else:
                    pass 
        #print(final_list)
    json_dict["Instance_details"]=final_list
    print(json.dumps(json_dict))
get_ec2_instances({'StartTime':'2018-08-06','EndTime':'2018-08-16'})