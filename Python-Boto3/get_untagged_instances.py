def untagged_instances():
    import boto3
    import json
    from pprint import pprint
    from  connect import aws_access_key_id,aws_secret_access_key,region_name
    client = boto3.client('ec2',region_name=region_name,aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
    list_instances=[]
    dict_output={}
    dict_final_output={}
    for region in ec2_regions:
        sess = boto3.Session(region_name=region,aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        ec2_client=sess.client('ec2')
        response = ec2_client.describe_instances()
        obj_number = len(response['Reservations'])
        for objects in range(obj_number):
            try:
                z = response['Reservations'][objects]['Instances'][0]['Tags'][0]['Key']
            except KeyError as e:
                untagged_instanceid = response['Reservations'][objects]['Instances'][0]['InstanceId']
                region_name=region
                dict_output={"instance_id":untagged_instanceid,"region":region_name}
                list_instances.append(dict_output.copy())
    #dict_final_output={"Untagged_instances":list_instances}
    #print(json.dumps(dict_final_output))
    return list_instances
