import config
import argparse
import boto3


def get_ec2_instances(region):
    conn = config.connect()
    ''' Makes an AWS API call to the list of EC2 instances in all
            regions '''

    ec2_conn = conn.ec2.connect_to_region()
    reservations = ec2_conn.get_all_reservations()
    for reservation in reservations:
        print(region + ':', reservation.instances)

    for vol in ec2_conn.get_all_volumes():
        print(region + ':', vol.id)

    # instances = conn.instances.filter(
    #     Filters=[{'Name': 'instance-state-name', 'Values': ['stopped', 'terminated']}])
    #
    # for instance in instances:
    #     print(instance.id, instance.instance_type)


def main():
    conn = config.connect()
    ec2_regions = [region['RegionName'] for region in conn.describe_regions()['Regions']]
    print(ec2_regions)
    for region in ec2_regions:
        get_ec2_instances(region)


if __name__ == '__main__':
    main()
